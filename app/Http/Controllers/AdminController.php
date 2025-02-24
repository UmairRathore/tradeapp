<?php

namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class AdminController extends Controller
{
    //
    /**
     * Display user statistics.
     */
    public function dashboard()
    {
        return response()->json([
            'total_users' => User::count(),
            'total_deposits' => \App\Models\Deposit::sum('amount'),
            'total_withdrawals' => \App\Models\Withdrawal::sum('amount'),
        ], 200);
    }

    /**
     * Approve a user.
     */
    public function approveUser(User $user)
    {
        $user->update(['status' => 'active']);

        return response()->json(['message' => 'User approved'], 200);
    }

    /**
     * Reject a user.
     */
    public function rejectUser(User $user)
    {
        $user->update(['status' => 'rejected']);

        return response()->json(['message' => 'User rejected'], 200);
    }
}
