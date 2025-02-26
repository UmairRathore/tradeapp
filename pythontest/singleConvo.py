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
# Replace with your conversation URN (URL-encoded)
# For example, the conversation URN might be:
# urn:li:msg_conversation:(urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0,2-MzkxNDhkMjQtZDNkMy00NGJmLTg4OWEtOWM0ODViZDkzZTU0XzEwMA==)
# URL-encoded, it becomes:
conversation_urn_encoded = ("urn%3Ali%3Amsg_conversation%3A%28urn%3Ali%3Afsd_profile%3AACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0%2C2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA%3D%3D%29")

# GraphQL endpoint URL for fetching messages for a single conversation
url = (
    "https://www.linkedin.com/voyager/api/voyagerMessagingGraphQL/graphql?"
    "queryId=messengerMessages.0c1bd47e37c67578e99250a711f0c18e&variables="
    f"(conversationUrn:{conversation_urn_encoded})"
)

# Send GET request
response = requests.get(url, headers=headers, cookies=cookies_dict)

# Print formatted response
print("\n🔍 **LinkedIn Single Conversation Messages API Response**")
print(f"📡 **Status Code:** {response.status_code}\n")

try:
    response_data = response.json()
    formatted_response = json.dumps(response_data, indent=4, ensure_ascii=False)
    print(f"📄 **Response Data:**\n{formatted_response}")
except json.JSONDecodeError:
    print("❌ Failed to parse JSON. Raw response:")
    print(response.text)



# {
#     "data": {
#         "_recipeType": "com.linkedin.c38c518a13ae3dfabbd000dba2c1323a",
#         "_type": "com.linkedin.c38c518a13ae3dfabbd000dba2c1323a",
#         "messengerMessagesBySyncToken": {
#             "_type": "com.linkedin.restli.common.CollectionResponse",
#             "metadata": {
#                 "_type": "com.linkedin.messenger.SyncMetadata",
#                 "deletedUrns": [],
#                 "newSyncToken": "kK-K8KJlkuHN-adlLnVybjpsaTpmYWJyaWM6cHJvZC1sb3IxAA==",
#                 "_recipeType": "com.linkedin.511454cd272357b3e0558c5dac215b69",
#                 "shouldClearCache": true
#             },
#             "_recipeType": "com.linkedin.b3fb020d7a62182dcf15004c87ed6684",
#             "elements": [
#                 {
#                     "reactionSummaries": [],
#                     "footer": null,
#                     "subject": null,
#                     "_type": "com.linkedin.messenger.Message",
#                     "inlineWarning": null,
#                     "body": {
#                         "_type": "com.linkedin.pemberly.text.AttributedText",
#                         "attributes": [],
#                         "text": "Hello Pei, I am expanding my network of insurance agents here on LinkedIn where we post lot of value content on online lead generation. Please accept my invite.\n\nThanks Pei\n",
#                         "_recipeType": "com.linkedin.1ea7e24db829a1347b841f2dd496da36"
#                     },
#                     "_recipeType": "com.linkedin.9a4948e0045f59eb49ee971c440d4e31",
#                     "originToken": null,
#                     "backendUrn": "urn:li:messagingMessage:2-MTczOTg0NzY4MDkxN2I2NTkxMy0xMDAmMjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==",
#                     "deliveredAt": 1739847681328,
#                     "renderContentFallbackText": null,
#                     "actor": {
#                         "hostIdentityUrn": "urn:li:fsd_profile:ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                         "preview": null,
#                         "entityUrn": "urn:li:msg_messagingParticipant:urn:li:fsd_profile:ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                         "showPremiumInBug": false,
#                         "memberBadgeType": null,
#                         "showVerificationBadge": true,
#                         "_type": "com.linkedin.messenger.MessagingParticipant",
#                         "participantType": {
#                             "member": {
#                                 "profileUrl": "https://www.linkedin.com/in/ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                                 "firstName": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Pei",
#                                     "_recipeType": "com.linkedin.1ea7e24db829a1347b841f2dd496da36"
#                                 },
#                                 "lastName": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Wu",
#                                     "_recipeType": "com.linkedin.1ea7e24db829a1347b841f2dd496da36"
#                                 },
#                                 "profilePicture": {
#                                     "digitalmediaAsset": null,
#                                     "_type": "com.linkedin.common.VectorImage",
#                                     "attribution": null,
#                                     "_recipeType": "com.linkedin.c029dbe5105f8bef89f4685f7ef3839b",
#                                     "focalPoint": null,
#                                     "artifacts": [
#                                         {
#                                             "width": 100,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "100_100/profile-displayphoto-shrink_100_100/0/1691794841650?e=1746057600&v=beta&t=mta-GGN16sqk5bQXtlfh3WumqXMby25KumAxrB3IFek",
#                                             "height": 100
#                                         },
#                                         {
#                                             "width": 200,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "200_200/profile-displayphoto-shrink_200_200/0/1691794841650?e=1746057600&v=beta&t=j21szdCfXbYBIHGONyib6OEJJRcRzdiv_HbVLeKKAwA",
#                                             "height": 200
#                                         },
#                                         {
#                                             "width": 400,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "400_400/profile-displayphoto-shrink_400_400/0/1691794841650?e=1746057600&v=beta&t=w-Srgbtkk1oLGTYZninDmIjoR9KjaU5SkA2FlhxHhNE",
#                                             "height": 400
#                                         },
#                                         {
#                                             "width": 800,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "800_800/profile-displayphoto-shrink_800_800/0/1691794841650?e=1746057600&v=beta&t=e74X-72eIiN2W9S4vka6F48Ak7PyPloXazN00chHTWU",
#                                             "height": 800
#                                         }
#                                     ],
#                                     "rootUrl": "https://media.licdn.com/dms/image/v2/D4E03AQEa-GNFVJFEzQ/profile-displayphoto-shrink_"
#                                 },
#                                 "distance": "DISTANCE_1",
#                                 "pronoun": {
#                                     "customPronoun": null,
#                                     "standardizedPronoun": "HE_HIM"
#                                 },
#                                 "_type": "com.linkedin.messenger.MemberParticipantInfo",
#                                 "_recipeType": "com.linkedin.a9535f2b6c53c4b69a1dd57697b6de6e",
#                                 "headline": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Certified Physician Assistant and Licensed Financial Professional",
#                                     "_recipeType": "com.linkedin.1ea7e24db829a1347b841f2dd496da36"
#                                 }
#                             },
#                             "custom": null,
#                             "organization": null
#                         },
#                         "_recipeType": "com.linkedin.8e75e1b6100649895f69cf66c6e25b20",
#                         "backendUrn": "urn:li:member:81071019"
#                     },
#                     "entityUrn": "urn:li:msg_message:(urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0,2-MTczOTg0NzY4MDkxN2I2NTkxMy0xMDAmMjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==)",
#                     "sender": {
#                         "hostIdentityUrn": "urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                         "preview": null,
#                         "entityUrn": "urn:li:msg_messagingParticipant:urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                         "showPremiumInBug": true,
#                         "memberBadgeType": null,
#                         "showVerificationBadge": true,
#                         "_type": "com.linkedin.messenger.MessagingParticipant",
#                         "participantType": {
#                             "member": {
#                                 "profileUrl": "https://www.linkedin.com/in/ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                                 "firstName": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Vrajesh",
#                                     "_recipeType": "com.linkedin.1ea7e24db829a1347b841f2dd496da36"
#                                 },
#                                 "lastName": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Shah",
#                                     "_recipeType": "com.linkedin.1ea7e24db829a1347b841f2dd496da36"
#                                 },
#                                 "profilePicture": {
#                                     "digitalmediaAsset": null,
#                                     "_type": "com.linkedin.common.VectorImage",
#                                     "attribution": null,
#                                     "_recipeType": "com.linkedin.c029dbe5105f8bef89f4685f7ef3839b",
#                                     "focalPoint": null,
#                                     "artifacts": [
#                                         {
#                                             "width": 100,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "100_100/profile-displayphoto-shrink_100_100/0/1607711262454?e=1746057600&v=beta&t=Rbjt5ieproxZZ4EulgTYY1_hQB0uBtRYRUSWCHSFtwc",
#                                             "height": 100
#                                         },
#                                         {
#                                             "width": 200,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "200_200/profile-displayphoto-shrink_200_200/0/1607711262454?e=1746057600&v=beta&t=WkHJTCGzRYUZ4B0RvIsimqAf9tYEHGOPtWnO7n8TLMI",
#                                             "height": 200
#                                         },
#                                         {
#                                             "width": 400,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "400_400/profile-displayphoto-shrink_400_400/0/1607711262454?e=1746057600&v=beta&t=hXNIA4W7m1HrqrW6rqLRP3JAFuaK4F1steMXq-XLFEE",
#                                             "height": 400
#                                         },
#                                         {
#                                             "width": 480,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.4e78982efcd19a00e60e23cb18452cb3",
#                                             "fileIdentifyingUrlPathSegment": "800_800/profile-displayphoto-shrink_800_800/0/1607711262454?e=1746057600&v=beta&t=ajEToToTalJYdB5afVJoWJ1wKhJxSLueqfe3MaxNyXs",
#                                             "height": 480
#                                         }
#                                     ],
#                                     "rootUrl": "https://media.licdn.com/dms/image/v2/C5603AQF3iijVKIdKtg/profile-displayphoto-shrink_"
#                                 },
#                                 "distance": "SELF",
#                                 "pronoun": {
#                                     "customPronoun": null,
#                                     "standardizedPronoun": "HE_HIM"
#                                 },
#                                 "_type": "com.linkedin.messenger.MemberParticipantInfo",
#                                 "_recipeType": "com.linkedin.a9535f2b6c53c4b69a1dd57697b6de6e",
#                                 "headline": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "I help small business owners and entrepreneurs to drive more traffic, leads, and calls with various innovative solutions.",
#                                     "_recipeType": "com.linkedin.1ea7e24db829a1347b841f2dd496da36"
#                                 }
#                             },
#                             "custom": null,
#                             "organization": null
#                         },
#                         "_recipeType": "com.linkedin.8e75e1b6100649895f69cf66c6e25b20",
#                         "backendUrn": "urn:li:member:65693899"
#                     },
#                     "backendConversationUrn": "urn:li:messagingThread:2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==",
#                     "incompleteRetriableData": false,
#                     "messageBodyRenderFormat": "DEFAULT",
#                     "renderContent": [],
#                     "conversation": {
#                         "_recipeType": "com.linkedin.45234f48bb281d0b04e9cd2ee2d88237",
#                         "_type": "com.linkedin.messenger.Conversation",
#                         "entityUrn": "urn:li:msg_conversation:(urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0,2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==)"
#                     }
#                 }
#             ]
#         }
#     }
# }
