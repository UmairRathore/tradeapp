<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;

use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Session;
use Twilio\Rest\Client;
use Twilio\TwiML\MessagingResponse;
use OpenAI\Laravel\Facades\OpenAI;

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




Route::post('/whatsapp-webhook', function (Request $request) {
    Log::info('Incoming WhatsApp Message:', $request->all());

    $from = $request->input('From');  // Sender's phone number
    $body = trim(strtolower($request->input('Body')));  // Normalize input

//    // Step 1: Full-Text Search (Best for Large Data)
//    $storedAnswer = DB::table('faq')
//        ->whereRaw("MATCH(question) AGAINST (? IN NATURAL LANGUAGE MODE)", [$body])
//        ->value('answer');
//
//    if (!$storedAnswer) {
//        // Step 2: Levenshtein Distance (Best for Typos & Rewording)
//        $questions = DB::table('faq')->get();
//        $bestMatch = null;
//        $lowestDistance = PHP_INT_MAX;
//
//        foreach ($questions as $q) {
//            $distance = levenshtein($body, strtolower($q->question));
//
//            if ($distance < $lowestDistance) {
//                $lowestDistance = $distance;
//                $bestMatch = $q->answer;
//            }
//        }
//
//        if ($lowestDistance <= 5) { // Allow small typo differences
//            $storedAnswer = $bestMatch;
//        }
//    }
//
//    if (!$storedAnswer) {
//        // Step 3: Soundex Matching (Best for Phonetic Similarities)
//        $storedAnswer = DB::table('faq')
//            ->whereRaw("SOUNDEX(question) = SOUNDEX(?)", [$body])
//            ->value('answer');
//    }
//
//    if (!$storedAnswer) {
//         Step 4: Query ChatGPT for an Answer
    $storedAnswer = 'check out this stored answer';
    try {
        $response = OpenAI::chat()->create([
            'model' => 'gpt-4o',
            'messages' => [
                ['role' => 'system', 'content' => 'You are a helpful AI assistant.'],
                ['role' => 'user', 'content' => $body]
            ],
        ]);

        // ✅ Properly access OpenAI response
        $storedAnswer = $response->choices[0]->message->content ?? "Sorry, I couldn't generate a response.";
    } catch (\Exception $e) {
        Log::error('ChatGPT API Error:', ['error' => $e->getMessage()]);
        $storedAnswer = "I'm having trouble understanding. Please try again later.";
    }
//    }

//    if (!$storedAnswer) {
//        // Step 5: Store Unanswered Question for Admin Review
//        DB::table('unanswered_questions')->insert([
//            'question' => $body,
//            'contact' => $from,
//            'created_at' => now()
//        ]);
//
//        $storedAnswer = "I'm not sure about that. Our team will review and get back to you. Please provide your contact details.";
//    } else {
//        // Step 6: Store ChatGPT Response in FAQ to Reduce API Calls
//        DB::table('faq')->insert([
//            'question' => $body,
//            'answer' => $storedAnswer,
//            'created_at' => now(),
//            'updated_at' => now(),
//        ]);
//    }
//dd($storedAnswer);
    // Respond with the best available answer
    $twiml = new MessagingResponse();
    $twiml->message($storedAnswer);

    // Convert to XML and log it
    $xmlResponse = $twiml->__toString();
    Log::info('Generated TwiML Response:', ['xml' => $xmlResponse]);

    return response($xmlResponse, 200)->header('Content-Type', 'application/xml');
});


Route::post('/send-whatsapp', function (Request $request) {
    $sid = env('TWILIO_SID');
    $token = env('TWILIO_AUTH_TOKEN');
    $twilioNumber = 'whatsapp:+14155238886';

//    $to = 'whatsapp:' . $request->input('to'); // Recipient number
    $to = 'whatsapp:' . "+923154462426"; // Recipient number
//    whatsapp:+1234567890
    $message = $request->input('message');  // Message content

//    if (!$message) {
//        return response()->json(['error' => 'Message content is required'], 400);
//    }

//            'body' => $message
    try {
        $client = new Client($sid, $token);
        $client->messages->create($to, [
            'from' => $twilioNumber,
            'body' => "check here this is the message we have for the testing"
        ]);

        return response()->json(['status' => 'Message sent!']);
    } catch (\Exception $e) {
        return response()->json(['error' => $e->getMessage()], 500);
    }
});









//...................FAQ MIGRATION............//


//use Illuminate\Database\Migrations\Migration;
//use Illuminate\Database\Schema\Blueprint;
//use Illuminate\Support\Facades\Schema;
//
//return new class extends Migration {
//    public function up() {
//        Schema::create('faq', function (Blueprint $table) {
//            $table->id();
//            $table->string('question');
//            $table->text('answer');
//            $table->timestamps();
//            $table->fullText('question'); // Enable full-text search
//        });
//    }
//
//    public function down() {
//        Schema::dropIfExists('faq');
//    }
//};


///
///
/// use Illuminate\Http\Request;
//use App\Models\Faq;
//use App\Models\UnansweredQuestion;
//
//class AdminController extends Controller {
//    public function unanswered() {
//        $questions = UnansweredQuestion::all();
//        return view('admin.unanswered', compact('questions'));
//    }
//
//    public function storeAnswer(Request $request) {
//        $request->validate([
//            'question_id' => 'required|exists:unanswered_questions,id',
//            'answer' => 'required'
//        ]);
//
//        $question = UnansweredQuestion::find($request->question_id);
//
//        // Save to FAQ
//        Faq::create([
//            'question' => $question->question,
//            'answer' => $request->answer
//        ]);
//
//        // Remove from unanswered
//        $question->delete();
//
//        return redirect()->back()->with('success', 'Answer saved!');
//    }
//}


////....................BLADE VIEW FOR ADMIN.................
//<h2>Unanswered Questions</h2>
//@foreach($questions as $question)
//    <p><strong>Question:</strong> {{ $question->question }}</p>
//    <form action="{{ route('admin.storeAnswer') }}" method="POST">
//    @csrf
//        <input type="hidden" name="question_id" value="{{ $question->id }}">
//        <textarea name="answer" required></textarea>
//        <button type="submit">Save Answer</button>
//    </form>
//@endforeach


//ROUTES

//Route::get('/admin/unanswered', [AdminController::class, 'unanswered'])->name('admin.unanswered');
//Route::post('/admin/answer', [AdminController::class, 'storeAnswer'])->name('admin.storeAnswer');



Route::post('/sync-account', function (Request $request) {
    // Set DSN and API access token (ideally, these values should be in your config or .env)
    $dsn = 'https://api10.unipile.com:14047';
    $accessToken = '7QX2gen5./CXPi+xq2RuTKjWy2tqNPNZlwDb2K63xNDf78ocK+bg=';

    // Prepare the payload for authentication using cookies
    $payload = [
        'provider'    => 'LINKEDIN',
        'access_token'=> 'AQEFAQ0BAAAAABQnCmsAAAGVJYRkkAAAAZVJkggVVgAAsHVybjpsaTplbnRlcnByaXNlQXV0aFRva2VuOmVKeGpaQUFDbGsyYVRpQ2EyV2ZxUHhETmZXckZGa1lRSTNqcWNTY3dRK1d6eHlRR1JnQzJyUWtiXnVybjpsaTplbnRlcnByaXNlUHJvZmlsZToodXJuOmxpOmVudGVycHJpc2VBY2NvdW50Ojc4Nzg0ODM0LDU1MzUwNzgyKV51cm46bGk6bWVtYmVyOjY1NjkzODk5pQp3pJ5IaDOcpQYKgZc39ggyYeKOFhoPDuqyFSjMjHe3H9NZCpiAGArBI7MgGRwnTYRk0AIVidI7VexZBzPhUgeKAZRGNGBYsW_a3Z186oIGqSkj5y9K6owXxumAdqaSJBv_tgj07HJpkVjkA283rZ_S_OuARRC9jzXTjrGg9YJ8jlQe1yWwJpyCQzu9DjpUvB8uPA',
        'cookie_li_a' => 'AQJ2PTEmc2FsZXNfY2lkPTE5NzgzMDgzNiUzQSUzQTE5Nzc3NTkzMiUzQSUzQXRpZXIxJTNBJTNBNzg3ODQ4MzQwxlDT6Ge7SFnjy_Z7qOeABio-wQ',
        'user_agent'  => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    ];

//    dd($payload);
    // Log the payload for debugging purposes (avoid logging sensitive tokens in production)
    Log::info('Sync account payload:', $payload);

    // Call Unipile's account connection endpoint
    $response = Http::withHeaders([
        'X-API-KEY' => $accessToken,
        'Accept'    => 'application/json',
    ])->post("{$dsn}/api/v1/accounts", $payload);
dd($response->body());
    // Decode the response JSON into an array
    $data = $response->json();

    // Log the response for debugging purposes
    Log::info('Unipile account sync response:', $data);

    // Dump and die the response for debugging
    dd($data);

    // The following code won't be reached due to dd(), but here's how you'd return a JSON response:
    /*
    if ($response->successful() && isset($data['account_id'])) {
        return response()->json([
            'message'    => 'LinkedIn account synced successfully.',
            'account_id' => $data['account_id'],
        ]);
    }

    return response()->json([
        'error'   => 'Unable to sync LinkedIn account.',
        'details' => $data,
    ], $response->status());
    */
});


Route::get('/get-connections', function () {
    // Retrieve the stored account_id
    $accountId = Session::get('linkedin_account_id', 'R52oyaW-SVmrRATUJ0b5wg'); // using your account_id as default

    $dsn = 'https://api10.unipile.com:14047';
    $accessToken = '7QX2gen5./CXPi+xq2RuTKjWy2tqNPNZlwDb2K63xNDf78ocK+bg=';

    // Assuming the correct endpoint is /api/v1/accounts/{account_id}/connections
    $response = Http::withHeaders([
        'X-API-KEY' => $accessToken,
        'Accept'    => 'application/json',
    ])->get("{$dsn}/api/v1/chats");

    $data = $response->json();
dd($data);
    return response()->json([
        'message'     => 'Connections retrieved successfully.',
        'connections' => $data,
    ]);
});




Route::get('/chats-with-names', function () {
    // Set DSN and access token (ideally, these values should come from your .env file)
    $dsn = 'https://api10.unipile.com:14047';
    $accessToken = '7QX2gen5./CXPi+xq2RuTKjWy2tqNPNZlwDb2K63xNDf78ocK+bg=';

    $provider_id = '2-MzkxNDhkMjQtZDNkMy00NGJmLTg4OWEtOWM0ODViZDkzZTU0XzEwMA==';

    $attendeeId =  'attendee_provider_id= ACoAAE3MrVQBgMZuZoH8F37oUjYsW_3cPbmJ2Pg"';
    // Retrieve the chat list
    $response = Http::withHeaders([
        'X-API-KEY' => $accessToken,
        'Accept'    => 'application/json',
    ])->get("{$dsn}/api/v1/users/$attendeeId");

    dd($response->body());
//    $chatList = $response->json();
//
//    if (!isset($chatList['items'])) {
//        return response()->json(['error' => 'No chat items found'], 404);
//    }
//
//    $chatsWithNames = [];


    $response = $client->request('GET', 'https://api1.unipile.com:13111/api/v1/users/identifier', [
        'headers' => [
            'accept' => 'application/json',
        ],
    ]);

    echo $response->getBody();
    // Loop through each chat item
    foreach ($chatList['items'] as $chat) {
        // By default, the "name" may be null; try to fetch profile info based on the attendee_provider_id
        $attendeeId = $chat['attendee_provider_id'] ?? null;
        if ($attendeeId) {
            // Fetch user profile using the attendee_provider_id
            // NOTE: Adjust the endpoint if your provider uses a different path
            $userResponse = Http::withHeaders([
                'X-API-KEY' => $accessToken,
                'Accept'    => 'application/json',
            ])->get("{$dsn}/api/v1/users/{$attendeeId}");

            dd($userResponse);
            $userProfile = $userResponse->json();

            // Assuming the profile returns a "full_name" field
            if (isset($userProfile['full_name'])) {
                $chat['name'] = $userProfile['full_name'];
            } else {
                $chat['name'] = 'Unknown';
            }
        } else {
            $chat['name'] = 'Unknown';
        }

        $chatsWithNames[] = $chat;
    }

    return response()->json([
        'object' => $chatList['object'],
        'items'  => $chatsWithNames,
    ]);
});
