from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return 'test'

@app.get('/aida')
async def love():
    return {'message': 'I LOVE YOU'}

@app.get('/calc/{x}/{y}')
def calc(x: int, y: int)->int:
    return x + y

@app.get('/files/{file_path:path}')
def get_path(file_path: str):
    return file_path

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    print(skip, limit)
    return fake_items_db[skip : skip + limit]