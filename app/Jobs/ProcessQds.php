<?php

namespace App\Jobs;

use App\Models\CapitaineRating;
use App\Models\CroisiereRating;
use App\Models\GeneralRating;
use App\Models\HotesseRating;
use App\Models\Passager;
use App\Models\QDS;
use App\Models\QdsLogs;
use App\Models\ReparterCroisiere;
use App\Models\RepasRating;
use App\Models\ShipRating;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;
use Illuminate\Support\Facades\Log;
use Symfony\Component\Process\Process;

class ProcessQds implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    protected $passager_id;
    public $timeout;
    public $time_start;
    private $json_results = [];

    public function __construct($passager_id)
    {
        $this->passager_id = $passager_id;
        $this->timeout = env('MAX_TRAITEMENT_SECOND', 60);
    }

    public function handle(): void
    {
        $this->time_start = time();
        $process = new Process(['python3', base_path() . '/PDF_OCR/main.py']);
        $process->start();

        Log::info("Watching for CSV output in PDF_OCR/Result folder");

        $timeout = 60;
        $startTime = time();

        while ((time() - $startTime) < $timeout) {
            $files = glob(base_path() . '/PDF_OCR/Result/*.csv');

            if (!empty($files)) {
                foreach ($files as $file) {
                    Log::info("Processing new CSV file: " . $file);

                    $csv_data = [];
                    if (($handle = fopen($file, "r")) !== FALSE) {
                        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
                            if (empty($data) || count($data) < 2) continue;
                            $csv_data[$data[0]] = $data[1];
                        }
                        fclose($handle);
                    }

                    $this->json_results = $csv_data;

                    $jsonFilePath = base_path() . '/PDF_OCR/Result/result_' . $this->passager_id . '.json';
                    file_put_contents($jsonFilePath, json_encode($this->json_results, JSON_PRETTY_PRINT));
                    Log::info("JSON result saved: " . $jsonFilePath);

                    break;
                }
                break;
            }

            sleep(2);
        }

        Log::info("Finished processing CSV files.");
    }
}
