import urllib
import json
import requests

api_key = ["cde8a184d3454fe88113f4561a159d8f"]

def bing_web_search(query, num_of_results = 25):
    base_url = "https://api.cognitive.microsoft.com/bing/v5.0/search"
    params = urllib.parse.urlencode({
        'q': query,
        'count': num_of_results,
        'offset': '0',
        'safesearch': 'Moderate',
    })
    headers = {'Ocp-Apim-Subscription-Key': api_key[0]}
    response_data = requests.get(base_url, params = params, headers=headers)

    json_data = response_data.json()['webPages']
    web_links = []
    for i in range(len(json_data['value'])):
        web_links.append(json_data['value'][i]['url'])
    return web_links