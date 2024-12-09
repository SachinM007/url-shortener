from pydantic import BaseModel


class URLMapping(BaseModel):
    original_url: str
    short_id: str
