<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\File;

class CropImagesGD extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'images:collage {directory} {--size=300} {--output=collage.jpg} {--background=#eaf4e3}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Center crop and merge images into a stylish slanted collage';

    /**
     * Execute the console command.
     */
    public function handle()
    {
        $directory = rtrim($this->argument('directory'), '/');
        $size = (int)$this->option('size');
        $outputFile = $this->option('output');
        $backgroundColor = $this->option('background');

        if (!File::exists($directory) || !File::isDirectory($directory)) {
            $this->error("❌ The directory '{$directory}' does not exist.");
            return;
        }

        $outputDir = "{$directory}/collage";
        if (!File::exists($outputDir)) {
            File::makeDirectory($outputDir, 0777, true);
        }

        $files = File::files($directory);
        $supportedExtensions = ['jpg', 'jpeg', 'png'];
        $croppedImages = [];

        foreach ($files as $file) {
            $extension = strtolower($file->getExtension());
            if (!in_array($extension, $supportedExtensions)) {
                continue;
            }

            $imagePath = $file->getRealPath();
            $image = match ($extension) {
                'jpg', 'jpeg' => @imagecreatefromjpeg($imagePath),
                'png' => @imagecreatefrompng($imagePath),
                default => null
            };

            if (!$image) {
                $this->error("❌ Failed to load image: {$file->getFilename()}");
                continue;
            }

            $width = imagesx($image);
            $height = imagesy($image);
            $cropSize = min($width, $height);
            $x = (int)(($width - $cropSize) / 2);
            $y = (int)(($height - $cropSize) / 2);

            // Center crop
            $cropped = imagecreatetruecolor($cropSize, $cropSize);
            imagecopy($cropped, $image, 0, 0, $x, $y, $cropSize, $cropSize);

            // Resize to fixed size
            $resized = imagecreatetruecolor($size, $size);
            imagecopyresampled($resized, $cropped, 0, 0, 0, 0, $size, $size, $cropSize, $cropSize);

            $croppedImages[] = $resized;

            imagedestroy($image);
            imagedestroy($cropped);
        }

        if (empty($croppedImages)) {
            $this->error("❌ No valid images found in '{$directory}'.");
            return;
        }

        // Canvas setup
        $totalWidth = count($croppedImages) * ($size * 0.85);
        $totalHeight = $size * 1.2;
        $canvas = imagecreatetruecolor($totalWidth, $totalHeight);

        // Convert HEX background color to RGB
        list($r, $g, $b) = sscanf($backgroundColor, "#%02x%02x%02x");
        $bgColor = imagecolorallocate($canvas, $r, $g, $b);
        imagefilledrectangle($canvas, 0, 0, $totalWidth, $totalHeight, $bgColor);

        // Merge images with slight tilt
        $xOffset = 20; // Start with some margin
        foreach ($croppedImages as $index => $img) {
            $angle = ($index % 2 === 0) ? -10 : 10; // Alternate angles
            $rotated = imagerotate($img, $angle, $bgColor);

            imagecopy($canvas, $rotated, $xOffset, 20, 0, 0, imagesx($rotated), imagesy($rotated));
            $xOffset += $size * 0.85; // Adjust spacing
            imagedestroy($rotated);
            imagedestroy($img);
        }

        // Save final collage
        $collagePath = "{$outputDir}/{$outputFile}";
        imagejpeg($canvas, $collagePath, 90);
        imagedestroy($canvas);

        $this->info("✅ Stylish collage created: {$collagePath}");
    }
}
