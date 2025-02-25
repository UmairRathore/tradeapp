import time
import requests
import uuid
import json
from linkedin_api import Linkedin
#
# # Define your LinkedIn session cookies as a dictionary
cookies_dict = {
    "li_at": "AQEDAQPqaMsDxv3UAAABlT8LBNkAAAGVYxeI2VYAcWPxhDIFIwN4b3w_tzM4fqk_t8rk3tDz5xU8HOX6NAeK8wVk7dXz-hdgT6J-ADsuEuQXK8leSxhvZ6IUGJjYFGF1v4RrUr4coUhTwTjsWnyP4KuD",
    "JSESSIONID": "ajax:6603156730395028075"
}

#                                    (o0.0o) when using linkedin-api (o0.0o)
#
# # # Convert cookies to a cookie jar
# cookies_jar = requests.utils.cookiejar_from_dict(cookies_dict)
# #
# # # Authenticate using the converted cookie jar
# api = Linkedin("", "", cookies=cookies_jar)
# #
# print("api", api)
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
# # ✅ Add headers that mimic LinkedIn's requests
# headers = {
#     "Csrf-Token": cookies_dict["JSESSIONID"],
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Accept": "application/json",
#     "X-RestLi-Protocol-Version": "2.0.0",
#     "Content-Type": "application/json"
# }
#
# # ✅ Test Authentication
# profile_url = "https://www.linkedin.com/voyager/api/me"
# response = requests.get(profile_url, headers=headers, cookies=cookies_dict)
#
# # ✅ Format and Print Response
# print("\n🔍 **LinkedIn Direct API Response**")
# print(f"📡 **Status Code:** {response.status_code}\n")
#
# try:
#     response_data = response.json()  # Convert response to JSON
#     formatted_response = json.dumps(response_data, indent=4, ensure_ascii=False)
#     print(f"📄 **Response Data:**\n{formatted_response}")
# except json.JSONDecodeError:
#     print("❌ **Failed to parse JSON. Raw Response:**")
#     print(response.text)



#  {
#     "plainId": 65693899,
#     "miniProfile": {
#       "memorialized": false,
#       "lastName": "Shah",
#       "dashEntityUrn": "urn:li:fsd_profile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#       "standardizedPronoun": "HE_HIM",
#       "occupation": "I help small business owners and entrepreneurs to drive more traffic, leads, and calls with various innovative solutions.",
#       "objectUrn": "urn:li:member:65693899",
#       "backgroundImage": {
#         "com.linkedin.common.VectorImage": {
#           "artifacts": [
#             {
#               "width": 757,
#               "fileIdentifyingUrlPathSegment": "200_800/profile-displaybackgroundimage-shrink_200_800/0/1706135060176?e=1746057600&v=beta&t=9ruaXprx8N4jgRPVwZHVpmjvMJukSc4WZTgrpSjvgPM",
#               "expiresAt": 1746057600000,
#               "height": 189
#             },
#             {
#               "width": 757,
#               "fileIdentifyingUrlPathSegment": "350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1706135060176?e=1746057600&v=beta&t=MIz1Zk2gQlkrmv1ho8ffxTyFeA94OP9k_9PQjoXL30I",
#               "expiresAt": 1746057600000,
#               "height": 189
#             }
#           ],
#           "rootUrl": "https://media.licdn.com/dms/image/v2/D5616AQEHUtaVa99DTQ/profile-displaybackgroundimage-shrink_"
#         }
#       },
#       "picture": {
#         "com.linkedin.common.VectorImage": {
#           "artifacts": [
#             {
#               "width": 100,
#               "fileIdentifyingUrlPathSegment": "100_100/profile-displayphoto-shrink_100_100/0/1607711262454?e=1746057600&v=beta&t=Rbjt5ieproxZZ4EulgTYY1_hQB0uBtRYRUSWCHSFtwc",
#               "expiresAt": 1746057600000,
#               "height": 100
#             },
#             {
#               "width": 200,
#               "fileIdentifyingUrlPathSegment": "200_200/profile-displayphoto-shrink_200_200/0/1607711262454?e=1746057600&v=beta&t=WkHJTCGzRYUZ4B0RvIsimqAf9tYEHGOPtWnO7n8TLMI",
#               "expiresAt": 1746057600000,
#               "height": 200
#             },
#             {
#               "width": 400,
#               "fileIdentifyingUrlPathSegment": "400_400/profile-displayphoto-shrink_400_400/0/1607711262454?e=1746057600&v=beta&t=hXNIA4W7m1HrqrW6rqLRP3JAFuaK4F1steMXq-XLFEE",
#               "expiresAt": 1746057600000,
#               "height": 400
#             },
#             {
#               "width": 480,
#               "fileIdentifyingUrlPathSegment": "800_800/profile-displayphoto-shrink_800_800/0/1607711262454?e=1746057600&v=beta&t=ajEToToTalJYdB5afVJoWJ1wKhJxSLueqfe3MaxNyXs",
#               "expiresAt": 1746057600000,
#               "height": 480
#             }
#           ],
#           "rootUrl": "https://media.licdn.com/dms/image/v2/C5603AQF3iijVKIdKtg/profile-displayphoto-shrink_"
#         }
#       },
#       "firstName": "Vrajesh",
#       "entityUrn": "urn:li:fs_miniProfile:ACoAAAPqaMsBppQ4Do96IW1KXudL-mT6tj3xXZ0",
#       "publicIdentifier": "vrajesh-shah-pmp-pmi-acp",
#       "trackingId": "/I0Dz5x6RmygzgcnlyvlyQ=="
#     },
#     "publicContactInfo": {},
#     "premiumSubscriber": true
#   }
