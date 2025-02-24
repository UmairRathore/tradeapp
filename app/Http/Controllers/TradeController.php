<?php

namespace App\Http\Controllers;

use App\Models\Trade;
use Illuminate\Http\Request;

class TradeController extends Controller
{
    //
    /**
     * Display a listing of trades.
     */
    public function index()
    {
        return response()->json(Trade::all(), 200);
    }

    /**
     * Store a newly created trade.
     */
    public function store(Request $request)
    {
        $request->validate([
            'user_id' => 'required|exists:users,id',
            'match_name' => 'required|string',
            'amount' => 'required|numeric',
            'roi' => 'required|numeric',
            'trade_type' => 'required|in:score,runs',
            'trade_status' => 'required|in:running,completed,cancelled',
        ]);

        $trade = Trade::create($request->all());

        return response()->json($trade, 201);
    }

    /**
     * Display the specified trade.
     */
    public function show(Trade $trade)
    {
        return response()->json($trade, 200);
    }

    /**
     * Update the specified trade.
     */
    public function update(Request $request, Trade $trade)
    {
        $trade->update($request->all());

        return response()->json($trade, 200);
    }

    /**
     * Remove the specified trade.
     */
    public function destroy(Trade $trade)
    {
        $trade->delete();

        return response()->json(['message' => 'Trade deleted'], 200);
    }
}
