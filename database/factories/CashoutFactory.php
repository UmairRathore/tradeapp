<?php

namespace Database\Factories;

use App\Models\BankDetail;
use App\Models\Cashout;
use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Cashout>
 */
class CashoutFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = Cashout::class;

    public function definition()
    {
        return [
            'user_id' => User::factory(),
            'bank_detail_id' => BankDetail::factory(),
            'amount' => $this->faker->randomFloat(2, 50, 5000),
            'status' => $this->faker->randomElement(['pending', 'approved', 'rejected']),
            'requested_at' => now(),
            'processed_at' => null,
            'rejection_reason' => null,
        ];
    }
}
