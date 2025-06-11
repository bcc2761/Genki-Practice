from fastapi import FastAPI

app = FastAPI()

items = []

# @app.post("/items/")
# async def create_item(item: dict):
#     items.append(item)
#     return {"item": item, "message": "Item created successfully"}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items