<?php

namespace Database\Factories;

use App\Models\MatchSchedule;
use App\Models\TradeLimit;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\TradeLimit>
 */
class TradeLimitFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = TradeLimit::class;

    public function definition()
    {
        return [
            'match_id' => MatchSchedule::factory(),
            'min_trade_amount' => $this->faker->randomFloat(2, 50, 500),
            'max_trade_amount' => $this->faker->randomFloat(2, 1000, 10000),
            'roi_percentage' => $this->faker->randomFloat(2, 1, 20),
        ];
    }
}
