#  Introduction to FastAPI - Notes - DataCamp

## FastAPI

### What is FastAPI?

- API: Application Programming Interface - refers to web applications using HTTP protocol to transmit structured data.
- Web Application: Application that serves traffic over the web
- Web Framework: Software framwork that helps build web applications
- FastAPI: Web framework for building high-performance APIs with Python

###  Key Features of FastAPI

- Fast (high performance)
- Low code and easy to learn: Python annotations and type hints
- Robust: Production-ready code with autodoc
- Standards-based: OpenAPI and JSON Schema support
- [Documentation](https://fastapi.tiangolo.com/)

###  FastAPI vs Other Web Frameworks

| Flask | Django | FastAPI | Key Differences |
|-------|--------|---------| -----------------|
| Build web-based (GUI) apps | Buil web-based (GUI) apps | Build APIs | For APIS without database operations |
| ORM optional | ORM built-in | ORM optional | Data and machine learning transactions |

###  FastAPI Installation

- Install FastAPI using pip

    ```bash
    pip install fastapi
    ```

- Crete your app in `main.py`

    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    ```

- Run your app

    ```bash
    fastapi dev main.py
    ```

###  Some Notes with FastAPI

- Can't run the FastAPI server with the "Run this code" button.
- Define server code in the Python editor as `main.py` instead.
- Run it from the termninal using the command `fastapi dev main.py`
- Verify that the logs in the terminal show `Application startup complete.`
- Stop the live server by pressing `Ctrl + C` in the terminal.
- You should install FastAPI in your own Python environment to get used to practicing with it.

--------------------

## Exercises - 1

### First application

- Let's run the FastAPI server for the first time! You can't run the FastAPI server directly with "Run this file" - see the instructions for how to run and stop the server from the terminal.

- Instructions
  - Run the live server in the bash repl (the terminal at the bottom): `fastapi dev main.py`
  - Verify the logs in the terminal show Application startup complete..
  - Stop the live server by pressing `Control+C`.

    ```python
    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    def root():
        return {"message": "Hello World"}
    ```

--------------------

## GET Operations

###  GET Operations Review

- HTTP protocol - several types of operations
- GET: Retrieve data from the server
- Example: `https://www.google.com:80/search?q=fastapi`
- The key parts of a GET request:
  - Host: `www.google.com`
  - Port: `80` (default)
  - Path: `/search`
  - Query: `?q=fastapi`

### FastAPI GET Operations

- Define a GET operation using the `@app.get` decorator
- The path is defined in the decorator

    ```python
    from faastapi import FastAPI

    app = FastAPI()

    @app.get("")
    def read_items():
        return {"message": "Hello World"}
    ```

- The application responds to requests to root by sending back a static dictionary with the key `message` and value `Hello World`. When it is returned, FastAPI will convert it to JSON format.

### Using the cURL web client

- cURL is a command-line tool for transferring data with URLs.
- Key cURL options:
  - `-X`: HTTP method
  - `-H`: Headers
  - `-d`: Data
  - `-i`: Include headers in the output
  - `-v`: Verbose mode
- Example: `curl -X GET http://localhost:8000/` - sends a GET request to the root path of the server.

###  Query Parameters

- New endpoint:
  - Path: "/hello"
  - Query parameter: "name"
    - Default value: "Alan"

    ```python
    @app.get("/hello")
    def hello_name(name: str = "Alan"):
        return {"message": f"Hello, {name}"}
    ```

- The query parameter is defined in the function signature with a default value.
- The query parameter is passed in the URL as `?name=Alan`.

--------------------

## Exercises - 2

### Hello World

- Let's build your first `GET` endpoint! You can't run the FastAPI server directly with "Run this file" - see the instructions for how to run and stop the server from the terminal.

- Instructions
  - Import FastAPI and instantiate the app server.
  - Run the live server in the terminal: `fastapi dev main.py`
  - Open a new terminal (top-right of terminal)
  - Test your code with the cURL command: `curl http://localhost:8000/` or `curl -X GET http://localhost:8000/`

    ```python
    from ____ import ____ # from fastapi import FastAPI

    app = ____() # app = FastAPI()


    @app.get("/")
    def root():
        return {"message": "Hello World"}
    ```

### Hello who?

- Let's build your first GET endpoint that accepts an input! You can't run the FastAPI server directly with "Run this file" - see the instructions for how to run and stop the server from the terminal.

- Instructions
  - Add a query parameter name with a default value "Alan".
  - Return a dictionary with the key message and the value "Hello {name}".
  - Run the live server in the terminal: `fastapi dev main.py`
  - Open a new terminal (top-right of terminal) and test your code with the following command:

  ```bash
    curl \
    -H 'Content-Type: application/json' \
    http://localhost:8000?name=Steve
    ```

    ```python
    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    def root(____: str = "____"):
        return {"message": f"Hello {____}"}
    ```

## POST Operations

### GET vs POST Operations

| GET | POST |
|-----|------|
| Traditional use: request info about an object | Traditional use: create a new object |
| Parameters sent via query string | Parameters sent via query string as well as request body |
| Limited data sent | Large data sent |
| Can be sent from a web browser | Requires an application or framework (cURL, requests) |

- GET example:

```python
api = "<http://localhost:8000>"
response = requests.get(f"{api}/hello?name=Steve")
```
  
- POST example:

```python
api = "http://localhost:8000"
body = {"name": "Steve"}
response = requests.post(f"{api}/hello", json=body)
```

### HTTP Request Body

- Data sent after the HTTP request header
- Header specifies body encoding
- Supports nested data structures
- JSON and XML are the most common encodings for APIs
- JSON is FastAPI's default encoding

- JSON Example:

```python
{
    "name": "Steve",
    "age": 30,
    "is_active": True,
    "items": ["item1", "item2"]
}
```

### pydantic BaseModel

- `pydantic` : interface to define request and response body schemas
- `BaseModel` : class to define the schema
- `Field` : class to define the data type and constraints
- This helps us keep our code clean and maintainable.
- With this structure, we can add attributes to the model and validate the data.
- Example:

```python
from pydantic import BaseModel

class Review(BaseModel):
    num_stars: int
    text: str
    public: bool = False

class MovieReview(BaseModel):
    movie: str
    # Nested model
    review: Review
```

### Handling POST Requests

- POST endpoint to create a new movie review
- Endpoint: `/reviews`
- Input: MovieReview
- Output: db_review

```python
@app.post("/reviews", response_model=DbReview)
def create_review(review: MovieReview):
    db_review = crud.create_review(review)
    return db_review
```

--------------------

## Exercises - 3

### Pydantic model

- You've been asked to create an API endpoint that manages items in inventory. To get started, create a Pydantic model for Items that has attributes name, quantity, and expiration.

- Instructions
  - Import date from datetime and BaseModel from pydantic.
  - Create a Pydantic model for Item.
  - Fill in the following fields correctly: name (string), quantity (integer, optional, default 0), and expiration (date, optional, default None).

```python
# Import date
from datetime import ____ # from datetime import date

# Import BaseModel
from pydantic import ____ # from pydantic import BaseModel

# Define model Item
class Item(____): # class Item(BaseModel):
    name: str
    ____: int = 0 # quantity: int = 0
    expiration: ____ = None # expiration: date = None

```

### POST operation in action

- You've been asked to create an API endpoint that accepts a `name` parameter and returns a message saying "We have `name`". To accomplish this, create a Pydantic model for `Item` and root endpoint `(/)` that serves HTTP POST operations. The endpoint should accept the Item model as input and respond with a message including `Item.name`.

- You can't run the FastAPI server directly with "Run this file" - see the instructions for how to run the server and test your code from the terminal.

- Instructions
  - Define pydantic model `Item` so that parameter name can be passed into the POST body.
  - Run the live server in the terminal: `fastapi dev main.py`
  - Open a new terminal (top-right of terminal) and test your code with the following command:

```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{"name": "bananas"}' \
  http://localhost:8000
```

```python
from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class ____(BaseModel): # class Item(BaseModel):
    ____: str # name: str

app = FastAPI()


@app.post("/")
def root(item: Item):
    name = item.name
    return {"message": f"We have {name}"}

```

## Review

- You learned about creating and managing POST operations in FastAPI, focusing on using Pydantic models to handle data. Here's a recap of the key concepts:

- Pydantic Model Creation: You created a Pydantic model named Item with attributes:

- name: a string representing the item's name.
- quantity: an integer with a default value of 0.
- expiration: a date with a default value of None.
- Defining POST Endpoints: You set up an API endpoint to accept POST requests using the Item model. This endpoint processes the input data and returns a message.

- Here's a code snippet from the lesson:

```python
# Import date
from datetime import date

# Import BaseModel
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str
    quantity: int = 0
    expiration: date = None
```

- Testing the Endpoint: You learned to test the POST endpoint using a curl command to send JSON data and receive a response.
