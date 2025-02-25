<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LinkedinController extends Controller
{
    //

    public function sendMessage(Request $request)
    {
        $username = escapeshellarg($request->username);
        $message = escapeshellarg($request->message);

        $command = escapeshellcmd("python3 linkedin_messaging.py $username $message");
        $output = shell_exec($command);

        return response()->json(["status" => "Message Sent", "output" => $output]);
    }
}
