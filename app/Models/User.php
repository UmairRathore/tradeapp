<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class User extends Authenticatable
{
    use HasFactory;

    protected $table = 'users';

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'name', 'username', 'email', 'password', 'referral_code',
        'referred_by', 'total_wealth', 'available_balance', 'on_trade_balance',
        'status', 'role'
    ];

    /**
     * The attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected $casts = [
        'total_wealth' => 'decimal:2',
        'available_balance' => 'decimal:2',
        'on_trade_balance' => 'decimal:2',
        'status' => 'string',
        'role' => 'string',
    ];

    public function trades(): HasMany
    {
        return $this->hasMany(Trade::class);
    }

    public function referrals(): HasMany
    {
        return $this->hasMany(Referral::class, 'referrer_id');
    }

    public function deposits(): HasMany
    {
        return $this->hasMany(Deposit::class);
    }

    public function withdrawals(): HasMany
    {
        return $this->hasMany(Withdrawal::class);
    }

    public function bankDetails(): HasMany
    {
        return $this->hasMany(BankDetail::class);
    }
}
