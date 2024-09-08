from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# python -m uvicorn module_16_3:app

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/users/{username}/{age}')
async def new_user(username, age: str) -> str:
    data = f'Имя: {username}, возраст: {age}'
    new_index = str(int(max(users)) + 1)
    users[new_index] = data
    return f'User <{new_index}> is registered'


@app.put('/users/{user_id}/{username}/{age}')
async def upd_user(user_id: str, new_name, new_age) -> str:
    new_str = f'Имя: {new_name}, возраст: {new_age}'
    users[user_id] = new_str
    return f'The user <{user_id}> was updated'


@app.delete('/user/{user_id}')
def del_user(user_id):
    users.pop(user_id)
