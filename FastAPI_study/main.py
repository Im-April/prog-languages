from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get('/')
def read_root():
    return {"hello": "world"}  # 따옴표 일관성

@app.get('/items/{item_id}')  # 슬래시 추가
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}