import os

from requests import get
from dotenv import load_dotenv
from schema.meme import Meme

load_dotenv()
REDDIT_ENDPOINT_URL = os.getenv('REDDIT_ENDPOINT_URL')

def get_meme(subreddit: str):
  endpoint = f'{REDDIT_ENDPOINT_URL}/{subreddit}.json'
  res = get(endpoint)

  if res.status_code == 200:
    res = res.json()
    data = res['data']['children']
    print(data[2])

    test = Meme(**data[2]['data'])
    print(test)
    return test

  return data