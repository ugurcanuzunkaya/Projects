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

--------------------

## Review - 1

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

--------------------

## PUT and DELETE Operations

### PUT vs DELETE

| PUT | DELETE |
|-----|--------|
| Traditional use: update an existing object | Traditional use: delete an existing object |
| Parameters sent via query string as well as request body | Parameters sent via query string as well as request body |
| Large data sent | Limited data sent |
| Requires an application or framework (cURL, requests) | Requires an application or framework (cURL, requests) |

- PUT Example:

```python
api = "http://localhost:8000"
body = {"name": "Steve", "age": 30}
response = requests.put(f"{api}/hello", json=body)
```

- DELETE Example:

```python
api = "http://localhost:8000"
response = requests.delete(f"{api}/hello?name=Steve")
```

### Referencing Existing Objects

- No ORM in FastAPI, so app must map objects to ID
- Database ID - unique identifier for each object
- `_id` - common name for the unique identifier
  - `review_id`: Table `reviews`, column `id`
  - Same convention in frameworks with ORM like Django and Flask

```python
from pydantic import BaseModel
class DbReview(BaseModel):
    movie: str
    num_stars: int
    text: str
    # Reference database ID of Reviews
    review_id: int
```

### Handling PUT Operation

- PUT endpoint to update a movie review
- Endpoint: `/reviews`
- Input: `DbReview`
- Output: `DbReview`

```python
@app.put("/reviews", response_model=DbReview)
def update_review(review: DbReview):
    db_review = crud.update_review(review)
    return db_review
```

### Handling DELETE Operation

- DELETE endpoint to delete a movie review
- Endpoint: `/reviews`
- Input: `DbReview`

```python
@app.delete("/reviews", response_model=DbReview)
def delete_review(review: DbReview):
    crud.delete_review(review)
    return {}
```

--------------------

## Exercises - 4

### PUT operation in action

- You've been asked to create a PUT endpoint `/items` that accepts parameters `name` and `description` and updates the `description` based on the `name` in a key-value store called `items`.

- You can't run the FastAPI server directly with "Run this file" - see the instructions for how to run the server and test your code from the terminal.

- Instructions
  - Define pydantic model `Item` so that parameters `name` and `description` can be passed into the PUT body.
  - Update `description` in `items` based on the key `name`.
  - Run the live server from the terminal: `fastapi dev main.py`.
  - Open a new terminal (top-right of terminal) and test your code with the following command:

    ```bash
        curl -X PUT \
        -H 'Content-Type: application/json' \
        -d '{"name": "bananas", "description": "Delicious!"}' \
        http://localhost:8000/items
    ```

    ```python
    from fastapi import FastAPI
    from pydantic import BaseModel

    # Define model Item
    class Item(BaseModel):
        ____: str # name: str
        ____: str # description: str

    # Define items at application start
    items = {"bananas": "Yellow fruit."}

    app = FastAPI()


    @app.put("/items")
    def update_item(item: Item):
        name = item.name
        # Update the description
        items[____] = item.____ # items[name] = item.description
        return item
    ```

### DELETE operation in action

- You've been asked to create a DELETE endpoint that accepts parameter `name` and deletes the item called `name` from a key store called `items`.

- You can't run the FastAPI server directly with "Run this file" - see the instructions for how to run the server and test your code from the terminal.

- Instructions
  - Define pydantic model `Item` with parameter `name`.
  - Delete from `items` based on the key `name`.
  - Run the live server from the terminal: `fastapi dev main.py`.
  - Open a new terminal (top-right of terminal) and test your code with the following command:

    ```bash
    curl -X DELETE \
    -H 'Content-Type: application/json' \
    -d '{"name": "bananas"}' \
    http://localhost:8000/items
    ```

    ```python
    from fastapi import FastAPI
    from pydantic import BaseModel

    # Define model Item
    class Item(BaseModel):
        ____: str # name: str

    # Define items at application start
    items = {"apples", "oranges", "bananas"}

    app = FastAPI()


    @app.delete("/items")
    def delete_item(item: Item):
        name = item.name
        # Delete the item
        items.remove(____) # items.remove(name)
        return {}
    ```

--------------------

## Handling Errors

###  Error Handling

- User Error
  - Invalid or outdated URI
  - Missing or invalid input

    ```python
    @app.delete("/items")
    def delete_item(item: Item):
        if item.id not in item_ids:
            return {"error": "Item not found"}
        else:
            crud.delete_item(item)
            return {}
    ```

- Server Error
  - Something else happended

  ```python
    @app.delete("/items")
    def delete_item(item: Item):
        try:
            crud.delete_item(item)
            return {}
        except:
            return {"error": "Server error"}
    ```

### HTTP Status Codes: "Levels of Yelling"

- Enables API to provide status in response
  - Success, failure, error, etc.
- Specific codes defined in HTTP protocol
- Range: 100 - 599
- Categorize by first number (1 - 5)
  - 1xx: Informational repsonses (100 - 199)
  - 2xx: Success responses (200 - 299)
  - 3xx: Redirection messages (300 - 399)
  - 4xx: Client Error responses (400 - 499)
  - 5xx: Server Error responses (500 - 599)

### Common HTTP Status Codes

- Success (2xx)
  - 200: OK - Default success response
  - 201: Created - Specific to POST operation
  - 202: Accepted - Noncommittal. "Working on it"
  - 204: No Content - Success! Nothing more to say

- Other responses
  - 301: Moved Permanently - URI changed permanently
  - 400: Bad Request - Client error
  - 404: Not Found - Server cannot find the requested resource
  - 500: Internal Server Error - Server has encountered a situation it doesn't know how to handle

### Handling Errors with Status Codes

- Example of handling errors with status codes in FastAPI

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.delete("/items")
def delete_item(item: Item):
    if item.id not in item_ids:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        delete_item_in_database(item)
        return {}
```

--------------------

## Exercises - 5

### Handling a client error

- You've been asked to create a DELETE endpoint that accepts parameter `name` and deletes the item called `name` from a key store called `items`. If the item is not found, the endpoint should return an appropriate status code and detailed message.

You can't run the FastAPI server directly with "Run this file" - see the instructions for how to run the server and test your code from the terminal.

- Instructions
  - Import `HTTPException` from FastAPI.
  - Raise `HTTPException` if an item is not in `items`.
  - Specify the appropriate status code for "not found."
  - Run the live server from the terminal: `fastapi dev main.py`.
  - Open a new terminal (top-right of terminal) and test your code with the following command:

    ```bash
    curl -X DELETE \
    -H 'Content-Type: application/json' \
    -d '{"name": "bananas"}' \
    http://localhost:8000/items
    ```

    ```python
    from fastapi import FastAPI, ____ # from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    # Define model Item
    class Item(BaseModel):
    name: str

    # Define items at application startup
    items = {"apples", "oranges"}

    app = FastAPI()


    @app.delete("/items")
    def delete_item(item: Item):
    name = item.name
    if name in items:
        items.remove(name)
    else:
        # Raise HTTPException with status code for "not found"
        raise ____(status_code=____, detail="Item not found.") # raise HTTPException(status_code=404, detail="Item not found.")
    return {}
    ```

--------------------

## Using async for Concurrent Work

### Why use async?

- Sequential code: One operation at a time
- Asynchronous code: Multiple operations at once
- If we use async our API can serve requests concurrently and spend less time waiting for work to be done.
- [Documentation Link](https://fastapi.tiangolo.com/async/)

### Async in FastAPI

- Sequential code:

```python
def get_sequential_burgers(number:int):
    # Do some sequential work

    return burgers

# Calling the function sequentially
burgers = get_sequential_burgers(10)
```

- Asynchronous code:

```python
async def get_async_burgers(number:int):
    # Do some asynchronous work

    return burgers

# Calling the function asynchronously
burgers = await get_async_burgers(10)
```

###  FastAPI with async

- If we can:

```python
results = await some_async_function()
```

- Then use `async def`:

```python
@app.get("/")
async def read_results():
    results = await some_async_function()
    return results
```

- Note: Only use `await` inside of functions created with `async def`.

###  When to use async

- Use async
  - If our application doesn't have to communicate with anything else and wait for it to respond
  - Examples:
    - Audio or image processing
    - Computer vision
    - Machine Learning
    - Deep Learning

- Don't use async
  - If our application has to communicate with: File system, database, another server, etc.
  - If we aren't sure if we should use async
  - Examples:
    - CRUD operations
    - API requests
    - Database transactions

--------------------

## Exercises - 6

###  Asynchronous DELETE operation

- You've been asked to create an API endpoint that deletes items managed by your API. To accomplish this, create an endpoint `/items` that serves HTTP DELETE operations. Make the endpoint asynchronous, so that your application can continue to serve requests while maintaining any long-running deletion tasks.

- We can't run the FastAPI server directly with "Run this file" - see the instructions for how to run the server and test your code from the terminal.

- Instructions
  - Make the delete operation asynchronous.
  - Validate the existence of `item.name` in list `items`.
  - Return the appropriate status code for "not found."
  - Run the live server from the terminal: `fastapi dev main.py`.
  - Open a new terminal (top-right of terminal) and test your code with the following command:
  
    ```bash
    curl -X DELETE \
    -H 'Content-Type: application/json' \
    -d '{"name": "rock"}' \
    http://localhost:8000/items

    curl -X DELETE \
    -H 'Content-Type: application/json' \
    -d '{"name": "roll"}' \
    http://localhost:8000/items
    ```

    ```python
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    # Define model Item
    class Item(BaseModel):
        name: str

    app = FastAPI()

    items = {"rock", "paper", "scissors"}


    @app.delete("/items")
    # Make asynchronous
    ____ def root(item: Item): # async def root(item: Item):
        name = item.name
        # Check if name is in items
        if ____ not in ____: # if name not in items:
            # Return the status code for not found
            raise HTTPException(status_code=___, detail="Item not found.") # raise HTTPException(status_code=404, detail="Item not found.")
        items.remove(name)
        return {"message": "Item deleted"}
    ```

--------------------

## Review - 2

- You learned about supporting PUT and DELETE operations in FastAPI, focusing on asynchronous operations to handle concurrent requests efficiently. Here's a recap of the key points:

- Using async in FastAPI:

- You should use async when all functions within your endpoint can be called with await. This allows your application to handle multiple requests simultaneously, improving performance under high workloads.
Asynchronous DELETE operation:

- You created an asynchronous endpoint /items for handling HTTP DELETE operations. This ensures that your application can continue processing other requests while performing long-running deletion tasks.
You validated the existence of item.name in the list items and returned a 404 status code if the item was not found.
- Code Example:

```python
@app.delete("/items")
async def delete_item(item: Item):
    if item.name not in items:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    # Perform deletion logic here
```

- This lesson emphasized the importance of using async judiciously to enhance the performance of your FastAPI applications.

--------------------

## FastAPI Automated Testing

### What is Automated Testing?

- Unit Tests
  - Focus: Isolated code
  - Purpose: Validate code function
  - Scope: Function or method
  - Environment: Isolated Python ENV

    ```python
    def test_main():
        response = main()
        assert response == {"message": "Hello World"}
    ```

- System Tests
  - Focus: Isolated system operations
  - Purpose: Validate system function
  - Scope: Endpoint
  - Environment: Python env with app running
  
  ```python
  def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
  ```

### Using TestClient

- FastAPI lets us write automated system tests using the `TestClient` class.
- `TestClient` simulates a web browser and sends requests to the FastAPI application.
- We can use the `TestClient` to test the application's endpoints. Validate any aspect of the full HTTP request and response.

- Example:

```python
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

### Testing Error or Failure Responses

- FastAPI system tests let us test error or failure responses just like success responses, by validating the HTTTP status code and response body.

- App

```python
app = FastAPI()

@app.delete("/items")
def delete_item(item: Item):
    if item.name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        delete_item_in_database(item)
        return {}
```

- Test

```python
def test_delete_item_not_found():
    response = client.delete("/items", json={"name": "rock"})
    assert response.status_code == 404
    json = response.json()
    assert response.json() == {"detail": "Item not found"}
```

--------------------

## Exercises - 7

###  System test

- You've built your FastAPI application and added unit tests to verify code functionality. Writing a system test for an API endpoint will ensure that the endpoint works on the running application.

- Instructions
  - Review the GET endpoint defined in `main.py`.
  - Complete the following system test in `system_test.py`
  - In the terminal, run `pytest`.

  ```python
    # main.py
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import Optional

    # define model Item
    class Item(BaseModel):
        name: str
        quantity: Optional[int] = 0

    app = FastAPI()

    items = {"scissors": Item(name="scissors", quantity=100)}


    @app.get("/items")
    def read(name: str):
        if name not in items:
            raise HTTPException(status_code=404, detail="Item not found")
        return items[name]

    # system_test.py
    # Import TestClient
    from fastapi.testclient import ____ # from fastapi.testclient import TestClient
    from main import app

    # Create test client with application context
    client = TestClient(____) # client = TestClient(app)

    def test_main():
        response = client.get("/items?name=scissors")
        assert response.status_code == 200
        assert response.json() == {"name": "scissors",
                                "quantity": ____} # "quantity": 100
    ```

## Building a JSON CRUD API

### Four Steps in Object Management Lifecycle (CRUD)

[Lifecycle](image.png)

- Lifecycle:
  - Create: Add a new object
  - Read: Retrieve an object
  - Update: Modify an object
  - Delete: Remove an object

- CRUD operations for HTTP protocol:
  - POST: Create
  - GET: Read
  - PUT: Update
  - DELETE: Delete

- We can build a JSON CRUD API using FastAPI to manage objects in a database.

### JSON CRUD API Motivation

- Fundamentals
  - Manage the entire object lifecycle
  - Understand best practices for HTTP API operations
  - Design our own data management APIs

- Oppurtunities
  - Business logic for more complex data operations
  - High throughput and low latency for data pipelines
  - Machine Learning inference pipelines

- Challenges
  - Data consistency and integrity
  - Data security and privacy
  - Data scalability and performance

### Building a CRUD Module

- We can build a CRUD module to manage objects in a database.
- The module will have functions to create, read, update, and delete objects.
- We can use the module to manage objects in the database.

- Example:

```python
from pydantic import BaseModel

class Review(BaseModel):
    movie: str
    num_stars: int
    text: str


class DbReview(BaseModel):
    movie: str
    num_stars: int
    text: str
    review_id: int


# crud.py

def create_review(review: Review) -> DbReview:
    # Create a new review in the database
    return db_review

def read_review(review_id: int) -> DbReview:
    # Read a review from the database
    return db_review

def update_review(review: DbReview) -> DbReview:
    # Update a review in the database
    return db_review

def delete_review(review: DbReview):
    # Delete a review from the database
    pass
```

### POST Endpoint to Create

- Endpoint: `/reviews`
- Input: `Review`
- Output: `DbReview`

```python
@app.post("/reviews", response_model=DbReview)
def create_review(review: Review):
    db_review = crud.create_review(review)
    return db_review
```

### GET Endpoint to Read

- Endpoint: `/reviews`
- Input: `?review_id=1234`
- Output: `DbReview`

```python
@app.get("/reviews", response_model=DbReview)
def read_review(review_id: int):
    db_review = crud.read_review(review_id)
    return db_review
```

### PUT Endpoint to Update

- Endpoint: `/reviews`
- Input: `DbReview`
- Output: `DbReview`

```python
@app.put("/reviews", response_model=DbReview)
def update_review(review: DbReview):
    db_review = crud.update_review(review)
    return db_review
```

### DELETE Endpoint to Delete

- Endpoint: `/reviews`
- Input: `DbReview`
- Output: `{}`

```python
@app.delete("/reviews", response_model=DbReview)
def delete_review(review: DbReview):
    crud.delete_review(review)
    return {}
```

--------------------

## Exercises - 8

###  Complete JSON CRUD API

- You've been asked to build a JSON CRUD API to manage item names and quantities. To test your API you need to create an item, read it, update it, delete, and verify it's been deleted.

- Instructions
  - Fill in the missing HTTP operations and status codes in `main.py`
  - Run the live server from the terminal: `fastapi dev main.py`
  - Open a new terminal (top-right of terminal) and test your code with the following five commands:

    ```bash
    curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"name": "rock"}' \
    http://localhost:8000/items

    curl http://localhost:8000/items?name=rock

    curl -X PUT \
    -H 'Content-Type: application/json' \
    -d '{"name": "rock", "quantity": 100}' \
    http://localhost:8000/items

    curl -X DELETE \
    -H 'Content-Type: application/json' \
    -d '{"name": "rock"}' \
    http://localhost:8000/items

    curl http://localhost:8000/items?name=rock
    ```

  - Verify that the first four commands return 200 OK, and the final command returns 404 Not Found

    ```python
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import Optional

    # define model Item
    class Item(BaseModel):
        name: str
        quantity: Optional[int] = 0

    app = FastAPI()

    items = {}


    @app.____("/items") # POST
    def create(item: Item):
        name = item.name
        if name in items:
            raise HTTPException(status_code=409, detail="Item exists")
        items[name] = item
        return {"message": f"Added {name} to items."}
    
    @app.____("/items") # GET
    def read(name: str):
        if name not in items:
            raise HTTPException(status_code=____, detail="Item not found") # 404
        return items[name]  
    
    @app.____("/items") # PUT
    def update(item: Item):
        name = item.name
        if name not in items:
            raise HTTPException(status_code=____, detail="Item not found") # 404
        items[name] = item
        return {"message": f"Updated {name}."}
    
    @app.delete("/items")
    def delete(item: Item):
        name = item.name
        if name not in items:
            raise HTTPException(status_code=____, detail="Item not found") # 404
        del items[name]
        return {"message": f"Deleted {name}."}
    ```

--------------------

## Review - 3

- You learned about building and testing a JSON CRUD API using FastAPI, focusing on managing object lifecycles over HTTP. Here are the key points you covered:

- HTTP Operations & CRUD Steps:
  - POST is used to create objects
  - GET is used to read objects.
  - PUT is used to update objects.
  - DELETE should return an empty response upon successful deletion, as no data remains.

- Building a JSON CRUD API:
  - You were tasked with creating an API to manage item names and quantities.
  - The process involved creating, reading, updating, and deleting items to verify functionality.

- Testing the API:
  - You used curl commands to test the API endpoints:

    ```bash
    curl -X POST -H 'Content-Type: application/json' -d '{"name": "rock"}' http://localhost:8000/items
    curl http://localhost:8000/items?name=rock
    curl -X PUT -H 'Content-Type: application/json' -d '{"name": "rock", "quantity": 100}' http://localhost:8000/items
    curl -X DELETE -H 'Content-Type: application/json' -d '{"name": "rock"}' http://localhost:8000/items
    curl http://localhost:8000/items?name=rock
    ```

  - Verified that the first four commands returned 200 OK, and the last returned 404 Not Found.

## Writing a Manual Functional Test

### What is a Functional Test?

- System Tests
  - Focus: Isolated system operations
  - Purpose: Validate system function
  - Scope: Endpoint
  - Environment: Python env with app running

    ```python
    def test_read():
        response = client.get("/items/1")
        assert response.status_code == 200
    ```

- Functional Tests
  - Focus: Integrated system
  - Purpose: Validate system overall
  - Scope: Application
  - Environment: Python env with app running

    ```python
    def test_delete_then_read():
        response = client.delete("/items/1")
        assert response.status_code == 200
        response = client.get("/items/1")
        assert response.status_code == 404
    ```

- The big difference is that the functional test validates the intraction between two endpoints.

###  Test Workflows

- Test workflows are a critical concept in functional testing.
- Workflows are specific sequences of application actions. Defining workflows forces us to identify endpoint combinations that should succeed or fail.
- This lets us build functional tests that the overall applications and not just specific endpoints.

### Functional Test Workflows Examples

- Successful Workflow
  - Create an item, then read it
  - Create an item, then update it
  - Create an item, then delete it

- Failing Workflow
  - Read without creating an item
  - Update after deleting an item
  - Delete without creating an item

###  Functional Test Scripts

- Outside test framework - "Manual tests"
- Test framework like `pytest`

- Use `requests` library to send HTTP requests

```python
import requests
ENDPOINT = "http://localhost:8000/items"
# Create an item "rock"
r = requests.post(ENDPOINT, json={"name": "rock"})
assert r.status_code == 200
# Get the item "rock"
r = requests.get(ENDPOINT, params={"name": "rock"})
assert r.status_code == 200
```

- Workflows built against known application state

--------------------

## Exercises - 9

###  Functional test

- You've built your FastAPI application and added system tests to verify the functionality of each endpoint. Building a functional test for a core API workflow will ensure that the endpoints work together for the full life cycle of your data.

- We can't run the FastAPI server directly with "Run this file" - see the instructions for how to run the server and test your code from the terminal.

- Instructions
  - Review the CRUD API defined in `main.py`.
  - Complete the following functional test workflow in `functional_test.py`.
  - Run the live server from the terminal: `fastapi dev main.py`.
  - Open a new terminal (top-right of terminal) with `functional_test.py` open and click "Run this file" to test your code.

  ```python
    # functional_test.py
    import requests

    ENDPOINT = "http://localhost:8000/items"

    # Create item "rock" without providing quantity
    r = requests.post(ENDPOINT, json={"name": "rock"})
    assert r.status_code == ____ # 200
    assert r.json()["message"] == "Added rock to items."

    # Verify that item "rock" has quantity 0
    r = requests.get(ENDPOINT + "?____=____") # name, rock
    assert r.status_code == 200
    assert r.json()["quantity"] == 0

    # Update item "rock" with quantity 100
    r = requests.put(ENDPOINT, json={"name": "rock", "quantity": 100})
    assert r.status_code == 200
    assert r.json()["message"] == "Updated rock."

    # Verify that item "rock" has quantity 100
    r = requests.get(ENDPOINT + "?name=rock")
    assert r.status_code == 200
    assert r.json()["quantity"] == ____ # 100

    # Delete item "rock"
    r = requests.delete(ENDPOINT, json={____: ____}) # name, rock
    assert r.status_code == 200
    assert r.json()["message"] == "Deleted rock."

    # Verify that item "rock" does not exist
    r = requests.get(ENDPOINT + "?name=rock")
    assert r.status_code == ____ # 404

    print("Test complete.")

    # main.py
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import Optional

    # define model Item
    class Item(BaseModel):
        name: str
        quantity: Optional[int] = 0

    app = FastAPI()

    items = {}


    @app.post("/items")
    def create(item: Item):
        name = item.name
        if name in items:
            raise HTTPException(status_code=409, detail="Item exists")
        items[name] = item
        return {"message": f"Added {name} to items."}
    
    @app.get("/items")
    def read(name: str):
        if name not in items:
            raise HTTPException(status_code=404, detail="Item not found")
        return items[name]  
    
    @app.put("/items")
    def update(item: Item):
        name = item.name
        if name not in items:
            raise HTTPException(status_code=404, detail="Item not found")
        items[name] = item
        return {"message": f"Updated {name}."}
    
    @app.delete("/items")
    def delete(item: Item):
        name = item.name
        if name not in items:
            raise HTTPException(status_code=404, detail="Item not found")
        del items[name]
        return {"message": f"Deleted {name}."}
    ```

--------------------

##  Wrap Up

###  FastAPI Review

- FastAPI key feautures:
  - Easy to use
  - Fast and efficient
  - Built-in data validation
  - Automatic API documentation
  - Support for async operations

- FastAPI use cases:
  - Building APIs for web applications
  - Building APIs for machine learning models
  - Building APIs for data pipelines

- Four Type of HTTP Operations:
  - POST: Create
  - GET: Read
  - PUT: Update
  - DELETE: Delete

- Building a JSON CRUD API:
  - Create, read, update, and delete objects
  - Use Pydantic models for data validation
  - Use FastAPI to define endpoints

- Using status codes to communicate success and failure:
  - 200: OK
  - 201: Created
  - 404: Not Found
  - 500: Internal Server Error

- Using `async` for concurrent work:
  - Use `async` to handle multiple requests
  - Use `await` to call async functions

- System tests and functional tests:
  - System tests validate individual endpoints
  - Functional tests validate workflows across endpoints

- Manual functional tests:
  - Use `requests` library to send HTTP requests
  - Validate workflows against known application state
