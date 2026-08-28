
import json
import requests
import sys
if len(sys.argv) != 2:
    sys.exit("Please provide exactly one argument.")

requests = requests.get("https://api.github.com/users/" + sys.argv[1])
print(requests.json())
print(json.dumps(requests.json(), sort_keys=True, indent=2))

o =requests.json()
for result in o:
    print(result, ":", o[result])
    print(result,["trackName"])