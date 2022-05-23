from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, Form
from email.mime import image
from typing import Optional
from fastapi import FastAPI, Body, Path, Query, Header
from enum import Enum
from pydantic import BaseModel, Required, Field, HttpUrl
from datetime import datetime, time, timedelta
from uuid import UUID
app = FastAPI()


# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# fake_items_db = [{"item_name": "Foo"}, {
#     "item_name": "Bar"}, {"item_name": "Baz"}]


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# class User(BaseModel):
#     username: str
#     full_name: str | None = None


# class Item(BaseModel):
#     name: str = Field(example="Foo")
#     description: str | None = Field(default=None, example="A very nice Item")
#     price: float = Field(example=35.4)
#     tax: float | None = Field(default=None, example=3.2)


# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]


# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: datetime | None = Body(default=None),
#     end_datetime: datetime | None = Body(default=None),
#     repeat_at: time | None = Body(default=None),
#     process_after: timedelta | None = Body(default=None),
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }


# app = FastAPI()


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict


# @app.post("/images/multiple/")
# async def create_multiple_images(images: list[Image]):
#     return images


# @app.post("/index-weights/")
# async def create_index_weights(weights: dict[int, float]):
#     return weights


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_items(*, item_id: int = Path(title='The ID of the item to get', gt=0, le=1000, default=None), size: float = Query(gt=0, lt=10.5, default=None), q: str):
#     results = {'item_id': item_id}
#     if q:
#         results.update({"q": q, "size": size})
#     return results


# # Because path operations are evaluated in order, you need to make sure that the path
# # for /users/me is declared before the one for /users/{user_id}


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

# # /files//home/johndoe/myfile.txt, with a double slash (//) between files and home


# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# Response Model encoding parameters
# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str


# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/items/", response_model=list[Item])
# async def read_items():
#     return items


# @app.get("/keyword-weights/", responsße_model=dict[str, float])
# async def read_keyword_weights():
#     return {"foo": 2.3, "bar": 3.4}

# Form data

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(default=None), password: str = Form(default=None)):
    return {"username": username}
