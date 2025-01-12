# Intermediate to Python for Developers Course - Datacamp

## Built-in Functions

### max() and min()

- max() and min() functions can be used to find the maximum and minimum values in a list.
- max() and min() can also be used to find the maximum and minimum values in a dictionary.
- max() and min() can also be used to find the maximum and minimum values in a string.

```python
# max() and min() functions
numbers = [1, 2, 3, 4, 5]
max_num = max(numbers)
min_num = min(numbers)
print(max_num) # 5
print(min_num) # 1

# max() and min() functions with dictionary
stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}
max_stock = max(stocks)
min_stock = min(stocks)
print(max_stock) # YHOO
print(min_stock) # AAPL

# max() and min() functions with string
name = 'DataCamp'
max_char = max(name)
min_char = min(name)
print(max_char) # t
print(min_char) # C
```

### sum() and round()

- sum() function can be used to find the sum of all the elements in a list.
- round() function can be used to round off a number to a specified number of decimal places.

```python
# sum() and round() functions
numbers = [1, 2, 3, 4, 5]
sum_numbers = sum(numbers)
print(sum_numbers) # 15

pi = 3.14159
round_pi = round(pi, 2)
print(round_pi) # 3.14
```

- You can nest functions inside each other.

```python
# Nesting functions
numbers = [1, 2, 3, 4, 5]
sum_numbers = sum(numbers)
round_sum = round(sum_numbers, 2)
print(round_sum) # 15.0
```

### len() and sorted()

- len() function can be used to find the length of a list.
- sorted() function can be used to sort a list in ascending order.

```python
# len() and sorted() functions
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
sorted_numbers = sorted(numbers)
print(length) # 5
print(sorted_numbers) # [1, 2, 3, 4, 5]
```

- You can use len() and sorted() functions with strings.

```python
# len() and sorted() functions with string
name = 'DataCamp'
length = len(name)
sorted_name = sorted(name)
print(length) # 8
print(sorted_name) # ['D', 'a', 'a', 'm', 'p', 't']
```

### Benefits of built-in functions

- Built-in functions are faster and more efficient than writing your own functions.
- Allowing you to perform complex operations with minimal code.

### Functions Cheat Sheet

| Function    | Returns                                                    |
|-------------|------------------------------------------------------------|
| `print()`   | Display an output, e.g., variable's values                 |
| `max()`     | Find the largest value in a data structure                 |
| `min()`     | Find the smallest value in a data structure                |
| `sum()`     | Add up all elements in a data structure                    |
| `round()`   | Trim a float to a specified number of decimal places       |
| `len()`     | Count the number of elements in a data structure           |
| `sorted()`  | Sort elements in a data structure in ascending order       |
| `help()`    | Get information about a function, variable, or value       |

## Modules

### What is a module?

- Modules are Python scripts
  - Files ending with .py extension
  - Contain functions and attributes
  - Can contain other modules
- Python Standard Library
  - Collection of modules that come with Python
  - No need to install them
  - Can be imported and used in your code
- Popular Python Standard Library modules
  - math - mathematical functions
  - random - random number generators
  - datetime - date and time functions
  - os - operating system functions
  - sys - system-specific functions
  - json - JavaScript Object Notation functions
  - csv - Comma Separated Values functions
  - re - regular expression functions
  - collections - advanced data structures types and functions
  - string - string functions
  - logging - log information when testing or running software
  - subprocess - run terminal commands from Python

### Importing modules

- You can import a module using the `import` keyword.

```python
# Importing a module
import math
print(math.pi) # 3.141592653589793
print(type(math)) # <class 'module'>
```

- You can use `help()` function to get information about a module.

```python
# Using help() function
help(math)
```

### os module

- The `os` module provides a way of using operating system dependent functionality.

```python
# Using os module
import os
print(os.getcwd()) # /home/repl
```

- You can use `os` module to list all the files in a directory.

```python
# Listing all files in a directory
import os
print(os.listdir()) # ['data', 'file.py', 'script.py']
```

### Module attributes

- You can use `dir()` function to list all the attributes of a module.

```python
# Listing all attributes of a module
import math
print(dir(math))
```

- Attributes have values
- Functions perform tasks
- Don't use parentheses with attributes

```python
# Using attributes of a module
import os
os.environ
print(os.environ) # {'HOME': '/home/repl', 'SHELL': '/bin/bash', 'USER': '
```

### Importing specific function or multiple functions

- You can import a specific function from a module using the `from` keyword.

```python
# Importing a specific function from a module
from math import pi
print(pi) # 3.141592653589793
```

- You can import multiple functions from a module using the `from` keyword.

```python
# Importing multiple functions from a module
from math import pi, sqrt
print(pi) # 3.141592653589793
print(sqrt(25)) # 5.0
```

## Packages

### What is a package?

- Packages are directories containing modules. Also called libraries.
- Packages can contain sub-packages.
- Packages can contain modules.
- Packages can contain attributes and functions.
- Dowlnoad and install packages using pip.
- Popular packages
  - NumPy - numerical computing
  - Pandas - data manipulation and analysis
  - Matplotlib - data visualization
  - Scikit-learn - machine learning
  - TensorFlow - deep learning
  - Keras - deep learning
  - OpenCV - computer vision
  - NLTK - natural language processing
  - Flask - web development
  - Django - web development

### Installing packages

- You can install packages using `pip` command.

```bash
pip install package_name
```

- You can install a specific version of a package using `pip` command.

```bash
pip install package_name==version
```

### Importing packages

- You can import a package using the `import` keyword.

```python
# Importing a package
import numpy
print(numpy.__version__) # 1.16.4
```

- You can import a package using an alias.

```python
# Importing a package using an alias
import numpy as np
print(np.__version__) # 1.16.4
```

### Functions versus methods

- Function = code to perform a task
- Method = function that is specific to a data type
- Functions are called using the function name
- Methods are called using the dot notation

```python
# Function
import math
print(math.sqrt(25)) # 5.0

# Method
import numpy as np
numbers = [1, 2, 3, 4, 5]
print(np.mean(numbers)) # 3.0
```

## Custom Functions

### Create custom functions

- Considerations for making a custom function
  - Number of lines
  - Code complexity
  - Freqyenct of use
  - DRY principle (Don't Repeat Yourself)
  - Code readability

- You can create a custom function using the `def` keyword.

```python
# Creating a custom function
def greet():
    print('Hello, World!')

greet() # Hello, World!
```

- You can create a custom function with parameters.

```python
# Creating a custom function with parameters
def greet(name):
    print(f'Hello, {name}!')

greet('Alice') # Hello, Alice!
```

- Storing the result of a function in a variable.

```python
# Storing the result of a function in a variable
def greet(name):
    return f'Hello, {name}!'

greeting = greet('Alice')
print(greeting) # Hello, Alice!
```

## Default and keyword arguments

### Arguments

- Arguments are values passed to a function. They are used to perform a task.
- There is two types of arguments:
  - Positional arguments
    - Provided in the order they are expected. Separated by commas.
    - Useful for simplicity and readability.
    - `value` syntax.
  - Keyword arguments
    - Provided with a keyword and an equals sign. Separated by commas.
    - Useful for interpretaton, readability, flexibility, and tracking.
    - `keyword=value` syntax.

- You can use default arguments in a function.

```python
# Using default arguments
def greet(name='World'):
    return f'Hello, {name}!'
print(greet()) # Hello, World!
print(greet('Alice')) # Hello, Alice!
```

- We use default arguments to help us think about likely uses for our function
  - Commonnly used value - set it using a default argument
- Potentially reduces code for users (if they don't need to specify the argument)
- Maintains flexibility for users

- You can use keyword arguments in a function.

```python
# Using keyword arguments
def greet(name='World', greeting='Hello'):
    return f'{greeting}, {name}!'
print(greet()) # Hello, World!
print(greet('Alice', 'Greetings')) # Greetings, Alice!
print(greet(greeting='Greetings', name='Alice')) # Greetings, Alice!
```

## Docstrings

### What is a docstring?

- String (block of text) describing a function, method, class, or module
- Help users understand what the code does, how to use it, and what to expect
- Enclosed in triple quotes (single or double). Should be triple quotes.
- Placed immediately after the definition of a function, method, class, or module

- You can use docstrings to document your custom functions.

```python
# Using docstrings
def greet(name='World'):
    """
    This function greets a person.

    Parameters:

    name (str): The name of the person.

    Returns:

    str: The greeting.
    """
    return f'Hello, {name}!'
```

- You can use `help()` function to get information about a function.

```python
# Using help() function
help(greet) # This function greets a person.
```

- You can use `__doc__` attribute to get information about a function.

```python
# Using __doc__ attribute
print(greet.__doc__) # This function greets a person.
```

- Update the docstring of the function.

```python
# Updating the docstring of the function
greets.__doc__ = 'This function greets a person using their name.'
print(greet.__doc__) # This function greets a person using their name.
```

##  Arbitrary Arguments

### Limitations of Defined Arguments

- Defined arguments are useful for functions with a fixed number of arguments. But what if you don't know how many arguments you need?
- You can use arbitrary arguments to pass a variable number of arguments to a function.

### Arbitrary Argument

- Docstrings help clarify how to use a function.
- Arbitrary arguments are useful when you don't know how many arguments you need. They allow functions to accept any number of arguments.
- Arbitrary arguments are defined using an asterisk (*) before the parameter name. Conventional name is `*args`. You can use any name.
- Arbitrary arguments are stored in a tuple.

```python
# Using arbitrary arguments
def greet(*names):
    for name in names:
        print(f'Hello, {name}!')

greet('Alice', 'Bob', 'Charlie') # Hello, Alice! Hello, Bob! Hello, Charlie!
```

- You can use one args argument in a function.

```python
# Using one args argument in a function
def greet(*names):
    for name in names:
        print(f'Hello, {name}!')

greet(*['Alice', 'Bob', 'Charlie']) # Hello, Alice! Hello, Bob! Hello, Charlie!
```

### Arbitrary Keyword Arguments

- Arbitrary keyword arguments are useful when you don't know how many keyword arguments you need. They allow functions to accept any number of keyword arguments.
- Arbitrary keyword arguments are defined using two asterisks (**) before the parameter name. Conventional name is `**kwargs`. You can use any name.
- Arbitrary keyword arguments are stored in a dictionary.

```python
# Using arbitrary keyword arguments
def greet(**names):
    for key, value in names.items():
        print(f'{key} is {value} years old.')

greet(Alice=24, Bob=30, Charlie=35) # Alice is 24 years old. Bob is 30 years old. Charlie is 35 years old.
```

- You can use one kwargs argument in a function.

```python
# Using one kwargs argument in a function
def greet(**names):
    for key, value in names.items():
        print(f'{key} is {value} years old.')

greet(**{'Alice': 24, 'Bob': 30, 'Charlie': 35}) # Alice is 24 years old. Bob is 30 years old. Charlie is 35 years old.
```

## Recap of Learning

- You learned about the flexibility of Python functions, specifically through the use of arbitrary arguments. This allows functions to accept any number of positional arguments (*args) or keyword arguments (**kwargs), making your functions adaptable to various inputs. Here are the key points:

- Arbitrary Positional Arguments: By prefixing a parameter with an asterisk (*), you can pass any number of positional arguments to a function. These arguments are accessed within the function as a tuple. For example, defining a function concat(`*args`) enables it to concatenate any number of strings passed to it.

- Arbitrary Keyword Arguments: Similarly, by using two asterisks (**) before a parameter, a function can accept any number of keyword arguments. Inside the function, these are treated as a dictionary, allowing for flexible data handling. Modifying the concat function to concat(`**kwargs`) lets it concatenate strings based on keyword arguments.

- Here's a practical example of using arbitrary positional arguments:

```python
  def concat(*args):
    result = ""
    for arg in args:
      result += " " + arg
    return result

  print(concat("Python", "is", "great!"))
```

- This lesson emphasized the importance of designing functions that can handle a variety of input types and quantities, enhancing the reusability and flexibility of your code.

## Lambda Functions

### What is a lambda function?

- Lambda functions are small, anonymous functions. They can have any number of arguments but only one expression.
- Lambda functions are defined using the `lambda` keyword.
- Lambda functions are used when you need a simple function for a short period of time.

- You can create a lambda function.

```python
# Creating a lambda function
print((lambda x, y: x + y)(5, 3)) # 8
```

- Convention is to use x for a single argument lambda function.
- The expression is the equivalent of the function body.
- No return statement is required.
- Store it and call it like a regular function.

- You can store a lambda function in a variable.

```python
# Creating a lambda function
add = lambda x, y: x + y
print(add(5, 3)) # 8
```

- Multiple arguments can be passed to a lambda function.

```python
# Creating a lambda function with multiple arguments
print((lambda x, y, z: x + y + z)(5, 3, 8)) # 16
```

- map() function can be used to apply a lambda function to a list.

```python
# Using map() function with a lambda function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) # [1, 4, 9, 16, 25]
```

- filter() function can be used to filter a list using a lambda function.

```python
# Using filter() function with a lambda function
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even) # [2, 4]
```

- reduce() function can be used to reduce a list using a lambda function.

```python
# Using reduce() function with a lambda function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total) # 15
```

### Custom vs. Lambda Functions

| Scenario | Function Type |
|----------|---------------|
| Complex task | Custom function |
| Same task multiple times | Custom function |
| Short task | Lambda function |
| One-time task | Lambda function |

## Introduction to Errors

### What is an error?

- An error is an unexpected event that occurs when a program is running. Code that violates one or more rules is called an error.
- Error = Exception = Bug.
- Common errors:
  - TypeError: An operation is performed on the wrong data type.
  - ValueError: A function receives the right type but an inappropriate value.
  - SyntaxError: Code violates Python syntax rules.
  - NameError: A variable is not defined.
  - ZeroDivisionError: Division by zero occurs.
  - FileNotFoundError: A file is not found.

###  Code in Packages

- Packages contain other people's code e.g., custom functions
- Known as source code
- `pip install <package>` - downloads source code to our local environment
- The pandas' `pd.read_csv()` function executes the code written for that custom function behind the scenes
- If the code contains an error, it will raise an exception

## Handling Errors

### What is error handling?

- Error handling is the process of responding to errors in a program. It allows a program to continue running even if an error occurs.
- We can use control flow (if, elif, else) to handle some errors. But we can't predict all errors.
- We can write docstring to help users understand how to use a function. But we can't predict all errors.
- We can use try and except blocks to handle errors.
- `try` block is used to test a block of code for errors.
- `except` block is executed if an error occurs in the `try` block.
- `raise` keyword is used to raise an exception.
- `finally` block is executed regardless of whether an error occurs.

- You can use try and except blocks to handle errors.

```python
# Using try and except blocks
try:
    print(5 / 0)
except ZeroDivisionError:
    print('Cannot divide by zero!')
```

- You can use raise keyword to raise an exception.

```python
# Using raise keyword
try:
    raise ValueError('This is a value error!')
except ValueError as e:
    print(e) # This is a value error!
```

- You can use finally block to execute code regardless of whether an error occurs.

```python
# Using finally block
try:
    print(5 / 0)
except ZeroDivisionError:
    print('Cannot divide by zero!')
finally:
    print('This code will always run!')
```

### try-except vs. raise

| try-except | raise |
|------------|-------|
| Avoid errors being produced | Will produce an error |
| Still execute subsequent code | Avoid executing subsequent code |
