<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class MatchSchedule extends Model
{
    use HasFactory;

    protected $table = 'match_schedules';

    protected $fillable = [
        'match_name', 'match_date', 'status'
    ];

    protected $casts = [
        'match_date' => 'datetime',
    ];

    public function capitalReserves(): HasMany
    {
        return $this->hasMany(CapitalReserve::class);
    }
}

