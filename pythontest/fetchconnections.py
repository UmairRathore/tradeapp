import time
import requests
import uuid
import json

from linkedin_api import Linkedin
#
# # Define your LinkedIn session cookies as a dictionary
cookies_dict = {
    "li_at": "AQEDAQPqaMsBaQylAAABlT8-IEkAAAGVY0qkSU0ABGBI_HSNak66k1YgrEW2AUn26pCGXescpj62VmYV8-zMzR9w0dWGv0zKn0QZIowJVUJVXKLB3ZCu5w95K6J0LWUnCe7LxFnxrDQyJfB-z2niEthc",
    "JSESSIONID": "ajax:0864037569280522439"
}

# # Convert cookies to a cookie jar
cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict)
#
# # Authenticate using the converted cookie jar
api = Linkedin("", "", cookies=cookies_jar)

print("\n✅ **Authenticated Successfully!**\n")

# ✅ Fetch chat conversations
try:
    conversations = api.get_conversations()

    if conversations:
        print(f"\n✅ **Found {len(conversations)} chat conversations!**\n")

        for convo in conversations[:10]:  # Limit to first 10
            conversation_id = convo.get("entityUrn", "Unknown").split(":")[-1]
            participants = convo.get("participants", [])
            message_snippet = convo.get("lastActivityAt", "No messages")

            participant_names = []
            for participant in participants:
                name = participant.get("miniProfile", {}).get("firstName", "Unknown") + " " + \
                       participant.get("miniProfile", {}).get("lastName", "Unknown")
                participant_names.append(name)

            print(f"📩 **Conversation ID:** {conversation_id}")
            print(f"👥 **Participants:** {', '.join(participant_names)}")
            print(f"📝 **Last Message Activity:** {message_snippet}")
            print("-" * 40)

    else:
        print("⚠️ No conversations found.")

except Exception as e:
    print(f"❌ **Error fetching conversations:** {e}")
