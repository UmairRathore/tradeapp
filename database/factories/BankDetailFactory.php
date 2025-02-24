<?php

namespace Database\Factories;

use App\Models\BankDetail;
use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\BankDetail>
 */
class BankDetailFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = BankDetail::class;

    public function definition()
    {
        return [
            'user_id' => User::factory(),
            'bank_name' => $this->faker->company,
            'account_holder_name' => $this->faker->name,
            'account_number' => $this->faker->bankAccountNumber,
            'branch' => $this->faker->city,
            'ifsc_code' => strtoupper($this->faker->lexify('??????')),
            'status' => $this->faker->randomElement(['active', 'inactive']),
        ];
    }
}
