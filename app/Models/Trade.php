<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Trade extends Model
{
    use HasFactory;

    protected $table = 'trades';

    protected $fillable = [
        'user_id', 'match_name', 'amount', 'roi', 'trade_type',
        'trade_status', 'winning_status', 'trade_start_time', 'trade_end_time'
    ];

    protected $casts = [
        'amount' => 'decimal:2',
        'roi' => 'decimal:2',
        'trade_start_time' => 'datetime',
        'trade_end_time' => 'datetime',
        'trade_status' => 'string',
        'winning_status' => 'string',
    ];

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}
