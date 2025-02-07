<?php

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\UserController;



Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');
// User Routes
Route::get('users', [UserController::class, 'index']);
Route::post('users/create', [UserController::class, 'store']);
Route::get('users/{user}', [UserController::class, 'show']);
Route::put('users/update/{user}', [UserController::class, 'update']);
Route::delete('users/delete/{user}', [UserController::class, 'destroy']);
