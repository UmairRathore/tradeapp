<?php

namespace Database\Factories;

use App\Models\Trade;
use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Trade>
 */
class TradeFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = Trade::class;

    public function definition()
    {
        return [
            'user_id' => User::factory(),
            'match_name' => $this->faker->sentence(3),
            'amount' => $this->faker->randomFloat(2, 50, 5000),
            'roi' => $this->faker->randomFloat(2, 1, 20),
            'trade_type' => $this->faker->randomElement(['score', 'runs']),
            'trade_status' => $this->faker->randomElement(['running', 'completed', 'cancelled']),
            'winning_status' => $this->faker->randomElement(['pending', 'won', 'lost']),
            'trade_start_time' => $this->faker->dateTimeBetween('-1 week', 'now'),
            'trade_end_time' => $this->faker->dateTimeBetween('now', '+1 week'),
        ];
    }
}
