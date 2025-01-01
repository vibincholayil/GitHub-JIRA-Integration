from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createjira', methods = ['POST'])
def createjira():
        
    url = "https://vibin.atlassian.net/rest/api/3/issue"
    #API_TOKEN = "ATATT3xFfGF0kM9a6NKYRlGGtWXYZ67GtNJBjIINR-fS8Sx0ItjOh4lT4T6zPKFlamvQzP6N-7UTxIh5nNdO9umHCrY5p_H9O1AnUYp8--g7KDbnoa56WkEF3HchsmOmIrVckK3uMkpF7e6FNyivQ7tpzB73fUupa0o9xbcaCvV11BSW4Z67EZs=70A27FDD"
    #auth = HTTPBasicAuth("vibinnath.c@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10016"
        },
        
        
        "project": {
        "key": "VJ"
        },
        "summary": "issue found by vibin",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

app.run('0.0.0.0', port=5000)