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
        Schema::create('capital_reserves', function (Blueprint $table) {
            $table->id();
            $table->foreignId('match_id')->constrained('match_schedules')->onDelete('cascade');
            $table->decimal('reserve_percentage', 5, 2); // Percentage of capital reserved
            $table->decimal('total_reserved_amount', 15, 2)->default(0.00);
            $table->timestamps();;
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('captial_reserves');
    }
};
