from pydantic import BaseModel

class Meme(BaseModel):
	title: str
	domain: str
	is_video: bool
	post_hint: str
	subreddit: str
	ups: int
	url_overridden_by_dest: str
