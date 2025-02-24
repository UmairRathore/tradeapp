<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use thiagoalessio\TesseractOCR\TesseractOCR;
use PhpOffice\PhpWord\PhpWord;
use PhpOffice\PhpWord\IOFactory;
use Illuminate\Support\Facades\Storage;

class ExtractTextFromImages extends Command
{
    protected $signature = 'extract:images';
    protected $description = 'Extract text from images and save to a Word document';

    public function handle()
    {
        $imageFolder = storage_path('app/public/images'); // Folder where images are stored
        $outputFile = storage_path('app/public/Extracted_Text.rtf'); // Output file

        // Ensure the folder exists
        if (!is_dir($imageFolder)) {
            $this->error("❌ Image folder does not exist: $imageFolder");
            return;
        }

        // Get list of image files
        $files = scandir($imageFolder);
        $imageFiles = array_filter($files, function ($file) use ($imageFolder) {
            return preg_match('/\.(png|jpg|jpeg)$/i', $file) && is_file("$imageFolder/$file");
        });

        if (empty($imageFiles)) {
            $this->error("⚠️ No images found in $imageFolder");
            return;
        }

        $phpWord = new PhpWord();
        $section = $phpWord->addSection();

        foreach ($imageFiles as $image) {
            $imagePath = "$imageFolder/$image";
            $this->info("🔍 Extracting text from: $image");

            try {
                // Extract text using Tesseract OCR
                $text = (new TesseractOCR($imagePath))
                    ->lang('eng') // Set OCR language
                    ->run();

                // Convert text to UTF-8 encoding
                $text = mb_convert_encoding($text, 'UTF-8', 'auto');

                // Ensure Word compatibility by removing invalid characters
                $text = preg_replace('/[^\x20-\x7E\xA0-\xFF]/', '', $text);

                // Add extracted text to Word document
                $section->addText($text, ['name' => 'Arial', 'size' => 12]);

                // Add a page break after each image's text
                $section->addPageBreak();
            } catch (\Exception $e) {
                $this->error("❌ Error processing $image: " . $e->getMessage());
            }
        }

        try {
            // Save Word document properly
            $writer = IOFactory::createWriter($phpWord, 'RTF');
            $writer->save($outputFile);

            $this->info("✅ Extraction complete! Word file saved: $outputFile");
        } catch (\Exception $e) {
            $this->error("❌ Failed to save Word document: " . $e->getMessage());
        }
    }
}
