from pydantic import BaseModel
from requests import get

class Test(BaseModel):
  id: int
  name: str


data = {
  'id': 123,
  'name': "Ryan",
  'Extra': 123566
}

test = Test(**data)

print(test.id)

def get_meme():
  x = get('https://www.reddit.com/r/formuladank.json')
  print(x.content)
  return x.json

y = get_meme()
print(y)