import time
import requests
import uuid

from linkedin_api import Linkedin
#
# # Define your LinkedIn session cookies as a dictionary
cookies_dict = {
    "li_at": "AQEFAQ0BAAAAABQnCmsAAAGVJYRkkAAAAZVJkggVVgAAsHVybjpsaTplbnRlcnByaXNlQXV0aFRva2VuOmVKeGpaQUFDbGsyYVRpQ2EyV2ZxUHhETmZXckZGa1lRSTNqcWNTY3dRK1d6eHlRR1JnQzJyUWtiXnVybjpsaTplbnRlcnByaXNlUHJvZmlsZToodXJuOmxpOmVudGVycHJpc2VBY2NvdW50Ojc4Nzg0ODM0LDU1MzUwNzgyKV51cm46bGk6bWVtYmVyOjY1NjkzODk5pQp3pJ5IaDOcpQYKgZc39ggyYeKOFhoPDuqyFSjMjHe3H9NZCpiAGArBI7MgGRwnTYRk0AIVidI7VexZBzPhUgeKAZRGNGBYsW_a3Z186oIGqSkj5y9K6owXxumAdqaSJBv_tgj07HJpkVjkA283rZ_S_OuARRC9jzXTjrGg9YJ8jlQe1yWwJpyCQzu9DjpUvB8uPA",
    "JSESSIONID": "ajax:6603156730395028075"
}

headers = {
    "Csrf-Token": cookies_dict["JSESSIONID"],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json"
}
#
# # Convert cookies to a cookie jar
cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict)
#
# # Authenticate using the converted cookie jar
api = Linkedin("", "", cookies=cookies_jar)
#
print("api", api)
#
# try:
#     my_profile = api.get_profile("me")
#     print(f"✅ Authenticated as: {my_profile['firstName']} {my_profile['lastName']}")
#
#     # Extract your LinkedIn URN ID
#     urn_id = my_profile["entityUrn"].split(":")[-1]
#     print(f"🔗 Your LinkedIn URN ID: {urn_id}\n")
#
# except Exception as e:
#     print(f"❌ Error fetching profile: {e}")
#     exit()

#

# # Step 3: Send Automated Messages to All Connections
# try:
#     print("\n📩 Sending messages...\n")
#
#     message_text = "Hello {name}, I hope you're doing well! Let's connect and collaborate. 🚀"
#
#     for conn in connections[:10]:  # Limit to first 10 for safety
#         recipient_urn = conn["entityUrn"]
#         personalized_message = message_text.format(name=conn["firstName"])
#
#         api.send_message(personalized_message, [recipient_urn])
#
#         print(f"✅ Sent message to {conn['firstName']} {conn['lastName']}")
#
#     print("\n🎉 All messages sent successfully!\n")
#
# except Exception as e:
#     print(f"❌ Error sending messages: {e}")



#
#
# # Direct request to LinkedIn API to fetch connections
# connections_url = "https://www.linkedin.com/voyager/api/relationships/connections"
# response = requests.get(connections_url, headers=headers, cookies=cookies_dict)
#
# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()  # Convert response to JSON
#     connections = data.get("elements", [])  # Extract connections list
#
#     print(f"\n✅ Found {len(connections)} connections!\n")
#
#     # Loop through connections and print details
#     for conn in connections[:5]:  # Limit to first 5
#         miniProfile = conn.get("miniProfile", {})
#         first_name = miniProfile.get("firstName", "Unknown")
#         last_name = miniProfile.get("lastName", "Unknown")
#         entity_urn = miniProfile.get("entityUrn", "Unknown")
#
#         print(f"👤 Name: {first_name} {last_name}")
#         print(f"🔗 URN: {entity_urn}")
#         print("-" * 40)
#
# else:
#     print(f"❌ Failed to fetch connections. Status Code: {response.status_code}")
#     print("Response:", response.text)


#
#
#
#

# ✅ Select a recipient's URN (get this from your connections list)
recipient_urn = "urn:li:fs_miniProfile:ACoAAAAAeFIBPq8DLqta8AkfdmtOE5kGKVLuAzo"  # Replace with actual URN

# ✅ Message text
message_text = "Hello! I Hope you are doing well. 🚀"


# ✅ Replace with your own mailbox URN (your profile URN)
your_mailbox_urn = "urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0"  # Replace with your profile URN

# ✅ Generate unique tracking ID
tracking_id = str(uuid.uuid4())

# ✅ Construct the payload for a new chat
payload = {
    "dedupeByClientGeneratedToken": False,
    "hostRecipientUrns": [recipient_urn],  # Recipient list
    "mailboxUrn": your_mailbox_urn,  # Your LinkedIn profile URN
    "message": {
        "body": {
            "attributes": [],
            "text": message_text
        },
        "originToken": tracking_id,
        "renderContentUnions": []
    },
    "messageRequestContextByRecipient": [
        {
            "contextEntityUrn": "urn:li:fsd_company:15864913",  # Context entity (not mandatory)
            "hostRecipientUrn": recipient_urn
        }
    ],
    "trackingId": tracking_id
}

# ✅ Send request to create a new conversation and send a message
message_url = "https://www.linkedin.com/voyager/api/voyagerMessagingDashMessengerMessages?action=createMessage"
response = requests.post(message_url, headers=headers, cookies=cookies_dict, json=payload)

# ✅ Print response
print("\n📩 LinkedIn API Response:")
print("Status Code:", response.status_code)
print("Response:", response.text)

#
# # # ✅ Send a message using `send_message`
# try:
#     response = api.send_message(message_text, [recipient_urn])
#     time.sleep(uniform(*delay_range))
#     print(f"✅ Message sent successfully to {recipient_urn}")
#     print("🔍 API Response:", response)
# except Exception as e:
#     print(f"❌ Failed to send message. Error: {e}")
#
#

# ✅ Select a recipient's Profile URN (get this from your connections list)
# recipient_urn = "urn:li:fsd_profile:ACoAACzO8mMBrDlrsCU5Bjyyics-RAewrhb8g_s"  # Replace with the correct recipient
#
# # ✅ Construct a conversation URN
# conversation_urn = f"urn:li:msg_conversation:({recipient_urn},2-{int(time.time()*1000)})"
#
# tracking_id = str(uuid.uuid4())
#
# # ✅ Construct payload
# payload = {
#     "dedupeByClientGeneratedToken": False,
#     "mailboxUrn": recipient_urn,
#     "message": {
#         "body": {
#             "attributes": [],
#             "text": message_text
#         },
#         "renderContentUnions": []
#     },
#     "conversationUrn": conversation_urn,
#     "originToken": "ca2d1585-6b45-48d5-8d29-7bedfa717e8a",
#     "quickActionContextUrn": "urn:li:quickReply:NAFBOjbXuNbUcwZnu7asLj-W7SZ5jpByzVr6VRHdYSpwiQ",
#     "trackingId": "Ê-\u0015kEHÕ){íúq~"
# }
#
# # ✅ Send message request
# message_url = "https://www.linkedin.com/voyager/api/voyagerMessagingDashMessengerMessages?action=createMessage"
# response = requests.post(message_url, headers=headers, cookies=cookies_dict, json=payload)
#


#
# payload = {
#     "keyVersion": "LEGACY_INBOX",
#     "conversationCreate": {
#         "eventCreate": {
#             "value": {
#                 "com.linkedin.voyager.messaging.create.MessageCreate": {
#                     "attributedBody": {
#                         "text": message_text,
#                         "attributes": []
#                     },
#                     "attachments": []
#                 }
#             }
#         },
#         "recipients": [recipient_urn],  # List of recipient URNs
#         "subtype": None
#     }
# }
#
# # ✅ Send request to create a new conversation and send a message
# message_url = "https://www.linkedin.com/voyager/api/messaging/conversations"
# response = requests.post(message_url, headers=headers, cookies=cookies_dict, json=payload)
#



# ✅ Print response
print("\n📩 LinkedIn API Response:")
print("Status Code:", response.status_code)
print("Response:", response.text)
