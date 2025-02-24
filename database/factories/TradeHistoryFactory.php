<?php
namespace Database\Factories;

use App\Models\TradeHistory;
use App\Models\User;
use App\Models\Trade;
use Illuminate\Database\Eloquent\Factories\Factory;

class TradeHistoryFactory extends Factory
{
    protected $model = TradeHistory::class;

    public function definition()
    {
        return [
            'user_id' => User::factory(),
            'trade_id' => Trade::factory(),
            'amount' => $this->faker->randomFloat(2, 50, 5000),
            'roi' => $this->faker->randomFloat(2, 1, 20),
            'total_earnings' => $this->faker->randomFloat(2, 50, 10000),
            'trade_status' => $this->faker->randomElement(['running', 'completed', 'cancelled']),
            'winning_status' => $this->faker->randomElement(['pending', 'won', 'lost']),
            'trade_start_time' => $this->faker->dateTimeBetween('-1 week', 'now'),
            'trade_end_time' => $this->faker->dateTimeBetween('now', '+1 week'),
        ];
    }
}
