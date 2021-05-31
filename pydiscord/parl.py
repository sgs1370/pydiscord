import requests

url = "https://api.opensea.io/api/v1/events"

querystring = {"only_opensea":"false","offset":"0","limit":"20","collection_slug":"bitshields"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
