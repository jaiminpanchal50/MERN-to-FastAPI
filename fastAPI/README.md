# FastApi

## Today we are going to learn FastAPI.

#### What is FastAPI?

#### FastAPI is the framework of python for create APIs

#### Create a virtual environment

```python
# this cmd create a separate virtual enevironment
python3 -m venv venv
# cmd activate the virtual enevironment
source venv/bin/activate
# fastAPI is the framework and uvicorn is the server
pip install fastapi uvicorn
# cmd for start server
uvicorn main:app --reload
```

#### How to create a GET Route (Static Route)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greet():
    print('Namste dosto')
```

#### Dynamic Route

##### Difference between Path and Query Parameter

###### Path parameters are variables embedded directly into the URL path. They are used to identify a specific, unique resource. Syntax in URL: /items/{item_id} FastAPI Syntax: You declare them in the route path and as function arguments with the exact same name.Required/Optional: Almost always required. If it's missing, the URL doesn't match the route. Example URL: http://localhost:8000/users/42

###### Query parameters are key-value pairs added to the end of a URL after a question mark (?), separated by ampersands (&). They are used to filter, sort, paginate, or search a collection of resources. Syntax in URL: /items?skip=0&limit=10 FastAPI Syntax: You declare them as standard function arguments. If they have a default value (e.g., skip: int = 0), they become optional. Required/Optional: Can be required (no default value) or optional (has a default value). Example URL: http://localhost:8000/users?role=admin&active=true

##### Path Parameter

###### without validation right now we are not checking the {id} is string or integer

```python
@app.get('/users/{id}')
def users(id):
    return {"user Id":id}
```

###### with validation right now we are checking the {id} is string or integer

```python
@app.get('/users/{id}')
def users(id:int):
    return {"user Id":id}
```

##### Query Parameter optional parameter

```python
# Query parameter with optional parameter without optional parameter facing errors so add optional parameter

@app.get('/users')
def users(name:str=None):
    return {"Name":name}
```

###### Default Parameter

```python
# in default parameter we pass the default value
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
```
