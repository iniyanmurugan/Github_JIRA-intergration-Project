from flask import Flask, jsonify, request
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)


@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://iniyanmurugan.atlassian.net/rest/api/3/issue"

    
    api_token = ''
    auth = HTTPBasicAuth("iniyanmurugan@gmail.com", api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "project": {
                "key": "INI"
            },
            "summary": "Ticket created via API",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": "This is a test description.",
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "id": "10083"
            }
        }
    })

    # Execute the request
    response = requests.post(url, data=payload, headers=headers, auth=auth)

    # Parse response to JSON
    try:
        response_data = response.json()
    except json.JSONDecodeError:
        response_data = {"error": "Could not parse Jira response", "raw": response.text}

    # Log to the console for debugging
    if response.status_code == 201:
        print(f"Success! Issue Created: {response_data.get('key')}")
    else:
        print(f"Failed with status {response.status_code}")
        print(response.text)

    # Return the response to the client (browser/Postman)
    return jsonify(response_data), response.status_code


if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)
