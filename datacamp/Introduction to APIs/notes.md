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

### Using request and response headers

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

## API Authentication

