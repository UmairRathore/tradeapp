<?php

namespace Database\Factories;

use App\Models\User;
use App\Models\Withdrawal;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Withdrawal>
 */
class WithdrawalFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = Withdrawal::class;

    public function definition()
    {
        return [
            'user_id' => User::factory(),
            'amount' => $this->faker->randomFloat(2, 100, 5000),
            'payment_method' => $this->faker->randomElement(['USDT', 'Bank Transfer']),
            'account_details' => $this->faker->iban,
            'status' => $this->faker->randomElement(['pending', 'approved', 'rejected']),
            'requested_at' => now(),
            'processed_at' => null,
            'rejection_reason' => null,
        ];
    }
}
