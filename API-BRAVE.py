#!/usr/bin/env python

import requests

print(
    requests.get(
        "https://api.search.brave.com/res/v1/llm/context",
        headers={
            "X-Subscription-Token": "<BRAVE_SEARCH_API_KEY>",
        },
        params={
            "q": "what is tallest mountain in solar system",
        },
    ).json()
)