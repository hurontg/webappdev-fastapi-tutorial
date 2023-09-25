# Web Application Development using FastAPI (python)

# To uninstall all packages
`pip freeze > requirements.txt`
`pip uninstall -r requirements.txt -y`

# To activate virutal environment
`source ./env/bin/activate`

# To deactivate virutal environment
`deactivate`

# To install FastAPI
`pip install "fastapi[all]"`

# To install psycopg (PostgreSQL driver)
`pip install psycopg2-binary`

# To install security related stuff
`pip install "python-jose[cryptography]"`

`pip install "passlib[bcrypt]"`

# To run 
`uvicorn main:app --reload`

# First Steps

## Step 1: import 'FastAPI'
`FastAPI` is a Python class that provides all the functionality for your API.

## Step 2: create a FastAPI "instance"
Here the `app` variable will be an "instance" of the class FastAPI.

This will be the main point of interaction to create all your API.

This `app` is the same one referred by `uvicorn` in the command:

## Step 3: create a *path operation*

### Path

"Path" here refers to the last part of the URL starting from the first '/'.

So, in a URL like:

`https://example.com/items/foo`

..the path would be:

`/items/foo`

**A "path" is also commonly called an "endpoint" or a "route".**

**While building an API, the "path" is the main way to separate "concerns" and "resources".**

### Operation

"Operation" here refers to one of the HTTP "methods".

One of:

- POST
- GET
- PUT
- DELETE

...and the more exotic ones:

- OPTIONS
- HEAD
- PATCH
- TRACE

In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

- `POST`: to create data.
- `GET`: to read data.
- `PUT`: to update data.
- `DELETE`: to delete data.

So, in OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "operations" too.

**Define a path operation decorator**

`@app.get("/")`

The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:

- the path `/`
- using a `get` operation

**@decorator Info**

That `@something` syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below corresponds to the **path** `/` with an **operation** `get`.

It is the "**path operation decorator**".

## Step 4: define the **path operation function**

This is our "**path operation function**":

- **path**: is `/`.
- **operation**: is `get`.
- **function**: is the function below the "decorator" (below `@app.get("/")`).

```
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

This is a Python function.

It will be called by FastAPI whenever it receives a request to the URL "`/`" using a `GET` operation.