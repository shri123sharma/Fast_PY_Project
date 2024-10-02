from fastapi import FastAPI
from app.database import init_db 
from app.v1.endpoint import items,products,cookies,headers,item_indexs,users,forms,country

app=FastAPI()

# Initialize the database (create tables)
init_db()

app.include_router(items.router,prefix="/items",tags=["items"])
app.include_router(products.router,prefix="/products",tags=["products"])
app.include_router(cookies.router,prefix="/cookies",tags=["cookies"])
app.include_router(headers.router,prefix="/headers",tags=["headers"])
app.include_router(item_indexs.router,prefix="/items_indexs",tags=["items_index"])
app.include_router(users.router,prefix="/users",tags=["users"])
app.include_router(forms.router,prefix="/forms",tags=["forms"])
app.include_router(country.router,prefix="/country",tags=["country"])

@app.get("/")
def default_run_project():
    return "This is FAST api project"
