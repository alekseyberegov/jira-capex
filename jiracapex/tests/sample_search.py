from requests.auth import HTTPBasicAuth
import json
import requests

url = "https://clicktripz.atlassian.net/rest/api/3/search"

auth = HTTPBasicAuth("aleksey@clicktripz.com", "mNnGfgV88Ocjrl4gnD91C6AF")

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps( {
  "expand": [
  ],
  "jql": "project = OL AND createdDate >= 2020-01-01 AND createdDate < 2022-01-01",
  "maxResults": 1,
  "fieldsByKeys": False,
  "fields": [
    "summary",
    "status",
    "assignee",
    "created",
    "creator"
  ],
  "startAt": 0
} )

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

