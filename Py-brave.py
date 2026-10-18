import requests

response = requests.get(
  "https://api.search.brave.com/res/v1/llm/context",
  headers={
    "X-Subscription-Token": "<YOUR_API_KEY>",
    "Accept": "application/json",
    "Accept-Encoding": "gzip"
  },
  params={
    "q": "how deep is the mediterranean sea"
  },
).json()