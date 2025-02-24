<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class CapitalReserve extends Model
{
    //
    use HasFactory;

    protected $table = 'capital_reserves';

    protected $fillable = [
        'match_id', 'reserve_percentage', 'total_reserved_amount'
    ];

    public function match()
    {
        return $this->belongsTo(MatchSchedule::class);
    }
}
