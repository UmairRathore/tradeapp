<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class TradeHistory extends Model
{
    use HasFactory;

    protected $table = 'trade_history';

    protected $fillable = [
        'user_id', 'trade_id', 'amount', 'roi', 'total_earnings',
        'trade_status', 'winning_status', 'trade_start_time', 'trade_end_time'
    ];

    protected $casts = [
        'amount' => 'decimal:2',
        'roi' => 'decimal:2',
        'total_earnings' => 'decimal:2',
        'trade_start_time' => 'datetime',
        'trade_end_time' => 'datetime',
    ];

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function trade(): BelongsTo
    {
        return $this->belongsTo(Trade::class);
    }
}
