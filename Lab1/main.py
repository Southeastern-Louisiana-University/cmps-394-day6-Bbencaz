from fastapi import FastAPI, HTTPException

app = FastAPI()


items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return item


@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items) :
        return items [item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(items):
        deleted_item = items.pop(item_id)
        return {"deleted": deleted_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")