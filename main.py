from fastapi import FastAPI
from pydantic import BaseModel

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

@app.post('/items/')
def create_item(item: Item):
    return item