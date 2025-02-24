<?php

namespace App\Http\Controllers;

use App\Models\Withdrawal;
use Illuminate\Http\Request;

class WithdrawalController extends Controller
{
    //
    /**
     * Display a listing of withdrawals.
     */
    public function index()
    {
        return response()->json(Withdrawal::all(), 200);
    }

    /**
     * Store a newly created withdrawal.
     */
    public function store(Request $request)
    {
        $request->validate([
            'user_id' => 'required|exists:users,id',
            'amount' => 'required|numeric',
            'payment_method' => 'required|string',
        ]);

        $withdrawal = Withdrawal::create($request->all());

        return response()->json($withdrawal, 201);
    }
}
