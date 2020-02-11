
import requests
import secrets

NEWSAPI_KEY = 'a5ef0f6edabe462e9f33c333b293a83e' 
base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "q" : "new hampshire",
    "country" : "us",
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
articles = result["articles"]

for a in articles:
	print(a['title'])