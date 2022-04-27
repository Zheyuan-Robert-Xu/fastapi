# from typing import Set, Tuple
# from typing import List
# from typing import Optional
# from datetime import date

# from fastapi import FastAPI
# from pydantic import BaseModel

# session FastAPI
# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_price": item.price, "item_id": item_id}

# session Features

# Declare a variable as a str
# and get editor support inside the function
# def main(user_id: str):
#     return user_id


# # A Pydantic model
# class User(BaseModel):
#     id: int
#     name: str
#     joined: date


# my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

# second_user_data = {
#     "id": 4,
#     "name": "Mary",
#     "joined": "2018-11-30",
# }

# # Pass the keys and values of the second_user_data dict directly as key-value arguments, equivalent to: User(id=4, name="Mary", joined="2018-11-30")
# my_second_user: User = User(**second_user_data)

# Session Python Types Info
# def get_full_name(first_name: str, last_name: str):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name


# print(get_full_name("john", "doe"))


# def get_name_with_age(name: str, age: int):
#     name_with_age = name + " is this old: " + str(age)
#     return name_with_age


# # def process_items(items: List[str]):
# #     for item in items:
# #         print(item)


# def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
#     return items_t, items_s


# class Person:
#     def __init__(self, name: str):
#         self.name = name


# def get_person_name(one_person: Person):
#     return one_person.name
