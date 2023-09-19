import requests
import json

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q": "tesla", "region": "US"}

headers = {
    "X-RapidAPI-Key": "1ac9ae1e49mshf51b3bcf9c404b8p139b22jsn6ed9a2a08255",
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring).json()


print(json.dumps(response, sort_keys=True, indent=4))

links = []
titles = []

# Loop through the news items and append links and titles to the lists
for i in range(2):
    links.append(response["news"][i]["link"])
    titles.append(response["news"][i]["title"])

# Print the lists of links and titles
print(links)
print(titles)
