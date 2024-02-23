from typing import Union
from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

class Image(BaseModel):
    ur: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    vat: float | None = None
    tag: set[str] = set()
    image: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.post('/offers')
async def create_Offer(offer: Offer):
    return offer



@app.put('/item/{item_id}')
async def update_item(item_id: int, item: Item):
    result = {'item_id': item_id, 'item': item}
    return result


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_price": item.price, "item_id": item_id}
