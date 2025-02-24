<?php

namespace Database\Factories;

use App\Models\Referral;
use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Referral>
 */
class ReferralFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = Referral::class;

    public function definition()
    {
        return [
            'referrer_id' => User::factory(),
            'referred_id' => User::factory(),
            'bonus_amount' => $this->faker->randomFloat(2, 10, 100),
            'awarded_at' => now(),
        ];
    }
}
