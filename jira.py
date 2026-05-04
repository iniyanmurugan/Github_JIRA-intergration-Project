import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://iniyanmurugan.atlassian.net/rest/api/3/issue"

api_token=''
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

response = requests.post(url, data=payload, headers=headers, auth=auth)

# Check the output
if response.status_code == 201:
    print("Success!")
    print(response.json())
else:
    print(f"Failed with status {response.status_code}")
    print(response.text)
