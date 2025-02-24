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
        Schema::create('trade_limits', function (Blueprint $table) {
            $table->id();
            $table->foreignId('match_id')->constrained('match_schedules')->onDelete('cascade');
            $table->decimal('min_trade_amount', 15, 2)->default(0.00); // Minimum amount a user can trade
            $table->decimal('max_trade_amount', 15, 2)->default(0.00); // Maximum amount a user can trade
            $table->decimal('roi_percentage', 5, 2)->default(0.00); // ROI percentage for the trade
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('trade_limits');
    }
};
