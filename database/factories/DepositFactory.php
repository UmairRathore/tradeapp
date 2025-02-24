<?php

namespace Database\Factories;

use App\Models\Deposit;
use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Deposit>
 */
class DepositFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = Deposit::class;

    public function definition()
    {
        return [
            'user_id' => User::factory(),
            'amount' => $this->faker->randomFloat(2, 100, 10000),
            'payment_method' => $this->faker->randomElement(['USDT', 'Bank Transfer']),
            'transaction_id' => $this->faker->uuid,
            'proof' => null,
            'status' => $this->faker->randomElement(['pending', 'approved', 'rejected']),
            'requested_at' => now(),
            'approved_at' => null,
            'rejection_reason' => null,
        ];
    }
}
