<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Cashout extends Model
{
    use HasFactory;

    protected $table = 'cashout_requests';

    protected $fillable = [
        'user_id', 'bank_detail_id', 'amount', 'status',
        'requested_at', 'processed_at', 'rejection_reason'
    ];

    protected $casts = [
        'amount' => 'decimal:2',
        'requested_at' => 'datetime',
        'processed_at' => 'datetime',
    ];

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function bankDetail(): BelongsTo
    {
        return $this->belongsTo(BankDetail::class);
    }
}
