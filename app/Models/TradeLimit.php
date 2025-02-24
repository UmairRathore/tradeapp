<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TradeLimit extends Model
{
    //
    use HasFactory;

    protected $table = 'trade_limits';

    protected $fillable = [
        'match_id', 'min_trade_amount', 'max_trade_amount', 'roi_percentage'
    ];

    public function match()
    {
        return $this->belongsTo(MatchSchedule::class);
    }
}
