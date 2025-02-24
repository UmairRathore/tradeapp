<?php

namespace Database\Factories;

use App\Models\MatchSchedule;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\CapitalReserve>
 */
class CapitalReserveFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = CapitalResrve::class;

    public function definition()
    {
        return [
            'match_id' => MatchSchedule::factory(),
            'reserve_percentage' => $this->faker->randomFloat(2, 1, 20),
            'total_reserved_amount' => $this->faker->randomFloat(2, 1000, 50000),
        ];
    }
}
