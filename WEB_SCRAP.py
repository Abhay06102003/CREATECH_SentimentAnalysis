import requests
import pandas as pd
import numpy as np

class LinkedInScraper:
    def __init__(self, api_key, query, num):
        self.api_key = api_key
        self.query = query
        self.num = num
        self.base_url = 'https://api.scraperapi.com/structured/twitter/search'

    def scrape_linkedin(self):
        payloads = {
            'api_key': self.api_key,
            'query': self.query,
            'num': self.num
        }
        response = requests.get(self.base_url, params=payloads)
        if response.status_code == 200:
            data = response.json()
            data = data['organic_results']
            ans = []
            for datum in data:
                ans.append(datum['snippet'])
            ans = np.array(ans)
            return ans
        else:
            print("Error occurred:", response.status_code)
            return None
