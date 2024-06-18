#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers for a given subreddit. """
    u_agent = 'Mozilla/5.0'
    headers = {'User-Agent': u_agent}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

# Example usage
if _name_ == "_main_":
    subreddit = "python"
    print(f"Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")
