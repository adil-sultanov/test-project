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