# Introduction to APIs - Notes - DataCamp

##  Introduction to APIs

### What is an API?

- Applicatin Programming Interface
- Set of communication rules and abilities
- Enables interactions between software applications

### Web APIs, clients and server

- Web APIs communicate over the internet using HTTP
- Client sends a request message to a Server
- Server returns a response message to the Client
- Request/Response cycle [Image 1](image1.png)

### Types of Web APIs

- SOAP (Simple Object Access Protocol)
  - Focus on strict and formal API design
  - Enterprise level
- REST (Representational State Transfer)
  - Focus on simplicity and scalability
  - Most common API architecture
- GraphQL
  - Focus on flexibility and efficiency
  - Query language for APIs

### Working with APIs in Python

- urllib
  - Bundled with Python
  - Powerful but not very developer-friendly

  - Example:

    ```python
    from urllib.request import urlopen
    api = "https://api.music-catalog.com"

    with urlopen(api) as response:
        data = response.read()
        string = data.decode('utf-8')
        print(string)
    ```

- requests
  - Third-party library
  - Many powerful built-in features
  - More developer-friendly

  - Example:

    ```python
    import requests
    api = "https://api.music-catalog.com"
    response = requests.get(api)
    print(response.text)
    ```

------------------------------------------------

## Exercises 1

### API requests with urllib

- Instructions
  - Use the read function on the response object to read the response data from the response object.
  - Use the decode function to decode the response data into a string with the right encoding.

```python
from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
  
  # Use the correct function to read the response data from the response object
  data = response.____() # read
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.____(encoding) # decode
  
  print(string)
```

### Using the requests package

- Instructions
  - Import the requests package.
  - Pass the URL <http://localhost:3000/lyrics> to the requests.get method.
  - Print out the response text.

```python
# Import the requests package
import ____ # requests

# Pass the API URL to the get function
response = requests.get(____) # 'http://localhost:3000/lyrics'

# Print out the text attribute of the response object
print(response.____) # text
```

------------------------------------------------

## The Basic Anatomy of an API Request

### What are URLs

- Uniform Resource Locator
- The structured address of an API Resource
- Customize the URL to interact with specific API Resources
- `http://350.5th-ave.com/unit/243` - Example URL

###  Dissecting the URL

- Protocol: `http://` - the means of transportation
- Domain: `350.5th-ave.com` - the street address of the office building
- Path: `:80` - the gate or door to use when entering the building
- Path: `/unit/243` - the specific office unit inside the building
- Query: `?floor=2` - any additional instructions
- By constructing a URL with a path and parameters, we can control where to send our API requests to.

###  Adding Query Parameters with requests

- Use the `params` argument to add query parameters to a request

- Example:

  ```python
  import requests
  api = "https://api.music-catalog.com"
  # Create query parameters dictionary
  query_params = {'floor': 77, 'elevator': True}
  # Pass the query parameters to the get function
  response = requests.get(api, params=query_params)
  print(response.url)
  ```

### HTTP Verbs

- Destination: Unit 243 of the 350 5th Ave office building
- URL: `http://350.5th-ave.com/unit/243`

- Actions
  - GET - Read - Check the mailbox contents
  - POST - Create - Drop a new package in the mailbox
  - PUT - Update - Replace all packages with a new one
  - DELETE - Delete - Remove all packages from the mailbox

- There are more HTTP verbs, but these are the most common ones.
- The HTTP verb is the method of the request object.

###  Sending data via POST and PUT

- Each verb has its own method in the `requests` package
- Use the `data` argument to pass data to a POST or PUT request

- Example:

  ```python
  import requests
  url = 'http://350.5th-ave.com/unit/243'
  # GET = Retrieve a resource
  response = requests.get(url)
  # POST = Create a new resource
  response = requests.post(url, data={'package': 'new'})
  # PUT = Update an existing resource
  response = requests.put(url, data={'package': 'updated'})
  # DELETE = Remove a resource
  response = requests.delete(url)
  ```

------------------------------------------------

## Exercises 2

###  Constructing a URL with parameters

- You can fine-tune your API requests using the path and query parameters of the URL. Let's learn how you can use HTTP verbs, URL paths, and parameters using the requests package.

- In this exercise, you will make another API request to the Lyrics API, but instead of getting today's lyric, you will send a request to the random lyrics API. You will then further customize the API request by adding query parameters to filter on specific artists and include the track title. Below, you can find the details needed to construct the correct URL.

| Component | Value |
| --- | --- |
| Protocol | http |
| Domain | localhost |
| Port | 3000 |
| Path | /lyrics/random |
| Artist filter parameter | artist |
| Include track parameter | include_track |

- The requests library is already imported for your convenience.

- Instructions
  - Construct the URL to the random lyrics API for the requests.get() method using the protocol, domain, port and path components. Note: Do not use the query parameters yet.

    ```python
    # Construct the URL string and pass it to the requests.get() function
    response = requests.get(____) # 'http://localhost:3000/lyrics/random'

    print(response.text)
    ```
  
  - Create a dictionary variable with one entry: the key `artist` with the value `Deep Purple`.
  - Pass this dictionary to the `requests.get()` method as the `params` argument.

    ```python
    # Create a dictionary variable with query params
    query_params = {____} # 'artist': 'Deep Purple'

    # Pass the dictionary to the get() function
    response = requests.get('http://localhost:3000/lyrics/random', ____=____) # params=query_params

    print(response.text)
    ```

  - Add a second item to the dictionary with the key include_track and the Boolean value True.
  - Print the response's url attribute to see the full URL.
  - Print out the lyric.

    ```python
    # Add the `include_track` parameter
    query_params = {'artist': 'Deep Purple', ____} # 'include_track': True 

    response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

    # Print the response URL
    print(response.____) # url

    # Print the lyric
    print(response.____) # text
    ```

### Creating and deleting resources using an API

- In this exercise, you will use the playlists API available via <http://localhost:3000/playlists/>. This API offers the following actions:

| Verb | Path | Description |
| --- | --- | --- |
| GET | /playlists/ | Retrieve all playlists |
| GET | /playlists/{id} | Retrieve a specific playlist |
| POST | /playlists/ | Create a new playlist |
| DELETE | /playlists/{id} | Delete a specific playlist |

- You will start by getting a list of all existing playlists, then you will learn how to create a new playlist and verify it's creation, and last you will learn how to remove an existing playlist.

- Instructions
  - Get a list of all playlists from the playlists API.

    ```python
    import requests
    # Get a list of all playlists from the API
    response = requests.____('____') # get, 'http://localhost:3000/playlists/'
    print(response.text)
    ```

  - Create a dictionary with `Name` set to `Rock Ballads`, then perform a POST request with this dictionary as the `data` parameter.

    ```python
    # Create a dictionary with the playlist info
    playlist_data = {____: ____} # 'Name': 'Rock Ballads'

    # Perform a POST request to the playlists API with your dictionary as data parameter
    response = requests.____('http://localhost:3000/playlists', ____=playlist_data) # post, data=playlist_data
    print(response.text)
    ```

  - Perform a `GET`request to get information on the playlist with PlaylistId `2`.

    ```python
    # Perform a GET request to get info on playlist with PlaylistId 2
    response = requests.get('____') # 'http://localhost:3000/playlists/2'
    print(response.text)
    ```

  - Send a `DELETE`request to the URL for the playlist with PlaylistId `2` and get the list of existing playlists to confirm removal.

    ```python
    # Perform a DELETE request to the playlist API using the path to playlist with PlaylistId 2
    requests.____('____') # delete, 'http://localhost:3000/playlists/2'

    # Get the list of all existing playlists again
    response = requests.____('____') # get, 'http://localhost:3000/playlists/'
    print(response.text)
    ```

------------------------------------------------

##  Headers and Status Codes

### Request and Response Message Anatomy

- [Example Image 2](image2.png)
- The start line (blue one in the picture)
  - Request: `GET /lyrics/random HTTP/1.1` - Contain request method and where to send the request
  - Response: `HTTP/1.1 200 OK` - Contain the status code and the status message (Knowns as the status line)
  - A server will always include a numeric status code in the response message
- Headers (green one in the picture)
  - Contain information about the request or response
  - Key-value pairs that provide additional information about the request or response. Case-insensitive.
  - Example: `Content-Type: application/json`
  - Content negotiation: The client and server agree on the format of the data being sent
  - The `Accept` header is used by the client to specify the format of the response it expects. The `Content-Type` header is used by the server to specify the format of the response it is sending.

### Status Codes

- 1xx - Informational
- 2xx - Success
  - 200 OK - The request was successful
  - 201 Created - The request was successful and a new resource was created
- 3xx - Redirection
- 4xx - Client Error
  - 400 Bad Request - The request was malformed
  - 401 Unauthorized - The request requires authentication
  - 404 Not Found - The requested resource was not found
- 5xx - Server Error
  - 500 Internal Server Error - The server encountered an error

### Headers with requests

- Use the `headers` argument to pass headers to a request

```python
import requests
url = 'http://350.5th-ave.com/unit/243'
# Create headers dictionary
headers = {'Content-Type': 'application/json'}
# Pass the headers to the get function
response = requests.get(url, headers=headers)
print(response.text)

# Reading response headers
print(response.headers)

# We can access a specific header using the get method
print(response.headers.get('Content-Type'))
```

###  Status codes with requests

- The status code is stored in the `status_code` attribute of the response object

```python
import requests
url = 'http://350.5th-ave.com/unit/243'
response = requests.get(url)
print(response.status_code)

# Check if the request was successful
if response.status_code == 200:
    print('Success!')

# Looking up status codes using requests.codes
response = requests.get(url)
print(requests.status_code == requests.codes.not_found)
```

------------------------------------------------

## Exercises 3

###  Response Codes and APIs

- When a client sends a request to a server, the server response includes a numeric status code, which is used to tell the client how the server responded to the request.

- In this exercise you will learn about the most important status codes you should know. We will send requests to valid and invalid paths and learn how we can access the status code to determine if our request was successful or not.

- The `requests` package comes with a built-in status code lookup object `requests.codes` you can use when you don't remember the exact numerical values.

- Instructions
  - Check if the server responded successfully with the `200` status code.

    ```python
    import requests
    response = requests.get('http://localhost:3000/lyrics')

    # Check the response status code
    if (response.____ == ____): # status_code, 200
        print('The server responded succesfully!')
    ```

  - Perform a request to the inexistent `/movies` path of the music catalog API. Check if the server responded with a status code indicating the resource was not found, providing the appropriate numerical status code representing this.

    ```python
    # Make a request to the movies endpoint of the API
    response = requests.get('http://localhost:3000/____') # movies

    if (response.status_code == 200):
        print('The server responded succesfully!')
    
    # Check the response status code
    elif (response.status_code == ____): # 404
        print('Oops, that API could not be found!')
    ```

  - Check for response codes with a `200 OK` and `404 Not found` status code using the `requests.codes` lookup object.
  
    ```python
    response = requests.get('http://localhost:3000/movies')

    # Check if the response.status_code is equal to the requests.codes value for "200 OK"
    if (response.status_code == ____): # requests.codes.ok
        print('The server responded succesfully!')
    
    # Or if the request was not successful because the API did not exist
    elif (response.status_code == ____): # requests.codes.not_found
        print('Oops, that API could not be found!')
    ```

###  Using request and response headers

- Headers contain additional information about your API calls, including the desired or used response format. Using accept and content-type headers, client and server can negotiate what response format to use.

- In this exercise, you'll use headers to inspect response formats after making a request and make a new request specifying the desired format via the accept header.

- Instructions
  - Find out the content-type of the response by printing out the response `content-type` header.
  
    ```python
    import requests
    response = requests.get('http://localhost:3000/lyrics')

    # Print the response content-type header
    print(response.____) # headers.get('Content-Type')
    ```

  - Find out what content-types the server can respond with by printing out the response `accept` header.
  
    ```python
    response = requests.get('http://localhost:3000/lyrics')

    # Print the response accept header
    print(response.____) # headers.get('Accept')
    ```

  - Add an `accept` header to the request so the server returns JSON formatted data, then print the response `text` attribute.

    ```python
    # Set the content type to application/json
    headers = {____: ____} # 'Accept': 'application/json'
    response = requests.get('http://localhost:3000/lyrics', headers=headers)

    # Print the response's text
    print(response.____) # text
    ```

### Handling content-types errors

- What happens when you ask for a response in a specific format but the server cannot satisfy that request? Say you want to receive the response in XML rather than JSON. If the server can not respond in XML, it will respond with a specific status-code indicating that it can't reply in the requested format. The status code used in this case is 406 Not Acceptable or 406 in short. The response from the server also frequently contains an accept header which includes a list of all response formats it can respond with. Use this to learn what content types the API can respond with.

- Instructions
  - Add an `accept` header to request a response in the `application/xml` content-type from the server.
  - Check if the server did not accept the request using the relevant status code.
  - Print out a list of accepted content types from the server response.

  ```python
  # Add a header to use in the request
    headers = {____} # 'Accept': 'application/xml'
    response = requests.get('http://localhost:3000/lyrics', headers=headers)

    # Check if the server did not accept the request
    if (response.____ == ____): # status_code, 406
        print('The server can not respond in XML')
        
        # Print the accepted content types
        print('These are the content types the server accepts: ' + response.____) # headers['Accept']
    else:
        print(response.text)
    ```

------------------------------------------------

## Review

- You learned about headers and status codes, which are crucial for communicating additional information and understanding server responses in API requests.

- Headers: These are key-value pairs that provide extra details about the request or response. For example, the accept header tells the server what content type the client can handle.
- Status Codes: These three-digit codes indicate the outcome of the request. Key codes include:
  - `200 OK`: The request was successful.
  - `404 Not Found`: The requested resource does not exist.
  - `500 Internal Server Error`: The server encountered an error.

- You also practiced using the requests package to handle headers and status codes in Python. Here's a code snippet you worked with:

```python
# Add a header to use in the request
headers = {'accept': 'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == 406):
  print('The server can not respond in XML')
  
  # Print the accepted content types
  print('These are the content types the server accepts: ' + response.headers['accept'])
else:
  print(response.text)
```

- This code demonstrates how to request a specific content type and handle a `406 Not Acceptable` status code.

------------------------------------------------

## API Authentication

- APIs we interact with frequently contain private, personal or sensitive data. To protect this data, APIs require authentication to verify the identity of the client making the request.

### Accessing Sensitive Data

- Attempting to access sensitive data without authentication will result in a `401 Unauthorized` status code. This status code indicates that the client must provide valid credentials to access the resource. [Image 3](image3.png)

- To access the resource, the client must provide a valid username and password. This is known as basic authentication. Then the server will respond with a `200 OK` status code and the requested data. [Image 4](image4.png)

### Authentication Methods

| Method | Ease of implementation | Security Level |
| --- | --- | --- |
| Basic Authentication | 5/5 | 1/5 |
| API key/token Authentication | 4/5 | 2/5 |
| JWT Authentication | 3/5 | 4/5 |
| OAuth 2.0 | 1/5 | 5/5 |

- Basic Authentication: The client sends a username and password with each request. This method is easy to implement but not very secure. You send the credentials in plain text, which can be intercepted.

- API key/token Authentication: The client sends an API key or token with each request. This method is more secure than basic authentication because the key/token is unique to the client. However, it is still vulnerable to interception.

- JWT Authentication: The client sends a JSON Web Token (JWT) with each request. This method is more secure than the previous two because the token is encrypted. However, it is more complex to implement. It has a limited lifespan and must be refreshed periodically.

- OAuth 2.0: The client sends an access token with each request. This method is the most secure because the token is encrypted and has a limited lifespan. It is also the most complex to implement because it requires multiple steps to obtain the token.

- Check the API documentation to determine which authentication method is required.

### Basic Authentication with requests

- We need to add an authorization header to the request with the value `Basic` followed by the base64-encoded username and password separated by a colon. Base64 encoding is a two-way algorith that antone cna easily decode. [Image 5](image5.png)

```python
import requests
requests.get('http://localhost:3000/lyrics', auth=('username', 'password'))
```

### API key/token Authentication with requests

- Using a query parameter to pass the API key/token to the server.

```python
params = {'access_token': 'your_api_key'}
requests.get('http://localhost:3000/lyrics', params=params)
```

- Using the "Bearer" token in the authorization header.

```python
headers = {'Authorization': 'Bearer your_api_key'}
requests.get('http://localhost:3000/lyrics', headers=headers)
```

------------------------------------------------

## Exercises 4

### Basic Authentication Exercise

- Basic Authentication is the simplest authentication method for web APIs. It works like logging into a website. To gain access, you need to send your personal username and password along with every request. Using this username and password, the API can identify you and grant you access to the requested data.

- Let's first learn how a server responds when authentication fails, and then let's fix it by using Basic Authentication.

- Good to know: You can use the username `john@doe.com` and the password `Warp_ExtrapolationsForfeited2` to authenticate.

- Instructions
  - Check the numeric status code value on the request object for a successful response.
  - Also check for a failed authentication request which has a specific status-code too.

  ```python
  import requests
  response = requests.get('http://localhost:3000/albums')

  # Check if the status code on the response object matches a successful response
  if(response.____ == ____): # status_code, 200
      print("Success!")
  # Check if the status code indicates a failed authentication attempt
  elif(response.____ == ____): # status_code, 401
      print('Authentication failed')
  else:
      print('Another error occurred')
  ```

  - Create the correct authentication variable with your username and password.
  - Then pass the authentication variable to the requests.get() method using the correct argument.

  ```python
  # Create the authentication tuple with the correct values for basic authentication
  authentication = ____ # ('john@doe.com', 'Warp_ExtrapolationsForfeited2')

  # Use the correct function argument to pass the authentication tuple to the API
  response = requests.get('http://localhost:3000/albums', ____=authentication) # auth

  if(response.status_code == 200):
      print("Success!")
  elif(response.status_code == 401):
      print('Authentication failed')
  else:
      print('Another error occurred')
  ```

### API Key Authentication Exercise

- API key-based authentication functions similarly to Basic Authentication, but you must include a unique API key using either a request header or a URL parameter for authenticated requests. Let's explore both approaches.

- Good to know: Use the API key/token 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3 to authenticate.

- Instructions
  - Create a dictionary with a key-value pair for the API key. The API expects the `access_token` URL parameter to contain your unique API key. Pass the dictionary to the `requests.get()` function using the correct argument to pass URL parameters.

  ```python
  import requests
  # Create a dictionary containing the API key using the correct key-value combination
  params = {____: ____} # 'access_token': '8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'
  # Add the dictionary to the requests.get() call using the correct function argument
  response = requests.get('http://localhost:3000/albums', ____=params) # params

  if(response.status_code == 200):
      print("Success!")
  elif(response.status_code == 401):
      print('Authentication failed')
  else:
      print('Another error occurred')
  ```

  - Create a dictionary that includes a key-value pair for the API key, this time using the `Authorization` header. Pass the dictionary to the `requests.get()` function as headers.

  ```python
  import requests
  # Create a headers dictionary containing and set the API key using the correct key and value 
  headers = {____: ____} # 'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'
  # Add the headers dictionary to the requests.get() call using the correct function argument
  response = requests.get('http://localhost:3000/albums', ____=headers) # headers

  if(response.status_code == 200):
      print("Success!")
  elif(response.status_code == 401):
      print('Authentication failed')
  else:
      print('Another error occurred')
  ```

------------------------------------------------

## Working with Structured Data

### Complex Data Structures

- Lyric API returns the entire lyric as plain text, unstructured text. Complex data types, like music albums, require a more structured format. [Image 6](image6.png)

###  JSON

- JavaScript Object Notation
- Lightweight data-interchange format
- Widely supported by most programming languages
- Human readable and machine usable.
- JSON is one of the many types we call content-types, mime-types or media-types.
- Other common content-types include:
  - XML - eXtensible Markup Language - `application/xml`
  - CSV - Comma Separated Values - `text/csv`
  - YAML - YAML Ain't Markup Language - `application/yaml`
  - HTML - HyperText Markup Language - `text/html`

### From Python to JSON and back

- Python has a built-in module called `json` that can convert Python objects to JSON and vice versa.
- The `json` module has two main functions:
  - `json.dumps()`: Converts a Python object to a JSON string
  - `json.loads()`: Converts a JSON string to a Python object

```python
import json
# Convert a Python object to a JSON string
data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)
print(json_string)

# Convert a JSON string to a Python object
data = json.loads(json_string)
print(data)
```

### JSON with requests

- The `requests` package can automatically convert JSON responses to Python objects using the `response.json()` method.

```python
import requests
response = requests.get('http://localhost:3000/albums')
data = response.json()
print(data)
```

###  Sending JSON data

- Use the `json` argument to pass JSON data to a request

```python
import requests
playlist_data = {'name': 'Rock Ballads'}
response = requests.post('http://localhost:3000/playlists', json=playlist_data)

# Check if the request was successful
if response.status_code == 201:
    print('Playlist created!')

# Get the playlist data
request = response.request

# Print the request content-type header
print(request.headers['Content-Type']) # application/json
```

------------------------------------------------

## Exercises 5

### Requesting JSON data from an API

- When working with complex data structures, JSON is a popular format used by many web APIs. However, APIs can respond in other formats, too. Therefore, it's crucial you know how to request a specific format from an API. You can achieve this by adding a header to your requests.

- Which of the following requests will return data formatted as JSON?
- [ ] `requests.get('https://api.datacamp.com', headers={'accept': 'json'})`
- [x] `requests.get('https://api.datacamp.com', headers={'accept': 'application/json'})`
- [ ] `requests.get('https://api.datacamp.com', headers={'content-type': 'application/json'})`
- [ ] `requests.get('https://api.datacamp.com', json=true)`

### Receiving JSON with the requests package

- When requesting JSON data from an API, the requests library makes it really easy to decode the JSON string you received from the API back into a Python object. In this exercise you'll first need to request data in the JSON format from the API, then decode the response into a Python object to retrieve and print the album `Title` property.

- Note: The albums API is protected by authentication, the correct header has already been added.

- Instructions
  - Add the correct header to request JSON from the API.
  - Decode the JSON response into an album object.
  - Print the album Title property.

  ```python
  headers = {
    'Authorization': 'Bearer ' + API_TOKEN,
    # Add a header to request JSON formatted data
    ____: ____ # 'Accept': 'application/json'
  }
  response = requests.get('http://localhost:3000/albums/1/', headers=headers)

  # Get the JSON data as a Python object from the response object
  album = ____ # response.json()

  # Print the album title 
  print(____) # album['Title']
  ```

### Sending JSON with the requests package

- Similar to how you can receive JSON text from an API response, you can also send JSON text to an API with POST or PUT requests. If you use the `json` argument for the `request.post()` and `request.put()` methods, the `requests` library will take care of adding all the necessary headers and encoding for you. Neat!

- Let's try it out! Did you know you can create multiple playlists at once using a POST request to the `/playlists` API? Just pass an array of playlists (each with a `Name` property) to the API and it will create them all at once.

- Instructions
  - Pass the `playlists` variable as an argument to the `requests.post()` method so that it will be automatically sent as JSON.
  - Get a list of all playlists from the API.
  - Inspect the response of the GET request by printing the JSON text.

  ```python
  import requests
  playlists = [{"Name":"Rock ballads"}, {"Name":"My favorite songs"}, {"Name":"Road Trip"}]

  # POST the playlists array to the API using the json argument
  requests.post('http://localhost:3000/playlists/', ____=____) # json=playlists

  # Get the list of all created playlists
  response = requests.____('http://localhost:3000/playlists') # get

  # Print the response text to inspect the JSON text
  print(response.____) # text
  ```

------------------------------------------------

## Error Handling

### Error Status Codes

- 4xx - Client Error
  - Common causes: Bad request, unauthorized, not found
  - Resolution: Fix the request or provide valid credentials
  - 400 Bad Request - The request was malformed
  - 401 Unauthorized - The request requires authentication
  - 404 Not Found - The requested resource was not found
  - 429 Too Many Requests - The client has sent too many requests

- 5xx - Server Error
  - Common causes: Server overloaded, server configuration error, internal server error
  - Resolution: Wait for the server to be fixed. Fixed by the API administrator.
  - 500 Internal Server Error - The server encountered an error
  - 502 Bad Gateway - The server received an invalid response from an upstream server
  - 503 Service Unavailable - The server is not ready to handle the request
  - 504 Gateway Timeout - The server did not receive a timely response from an upstream server

### Handling Errors with requests

- API errors
  - The `response` object has a `status_code` attribute that contains the status code of the response
  - Use the `response.raise_for_status()` method to raise an exception if the status code indicates an error

```python
import requests
url = 'http://350.5th-ave.com/unit/243'
r = requests.get(url)

if r.status_code >= 400:
  print('Error:', r.status_code)
  r.raise_for_status()
else:
  print(r.text)
```

- Connection errors
  - Use the `requests.exceptions` module to handle connection errors
  - Use the `requests.exceptions.ConnectionError` exception to catch connection errors

```python
import requests
from requests.exceptions import ConnectionError

url = ''

try:
  r = requests.get(url)
  print(r.status_code)
except ConnectionError as conn_err:
  print(f'Connection error: {conn_err}')
  print(error)
```

### reaise_for_status() method

- The `raise_for_status()` method raises an exception if the status code indicates an error
- Use this method to handle errors in a more structured way

```python
import requests
from requests.exceptions import HTTPError, ConnectionError
url = 'http://350.5th-ave.com/unit/243'

try:
  r = requests.get(url)
  r.raise_for_status()
  print(r.status_code)
except HTTPError as http_err:
  print(f'HTTP error occurred: {http_err}')
except ConnectionError as conn_err:
  print(f'Connection error occurred: {conn_err}')
```

------------------------------------------------

## Exercises 6

### Handling errors with Requests

- When the `requests` library is unable to connect to an API server, it will raise an exception. This exception allows you to detect if the API is available and act accordingly. But even when the request is successfully sent, we can still encounter errors. If we send an invalid request, a `4xx Client Error` is returned from the API, if the server encounters an error, a `5xx Server Error` is returned.

- The `requests` package provides a set of included exceptions that can be used to handle these errors using `try/except` statements.

- Instructions
  - Import the exception class used to detect connection errors from the `requests` package, then use the imported class to intercept the error raised by the API request.
  
  ```python
  import requests
  # Import the correct exception class
  from ____ import ____ # requests.exceptions import ConnectionError

  url ="http://wronghost:3000/albums"
  try: 
      r = requests.get(url) 
      print(r.status_code)
  # Use the imported class to intercept the connection error
  except ____ as conn_err: # ConnectionError
      print(f'Connection Error! {conn_err}.')
  ```

  - Import the exception class used to detect errors returned via the response status code, then enable the setting on the response object which will automatically raise an error when an unsuccessful status code value is received. Finally, intercept the imported exception to print an error.
  
  ```python
  # Import the correct exception class
  from requests.exceptions import ____ # HTTPError

  url ="http://localhost:3000/albums/"
  try: 
      r = requests.get(url) 
    # Enable raising errors for all error status_codes
      r.____() # raise_for_status()
      print(r.status_code)
  # Intercept the error 
  except ____ as http_err: # HTTPError
      print(f'HTTP error occurred: {http_err}')
  ```

### Respecting API rate limits

- Let's put what we learned about error handling to the test. In this exercise you'll encounter a rate-limit error, which means you're sending too many requests to the server in a short amount of time. Let's fix it by implementing a workaround to circumvent the rate limit so our script doesn't fail.

- Your music library contains over 3500 music tracks, so let's try to find the longest track by checking the `Length` property of each track.

- But there is an issue, the `/tracks` API has a maximum page size of 500 items and has a rate-limit of 1 request per second. The script we've written is sending too many requests to the server in a short amount of time. Let's fix it!

- We've created the following variables for you:

```python
longestTrackLength = 0
longestTrackTitle = ""
headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
page_number = 1
```

- Instructions
  - Start by running the exercise without making changes to the code, you'll notice that the console outputs a `429 Client Error` indicating we are sending too many requests to the server in a short amount of time.
  - Fix the script by adding a 3 second pause at the end of the while-loop using the `sleep` method from the `time` package.

  ```python
  import requests
  import time

  while True:
    params = {'page': page_number, 'per_page': 500}
    response = requests.get('http://localhost:3000/tracks', params=params, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    
    print(f'Fetching tracks page {page_number}')

    if len(response_data['results']) == 0:
        break

    for track in response_data['results']:
        if(track['Length'] > longestTrackLength):
            longestTrackLength = track['Length']
            longestTrackTitle = track['Name']

    page_number = page_number + 1
    
    # Add your fix here
    # time.sleep(3)
  

  print('The longest track in my music library is: ' + longestTrackTitle)
  ```

------------------------------------------------

## Final Thoughts on What You've Learned

###  API Basics

- The role of APIs
- Different types of APIs
- URL components
- Anatomy of a request and response
- HTTP verbs

###  API Requests with Python

- Requests package
- HTTP methods
- URL Parameters
- Headers
- Status codes
- Different content types (JSON, XML, etc.)

###  Authentication

- Basic Authentication
- API key/token Authentication

###  Structured Data

- Reading JSON data
- Sending JSON data

### Handling Errors

- Types of errors
- Handling connection errors
- Handling HTTP errors
- Handling API errors
- Handling rate limits
- Using the `raise_for_status()` method
- Using the `requests.exceptions` module
