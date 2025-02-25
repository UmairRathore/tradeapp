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





#
#       {
#                     "notificationStatus": "ACTIVE",
#                     "conversationParticipants": [
#                         {
#                             "hostIdentityUrn": "urn:li:fsd_profile:ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                             "preview": null,
#                             "entityUrn": "urn:li:msg_messagingParticipant:urn:li:fsd_profile:ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                             "showPremiumInBug": false,
#                             "memberBadgeType": null,
#                             "showVerificationBadge": true,
#                             "_type": "com.linkedin.messenger.MessagingParticipant",
#                             "participantType": {
#                                 "member": {
#                                     "profileUrl": "https://www.linkedin.com/in/ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                                     "firstName": {
#                                         "_type": "com.linkedin.pemberly.text.AttributedText",
#                                         "attributes": [],
#                                         "text": "Pei",
#                                         "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                     },
#                                     "lastName": {
#                                         "_type": "com.linkedin.pemberly.text.AttributedText",
#                                         "attributes": [],
#                                         "text": "Wu",
#                                         "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                     },
#                                     "profilePicture": {
#                                         "digitalmediaAsset": null,
#                                         "_type": "com.linkedin.common.VectorImage",
#                                         "attribution": null,
#                                         "_recipeType": "com.linkedin.a9ce6181e85f7839de79e56e19a95e47",
#                                         "focalPoint": null,
#                                         "artifacts": [
#                                             {
#                                                 "width": 100,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "100_100/profile-displayphoto-shrink_100_100/0/1691794841650?e=1746057600&v=beta&t=mta-GGN16sqk5bQXtlfh3WumqXMby25KumAxrB3IFek",
#                                                 "height": 100
#                                             },
#                                             {
#                                                 "width": 200,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "200_200/profile-displayphoto-shrink_200_200/0/1691794841650?e=1746057600&v=beta&t=j21szdCfXbYBIHGONyib6OEJJRcRzdiv_HbVLeKKAwA",
#                                                 "height": 200
#                                             },
#                                             {
#                                                 "width": 400,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "400_400/profile-displayphoto-shrink_400_400/0/1691794841650?e=1746057600&v=beta&t=w-Srgbtkk1oLGTYZninDmIjoR9KjaU5SkA2FlhxHhNE",
#                                                 "height": 400
#                                             },
#                                             {
#                                                 "width": 800,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "800_800/profile-displayphoto-shrink_800_800/0/1691794841650?e=1746057600&v=beta&t=e74X-72eIiN2W9S4vka6F48Ak7PyPloXazN00chHTWU",
#                                                 "height": 800
#                                             }
#                                         ],
#                                         "rootUrl": "https://media.licdn.com/dms/image/v2/D4E03AQEa-GNFVJFEzQ/profile-displayphoto-shrink_"
#                                     },
#                                     "distance": "DISTANCE_1",
#                                     "pronoun": {
#                                         "customPronoun": null,
#                                         "standardizedPronoun": "HE_HIM"
#                                     },
#                                     "_type": "com.linkedin.messenger.MemberParticipantInfo",
#                                     "_recipeType": "com.linkedin.0f82f512c60591c33e895f4d34cb0691",
#                                     "headline": {
#                                         "_type": "com.linkedin.pemberly.text.AttributedText",
#                                         "attributes": [],
#                                         "text": "Certified Physician Assistant and Licensed Financial Professional",
#                                         "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                     }
#                                 },
#                                 "custom": null,
#                                 "organization": null
#                             },
#                             "_recipeType": "com.linkedin.9231cef93fe1acfa5138b36bd4776187",
#                             "backendUrn": "urn:li:member:81071019"
#                         },
#                         {
#                             "hostIdentityUrn": "urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                             "preview": null,
#                             "entityUrn": "urn:li:msg_messagingParticipant:urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                             "showPremiumInBug": true,
#                             "memberBadgeType": null,
#                             "showVerificationBadge": true,
#                             "_type": "com.linkedin.messenger.MessagingParticipant",
#                             "participantType": {
#                                 "member": {
#                                     "profileUrl": "https://www.linkedin.com/in/ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                                     "firstName": {
#                                         "_type": "com.linkedin.pemberly.text.AttributedText",
#                                         "attributes": [],
#                                         "text": "Vrajesh",
#                                         "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                     },
#                                     "lastName": {
#                                         "_type": "com.linkedin.pemberly.text.AttributedText",
#                                         "attributes": [],
#                                         "text": "Shah",
#                                         "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                     },
#                                     "profilePicture": {
#                                         "digitalmediaAsset": null,
#                                         "_type": "com.linkedin.common.VectorImage",
#                                         "attribution": null,
#                                         "_recipeType": "com.linkedin.a9ce6181e85f7839de79e56e19a95e47",
#                                         "focalPoint": null,
#                                         "artifacts": [
#                                             {
#                                                 "width": 100,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "100_100/profile-displayphoto-shrink_100_100/0/1607711262454?e=1746057600&v=beta&t=Rbjt5ieproxZZ4EulgTYY1_hQB0uBtRYRUSWCHSFtwc",
#                                                 "height": 100
#                                             },
#                                             {
#                                                 "width": 200,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "200_200/profile-displayphoto-shrink_200_200/0/1607711262454?e=1746057600&v=beta&t=WkHJTCGzRYUZ4B0RvIsimqAf9tYEHGOPtWnO7n8TLMI",
#                                                 "height": 200
#                                             },
#                                             {
#                                                 "width": 400,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "400_400/profile-displayphoto-shrink_400_400/0/1607711262454?e=1746057600&v=beta&t=hXNIA4W7m1HrqrW6rqLRP3JAFuaK4F1steMXq-XLFEE",
#                                                 "height": 400
#                                             },
#                                             {
#                                                 "width": 480,
#                                                 "_type": "com.linkedin.common.VectorArtifact",
#                                                 "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                 "fileIdentifyingUrlPathSegment": "800_800/profile-displayphoto-shrink_800_800/0/1607711262454?e=1746057600&v=beta&t=ajEToToTalJYdB5afVJoWJ1wKhJxSLueqfe3MaxNyXs",
#                                                 "height": 480
#                                             }
#                                         ],
#                                         "rootUrl": "https://media.licdn.com/dms/image/v2/C5603AQF3iijVKIdKtg/profile-displayphoto-shrink_"
#                                     },
#                                     "distance": "SELF",
#                                     "pronoun": {
#                                         "customPronoun": null,
#                                         "standardizedPronoun": "HE_HIM"
#                                     },
#                                     "_type": "com.linkedin.messenger.MemberParticipantInfo",
#                                     "_recipeType": "com.linkedin.0f82f512c60591c33e895f4d34cb0691",
#                                     "headline": {
#                                         "_type": "com.linkedin.pemberly.text.AttributedText",
#                                         "attributes": [],
#                                         "text": "I help small business owners and entrepreneurs to drive more traffic, leads, and calls with various innovative solutions.",
#                                         "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                     }
#                                 },
#                                 "custom": null,
#                                 "organization": null
#                             },
#                             "_recipeType": "com.linkedin.9231cef93fe1acfa5138b36bd4776187",
#                             "backendUrn": "urn:li:member:65693899"
#                         }
#                     ],
#                     "unreadCount": 0,
#                     "conversationVerificationLabel": null,
#                     "lastActivityAt": 1739847681338,
#                     "descriptionText": null,
#                     "draftMessages": {
#                         "_type": "com.linkedin.restli.common.CollectionResponse",
#                         "_recipeType": "com.linkedin.cdf141a90f1f2e361397eb5d73916900",
#                         "elements": []
#                     },
#                     "conversationVerificationExplanation": null,
#                     "title": null,
#                     "backendUrn": "urn:li:messagingThread:2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==",
#                     "shortHeadlineText": null,
#                     "createdAt": 1739847680886,
#                     "lastReadAt": 1739911971153,
#                     "hostConversationActions": [],
#                     "entityUrn": "urn:li:msg_conversation:(urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0,2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==)",
#                     "categories": [
#                         "INBOX",
#                         "PRIMARY_INBOX"
#                     ],
#                     "state": null,
#                     "disabledFeatures": [
#                         {
#                             "_type": "com.linkedin.messenger.ConversationDisabledFeature",
#                             "disabledFeature": "UPDATE_MESSAGE_REQUEST_STATE",
#                             "reasonText": null,
#                             "_recipeType": "com.linkedin.64dbf3b345571aa29bbd9f04564f200f"
#                         },
#                         {
#                             "_type": "com.linkedin.messenger.ConversationDisabledFeature",
#                             "disabledFeature": "ADD_PARTICIPANT",
#                             "reasonText": null,
#                             "_recipeType": "com.linkedin.64dbf3b345571aa29bbd9f04564f200f"
#                         },
#                         {
#                             "_type": "com.linkedin.messenger.ConversationDisabledFeature",
#                             "disabledFeature": "RENAMED_CONVERSATION",
#                             "reasonText": null,
#                             "_recipeType": "com.linkedin.64dbf3b345571aa29bbd9f04564f200f"
#                         },
#                         {
#                             "_type": "com.linkedin.messenger.ConversationDisabledFeature",
#                             "disabledFeature": "REMOVE_PARTICIPANT",
#                             "reasonText": null,
#                             "_recipeType": "com.linkedin.64dbf3b345571aa29bbd9f04564f200f"
#                         },
#                         {
#                             "_type": "com.linkedin.messenger.ConversationDisabledFeature",
#                             "disabledFeature": "CREATE_GROUP_CHAT_LINK",
#                             "reasonText": null,
#                             "_recipeType": "com.linkedin.64dbf3b345571aa29bbd9f04564f200f"
#                         }
#                     ],
#                     "creator": {
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
#                                     "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                 },
#                                 "lastName": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Wu",
#                                     "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                 },
#                                 "profilePicture": {
#                                     "digitalmediaAsset": null,
#                                     "_type": "com.linkedin.common.VectorImage",
#                                     "attribution": null,
#                                     "_recipeType": "com.linkedin.a9ce6181e85f7839de79e56e19a95e47",
#                                     "focalPoint": null,
#                                     "artifacts": [
#                                         {
#                                             "width": 100,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                             "fileIdentifyingUrlPathSegment": "100_100/profile-displayphoto-shrink_100_100/0/1691794841650?e=1746057600&v=beta&t=mta-GGN16sqk5bQXtlfh3WumqXMby25KumAxrB3IFek",
#                                             "height": 100
#                                         },
#                                         {
#                                             "width": 200,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                             "fileIdentifyingUrlPathSegment": "200_200/profile-displayphoto-shrink_200_200/0/1691794841650?e=1746057600&v=beta&t=j21szdCfXbYBIHGONyib6OEJJRcRzdiv_HbVLeKKAwA",
#                                             "height": 200
#                                         },
#                                         {
#                                             "width": 400,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                             "fileIdentifyingUrlPathSegment": "400_400/profile-displayphoto-shrink_400_400/0/1691794841650?e=1746057600&v=beta&t=w-Srgbtkk1oLGTYZninDmIjoR9KjaU5SkA2FlhxHhNE",
#                                             "height": 400
#                                         },
#                                         {
#                                             "width": 800,
#                                             "_type": "com.linkedin.common.VectorArtifact",
#                                             "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
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
#                                 "_recipeType": "com.linkedin.0f82f512c60591c33e895f4d34cb0691",
#                                 "headline": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Certified Physician Assistant and Licensed Financial Professional",
#                                     "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                 }
#                             },
#                             "custom": null,
#                             "organization": null
#                         },
#                         "_recipeType": "com.linkedin.9231cef93fe1acfa5138b36bd4776187",
#                         "backendUrn": "urn:li:member:81071019"
#                     },
#                     "read": true,
#                     "groupChat": false,
#                     "_type": "com.linkedin.messenger.Conversation",
#                     "contentMetadata": null,
#                     "_recipeType": "com.linkedin.b4bed56e563978b05b51089315cd59e6",
#                     "conversationUrl": "https://www.linkedin.com/messaging/thread/2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==/",
#                     "headlineText": null,
#                     "incompleteRetriableData": false,
#                     "messages": {
#                         "_type": "com.linkedin.restli.common.CollectionResponse",
#                         "_recipeType": "com.linkedin.25534c62459517a82315b362fee601e2",
#                         "elements": [
#                             {
#                                 "reactionSummaries": [],
#                                 "footer": null,
#                                 "subject": null,
#                                 "_type": "com.linkedin.messenger.Message",
#                                 "inlineWarning": null,
#                                 "body": {
#                                     "_type": "com.linkedin.pemberly.text.AttributedText",
#                                     "attributes": [],
#                                     "text": "Hello Pei, I am expanding my network of insurance agents here on LinkedIn where we post lot of value content on online lead generation. Please accept my invite.\n\nThanks Pei\n",
#                                     "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                 },
#                                 "_recipeType": "com.linkedin.5dd58cbb658023cdbe1cf38af950499c",
#                                 "originToken": null,
#                                 "backendUrn": "urn:li:messagingMessage:2-MTczOTg0NzY4MDkxN2I2NTkxMy0xMDAmMjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==",
#                                 "deliveredAt": 1739847681328,
#                                 "renderContentFallbackText": null,
#                                 "actor": {
#                                     "hostIdentityUrn": "urn:li:fsd_profile:ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                                     "preview": null,
#                                     "entityUrn": "urn:li:msg_messagingParticipant:urn:li:fsd_profile:ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                                     "showPremiumInBug": false,
#                                     "memberBadgeType": null,
#                                     "showVerificationBadge": true,
#                                     "_type": "com.linkedin.messenger.MessagingParticipant",
#                                     "participantType": {
#                                         "member": {
#                                             "profileUrl": "https://www.linkedin.com/in/ACoAAATVC6sBb5ZltIhxZl0QybFnZTUK6i7Vc5Q",
#                                             "firstName": {
#                                                 "_type": "com.linkedin.pemberly.text.AttributedText",
#                                                 "attributes": [],
#                                                 "text": "Pei",
#                                                 "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                             },
#                                             "lastName": {
#                                                 "_type": "com.linkedin.pemberly.text.AttributedText",
#                                                 "attributes": [],
#                                                 "text": "Wu",
#                                                 "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                             },
#                                             "profilePicture": {
#                                                 "digitalmediaAsset": null,
#                                                 "_type": "com.linkedin.common.VectorImage",
#                                                 "attribution": null,
#                                                 "_recipeType": "com.linkedin.a9ce6181e85f7839de79e56e19a95e47",
#                                                 "focalPoint": null,
#                                                 "artifacts": [
#                                                     {
#                                                         "width": 100,
#                                                         "_type": "com.linkedin.common.VectorArtifact",
#                                                         "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                         "fileIdentifyingUrlPathSegment": "100_100/profile-displayphoto-shrink_100_100/0/1691794841650?e=1746057600&v=beta&t=mta-GGN16sqk5bQXtlfh3WumqXMby25KumAxrB3IFek",
#                                                         "height": 100
#                                                     },
#                                                     {
#                                                         "width": 200,
#                                                         "_type": "com.linkedin.common.VectorArtifact",
#                                                         "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                         "fileIdentifyingUrlPathSegment": "200_200/profile-displayphoto-shrink_200_200/0/1691794841650?e=1746057600&v=beta&t=j21szdCfXbYBIHGONyib6OEJJRcRzdiv_HbVLeKKAwA",
#                                                         "height": 200
#                                                     },
#                                                     {
#                                                         "width": 400,
#                                                         "_type": "com.linkedin.common.VectorArtifact",
#                                                         "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                         "fileIdentifyingUrlPathSegment": "400_400/profile-displayphoto-shrink_400_400/0/1691794841650?e=1746057600&v=beta&t=w-Srgbtkk1oLGTYZninDmIjoR9KjaU5SkA2FlhxHhNE",
#                                                         "height": 400
#                                                     },
#                                                     {
#                                                         "width": 800,
#                                                         "_type": "com.linkedin.common.VectorArtifact",
#                                                         "_recipeType": "com.linkedin.b671f4dfc10869c465eb094fd22df34b",
#                                                         "fileIdentifyingUrlPathSegment": "800_800/profile-displayphoto-shrink_800_800/0/1691794841650?e=1746057600&v=beta&t=e74X-72eIiN2W9S4vka6F48Ak7PyPloXazN00chHTWU",
#                                                         "height": 800
#                                                     }
#                                                 ],
#                                                 "rootUrl": "https://media.licdn.com/dms/image/v2/D4E03AQEa-GNFVJFEzQ/profile-displayphoto-shrink_"
#                                             },
#                                             "distance": "DISTANCE_1",
#                                             "pronoun": {
#                                                 "customPronoun": null,
#                                                 "standardizedPronoun": "HE_HIM"
#                                             },
#                                             "_type": "com.linkedin.messenger.MemberParticipantInfo",
#                                             "_recipeType": "com.linkedin.0f82f512c60591c33e895f4d34cb0691",
#                                             "headline": {
#                                                 "_type": "com.linkedin.pemberly.text.AttributedText",
#                                                 "attributes": [],
#                                                 "text": "Certified Physician Assistant and Licensed Financial Professional",
#                                                 "_recipeType": "com.linkedin.f63b4788f6578b8c233494ad21afe660"
#                                             }
#                                         },
#                                         "custom": null,
#                                         "organization": null
#                                     },
#                                     "_recipeType": "com.linkedin.9231cef93fe1acfa5138b36bd4776187",
#                                     "backendUrn": "urn:li:member:81071019"
#                                 },
#                                 "entityUrn": "urn:li:msg_message:(urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0,2-MTczOTg0NzY4MDkxN2I2NTkxMy0xMDAmMjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==)",
#                                 "sender": {
#                                     "hostIdentityUrn": "urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                                     "entityUrn": "urn:li:msg_messagingParticipant:urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#                                     "showPremiumInBug": true,
#                                     "memberBadgeType": null,
#                                     "showVerificationBadge": true,
#                                     "_type": "com.linkedin.messenger.MessagingParticipant",
#                                     "_recipeType": "com.linkedin.9231cef93fe1acfa5138b36bd4776187"
#                                 },
#                                 "backendConversationUrn": "urn:li:messagingThread:2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==",
#                                 "incompleteRetriableData": false,
#                                 "messageBodyRenderFormat": "DEFAULT",
#                                 "renderContent": [],
#                                 "conversation": {
#                                     "_recipeType": "com.linkedin.b4bed56e563978b05b51089315cd59e6",
#                                     "_type": "com.linkedin.messenger.Conversation",
#                                     "entityUrn": "urn:li:msg_conversation:(urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0,2-MjIyYzk4ODctZDIxYy00MzFkLWFiYTktMzVkOWNlZTlhMjJlXzEwMA==)"
#                                 }
#                             }
#                         ]
#                     },
#                     "conversationTypeText": null
#                 },
#
