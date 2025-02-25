import time
import requests
import uuid
import json

from linkedin_api import Linkedin
#
# # Define your LinkedIn session cookies as a dictionary
cookies_dict = {
    "li_at": "AQEDAQPqaMsBNE5kAAABlT9ZRvUAAAGVY2XK9VYAvSY97BLQ910WtqIHhWPrF21s5Q17ydGzO7G3bMVVcv9LeJ8KeZah80uUCPBl7UnNSxW6yj8WFqoh8GUY0Vn3Y9zDjtT4eZjnkmEEk3Au1McoR__L",
    "JSESSIONID": "ajax:0864037569280522439"
}

headers = {
    "Csrf-Token": cookies_dict["JSESSIONID"],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
    "X-RestLi-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

# Replace with your mailbox URN (URL-encoded already)
mailbox_urn = "urn%3Ali%3Afsd_profile%3AACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0"

# Set additional variables (modify lastUpdatedBefore value as needed)
variables = (
    "(query:(predicateUnions:List((conversationCategoryPredicate:(category:PRIMARY_INBOX)))),"
    "count:20,"
    "mailboxUrn:" + mailbox_urn + ","
    "lastUpdatedBefore:1740419085505)"
)

# GraphQL endpoint URL
url = (
    "https://www.linkedin.com/voyager/api/voyagerMessagingGraphQL/graphql?"
    "queryId=messengerConversations.8656fb361a8ad0c178e8d3ff1a84ce26&variables=" + variables
)

# Send GET request
response = requests.get(url, headers=headers, cookies=cookies_dict)

# Print formatted response
print("\n🔍 **LinkedIn Conversation Listing (GraphQL) API Response**")
print(f"📡 **Status Code:** {response.status_code}\n")

try:
    response_data = response.json()
    formatted_response = json.dumps(response_data, indent=4, ensure_ascii=False)
    print(f"📄 **Response Data:**\n{formatted_response}")
except json.JSONDecodeError:
    print("❌ Failed to parse JSON. Raw response:")
    print(response.text)
