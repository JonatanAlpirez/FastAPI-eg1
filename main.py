from fastapi import FastAPI
from typing import Union
from database import database as connection
from database import User


app = FastAPI(title='API eg', description='This is an API e.g.', version='1.0.1')

#Startup EVENT
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([User])
    
#Shutdown EVENT
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

#GET
@app.get("/")
async def read_root():
    return {"Helo" : "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#POST
@app.post()
async def create_item():
    pass

#PUT

#DELETE

