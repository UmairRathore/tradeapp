<?php

namespace Database\Factories;

use App\Models\MatchSchedule;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\MatchSchedule>
 */
class MatchScheduleFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = MatchSchedule::class;

    public function definition()
    {
        return [
            'match_name' => $this->faker->sentence(3),
            'match_date' => $this->faker->dateTimeBetween('now', '+1 week'),
            'status' => $this->faker->randomElement(['upcoming', 'ongoing', 'completed']),
        ];
    }
}
