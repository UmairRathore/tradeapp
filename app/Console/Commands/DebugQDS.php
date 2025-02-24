<?php

namespace App\Console\Commands;

use App\Jobs\ProcessQds;
use Illuminate\Console\Command;

class DebugQDS extends Command
{
    protected $signature = 'debug:qds {passager_id}';
    protected $description = 'Debug the QDS handling process';

    public function handle()
    {
        $passager_id = $this->argument('passager_id');
        $yourClassInstance = new ProcessQds($passager_id); // Adjust the class instantiation accordingly
        $yourClassInstance->handle();
    }
}
