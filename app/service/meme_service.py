from requests import get

def get_meme():
  x = get('https://www.reddit.com/r/formuladank.json')
  return x