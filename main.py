from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

@app.get('/')
async def root():
    return 'test'

@app.get('/calc/{x}/{y}')
def calc(x: int, y: int)->int:
    return x + y

@app.get('/files/{file_path:path}')
def get_path(file_path: str):
    return file_path

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post('/items/')
def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results: dict[str, object] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items2(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results: dict[str, object] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results