<?php

namespace App\Http\Controllers;

use App\Models\Deposit;
use Illuminate\Http\Request;

class DepositController extends Controller
{
    //
    /**
     * Display a listing of deposits.
     */
    public function index()
    {
        return response()->json(Deposit::all(), 200);
    }

    /**
     * Store a newly created deposit.
     */
    public function store(Request $request)
    {
        $request->validate([
            'user_id' => 'required|exists:users,id',
            'amount' => 'required|numeric',
            'payment_method' => 'required|string',
        ]);

        $deposit = Deposit::create($request->all());

        return response()->json($deposit, 201);
    }
}
