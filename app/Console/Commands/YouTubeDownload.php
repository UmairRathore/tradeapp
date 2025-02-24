<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\File;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class YouTubeDownload extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'youtube:download {url} {--format=mp4} {--output=storage/youtube}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Download YouTube videos as MP3 or MP4 using yt-dlp';

    /**
     * Execute the console command.
     */
    public function handle()
    {
        $url = $this->argument('url');
        $format = strtolower($this->option('format')); // mp3 or mp4
        $outputDir = rtrim($this->option('output'), '/');

        // Ensure the output directory exists
        if (!File::exists($outputDir)) {
            File::makeDirectory($outputDir, 0777, true, true);
        }

        // Use correct escaping for Windows & Linux
        $outputTemplate = "\"{$outputDir}/%(title)s.%(ext)s\"";

        // yt-dlp command
        $ytDlpCommand = [
            'yt-dlp',
            '--no-playlist',
            '--no-warnings',
            '--output', $outputTemplate
        ];

        // Choose format
        if ($format === 'mp3') {
            $ytDlpCommand[] = '--extract-audio';
            $ytDlpCommand[] = '--audio-format';
            $ytDlpCommand[] = 'mp3';
        } else {
            $ytDlpCommand[] = '--format';
            $ytDlpCommand[] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4';
        }

        $ytDlpCommand[] = $url;

        // Run process with verbose mode
        $process = new Process($ytDlpCommand);
        $process->setTimeout(600); // Set timeout (600 seconds)
        $process->run();

        // Check for errors
        if (!$process->isSuccessful()) {
            $this->error("❌ Download failed!");
            $this->error("Error Output: " . $process->getErrorOutput());
            throw new ProcessFailedException($process);
        }

        $this->info("✅ Download completed! Files saved in '{$outputDir}'.");
    }
}
