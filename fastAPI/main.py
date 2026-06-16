from fastapi import FastAPI

app = FastAPI()


# static Routes

@app.get('/')
def home():
    return {"message":"Namste dosto"}


@app.get('/about')
def about():
    return{"message":"i m about route"}


# Path Parameter
# @app.get('/users/{id}')
# def users(id:int):
#     return {"user Id":id}



# Query parameter with optional parameter without optional parameter facing errors so add optional parameter
# http://127.0.0.1:8000/users

@app.get('/users')
def users(name:str=None):
    return {"Name":name}


# default parameter
## in default parameter we pass the default value 
# http://127.0.0.1:8000/products?limit=200
@app.get('/products')
def products(limit:int=10):
    return {"products":limit}

# multiple parameter 

@app.get('/items')
def items(name:str=None,price:int=0):
    return{
        "Name":name,
        "Price":price
    }

