# import requests
# import json

# base_url = "https://itunes.apple.com/search"
# params = {
#     "term" : "black keys",
#     "entity" : "musicTrack"
# }

# response = requests.get(base_url, params)
# result = response.json()

# print(result)

################################################

# import json

# sample_json = r'''
# {
#   "created_at": "Thu Apr 06 15:24:15 +0000 2017",
#   "id_str": "850006245121695744",
#   "text": "1\/ Today we are sharing our vision for the future of the Twitter API platform!\nhttps:\/\/t.co\/XweGngmxlP",
#   "user": {
#     "id": 2244994945,
#     "name": "Twitter Dev",
#     "screen_name": "TwitterDev",
#     "location": "Internet",
#     "url": "https:\/\/dev.twitter.com\/",
#     "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"
#   },
#   "place": {   
#   },
#   "entities": {
#     "hashtags": [      
#     ],
#     "urls": [
#       {
#         "url": "https:\/\/t.co\/XweGngmxlP",
#         "unwound": {
#           "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",
#           "title": "Building the Future of the Twitter API Platform"
#         }
#       }
#     ],
#     "user_mentions": [     
#     ]
#   }
# }
# '''

# tweet = json.loads(sample_json)
# urls = tweet["entities"]["urls"]

# print(f"URL: {type(urls)}")

################################################

# def sum_params(p1, p2=100, p3=10, p4=1):
#     return p1 + p2 + p3 + p4

# print(sum_params())

################################################




