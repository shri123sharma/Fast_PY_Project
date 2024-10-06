from app.v1.schemas import *

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in:UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

def fake_password_hasher1(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user1(user_in: UserIn):
    hashed_password = fake_password_hasher1(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db