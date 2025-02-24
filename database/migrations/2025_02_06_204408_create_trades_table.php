<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('trades', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained('users')->onDelete('cascade');
            $table->enum('trade_type', ['score', 'runs'])->default('score'); // Define trade options
            $table->string('match_name');
            $table->decimal('amount', 15, 2);
            $table->decimal('roi', 5, 2);
            $table->decimal('total_earnings', 15, 2)->storedAs('amount * roi');
            $table->enum('trade_status', ['running', 'completed', 'cancelled'])->default('running');
            $table->enum('winning_status', ['pending', 'won', 'lost'])->default('pending');
            $table->timestamp('trade_start_time');
            $table->timestamp('trade_end_time')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('trades');
    }
};
