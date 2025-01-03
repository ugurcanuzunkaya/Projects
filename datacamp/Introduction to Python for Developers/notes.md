# Introduction to Python for Developers Course - Datacamp

##  What is Python?

- Open source programming language
- Packages to use other's code to avoid reinventing the wheel
- Syntax resembles English
- Use cases;
  - Task automation
  - Web apps
  - Artificial intelligence (AI)
    - Web scraping
    - Content generation / summarization
    - Image recognition
- Easier to code and develop
- Python is a high-level language
- Python is slow compared to C, C++, Java, etc.

##  How to run Python Code

- Code comments
  - Single line comments: `#`
  - Multi-line comments: `'''` or `"""`
  - It doesn't affect the code execution. It's for the developer to understand the code.

- Calculations
  - Python can be used as a calculator.
  - Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - Order of operations: `()`, `**`, `*`, `/`, `//`, `%`, `+`, `-`
  - Division: `/` returns a float, `//` returns an integer
  - Modulus: `%` returns the remainder of the division
  - Exponentiation: `**` returns the power of a number

- print() function
  - `print()` function is used to display the output.
  - It can take multiple arguments.
  - It can take keyword arguments.
  - It can take a separator argument.
  - It can take an end argument.

## Review

- You learned about the basics of running Python code, including the use of the DataCamp interface for executing Python scripts. You explored how to write and run Python code in both the IPython Shell and script files (.py), understanding the importance of comments for code clarity. Additionally, you discovered how to perform basic arithmetic operations in Python, using it as a powerful calculator. Key points include:

- The IPython Shell allows for immediate execution and output display of Python code.
- Python script files, saved with a .py extension, can be executed to perform tasks, with the print() function used to display outputs.
- Comments, starting with a #, help document the code without affecting its execution.
- Basic arithmetic operations in Python include addition (+), subtraction (-), multiplication (*), and division (/).
- Advanced operations like exponentiation (**) and modulo (%) allow for more complex calculations.
- For example, to perform and print calculations, you used code like this:

```python
# Add 19 and 17
print(19 + 17)

# Calculate nine squared
print(9 ** 2)
```

- This lesson laid the foundation for using Python for various calculations, an essential skill for any programming task.

## Variables and Data Types

### Variables

- `variable_name`- Name of the variable (case-sensetive)
- `=`- For assigning a value
- `value`- The value to assign to the variable
- Example: `customer_age = 25` and `Customer_Age = 25` are different variables.

### Why use Variables

- Avoid having to retype the same information
- Can update variables if conditions change

### Integers

- Whole numbers
- Example: `customer_age = 25`
- No need to tell Python what data type the variable is
- `type()` function can be used to check the data type of a variable

### Floats

- Decimal numbers
- Example: `customer_age = 25.5`

### Strings

- Text data. ' ' or " " can be used to define a string. Don't mix the quotation marks.
- Example: `customer_name = 'John'`

### Booleans

- True or False. `True` and `False` are keywords.
- Example: `customer_age = True` or `customer_age = False`
- `type()` function can be used to check the data type of a variable (e.g. `type(customer_age)` returns `<class 'bool'>`)

### Variable Naming

- Variable names can contain letters, numbers, and underscores.
- Variable names can't start with a number.
- Variable names can't contain spaces.
- Variable names can't be a keyword.
- Variable names should be descriptive. (e.g. `customer_age` instead of `age`)
- Variable names should be lowercase. (e.g. `customer_age` instead of `Customer_Age`)
- Variable names should be separated by underscores. (e.g. `customer_age` instead of `customerage`)

### Case conventions

- `snake_case`: `customer_age`
- `camelCase`: `customerAge`
- `PascalCase`: `CustomerAge`

### Calculations with Variables

- Variables can be used in calculations.
- Example: `total_cost = price * quantity`

## Working with Data Types

### Strings are everywhere

- User profiles
- Search engines
- Large Language Models (LLMs)

### Single and Double Quotes

- Single quotes: `' '`. Used when the string contains a double quote.
- Double quotes: `" "`. Used when the string contains a single quote/apostrophe.
- Triple quotes: `''' '''` or `""" """`. Enhance readability and can be used for multi-line strings. Avoid the need to use special characters. Longer text such as customer reviews. Used to describe what functions do.
- Use double quotes if the string contains a single quote/apostrophe.
- Use triple quotes for multi-line strings.

###  Methods

- Method = a function that is only available for a specific data type.
- `str` methods. `str_variable.method()` - e.g. `customer_name.upper()`

###  Replacing parts of a string

- `str_variable.replace('old', 'new')` - e.g. `customer_name.replace('John', 'Jane')`
- Common cases:
  - Reformatting e.g., change spaces to underscores
  - Fixing or removing typos
  - Replacing a substring with another substring
- `str_variable.upper()` - Converts the string to uppercase
- `str_variable.lower()` - Converts the string to lowercase
- `str_variable.capitalize()` - Capitalizes the first letter of the string
- `str_variable.title()` - Capitalizes the first letter of each word in the string

### Cheat Sheet

| Syntax | Purpose | Example |
| --- | --- | --- |
| Single quotes | Define a string | `customer_name = 'John'` |
| Double quotes | Define a string | `customer_name = "John"` |
| Triple quotes | Define a multi-line string | `customer_review = '''Great service!'''` |
| `str_variable.upper()` | Convert the string to uppercase | `customer_name.upper()` |
| `str_variable.lower()` | Convert the string to lowercase | `customer_name.lower()` |
| `str_variable.capitalize()` | Capitalize the first letter of the string | `customer_name.capitalize()` |
| `str_variable.title()` | Capitalize the first letter of each word in the string | `customer_name.title()` |
| `str_variable.replace('old', 'new')` | Replace a substring with another substring | `customer_name.replace('John', 'Jane')` |

## Lists

### What are Lists?

- List = store multiple values in a single variable
  - Can store different data types in a single list. (e.g. integers, floats, strings, booleans)
- Syntax: `list_name = [value1, value2, value3]`
- Example: `customer_data = ['John', 25, True]`
- Variables can be used in lists. (e.g. `customer_data = [customer_name, customer_age, customer_age]`)
- `type()` function can be used to check the data type of a variable (e.g. `type(customer_data)` returns `<class 'list'>`)
- Lists can be nested. (e.g. `customer_data = [['John', 25, True], ['Jane', 30, False]]`)
- Lists can be empty. (e.g. `customer_data = []`)
- Lists can be accessed by index. (e.g. `customer_data[0]` returns `'John'`)
- Lists are ordered
  - Can use subsetting or indexing
  - Python counts values starting from zero for the first element

### Acessing List Elements

- Indexing: `list_name[index]` - e.g. `customer_data[0]`. - Returns the first element of the list.
- Subsetting: `list_name[start:end]` - e.g. `customer_data[0:2]` - returns the first two elements of the list. [start, end + 1]
- Negative indexing: `list_name[-index]` - e.g. `customer_data[-1]` - returns the last element of the list.
- Slicing: `list_name[start:end:step]` - e.g. `customer_data[0:3:2]` - returns the first and third elements of the list. [start, end + 1, step] - step is optional. Default is 1. If step is negative, the list is returned in reverse order.
- Multiple Elements: `list_name[start:end]` - e.g. `customer_data[:2]` - returns the first two elements of the list. `customer_data[1:]` - returns the second index and all the elements after it.
- Reversing a list: `list_name[::-1]` - e.g. `customer_data[::-1]` - returns the list in reverse order.

## Dictionaries

###  What are Dictionaries?

- Dictionary = store key-value pairs
- Syntax: `dict_name = {'key1': value1, 'key2': value2}` - e.g. `customer_data = {'name': 'John', 'age': 25, 'is_customer': True}`
- Variables can be used in dictionaries. (e.g. `customer_data = {'name': customer_name, 'age': customer_age, 'is_customer': customer_age}`)
- `type()` function can be used to check the data type of a variable (e.g. `type(customer_data)` returns `<class 'dict'>`)
- Dictionaries can be nested. (e.g. `customer_data = {'customer1': {'name': 'John', 'age': 25, 'is_customer': True}, 'customer2': {'name': 'Jane', 'age': 30, 'is_customer': False}}`)
- Dictionaries can be empty. (e.g. `customer_data = {}`)
- Dictionaries can be accessed by key. (e.g. `customer_data['name']` returns `'John'`)
- Dictionaries are ordered
  - Allows values to be accessed by subsetting on the key
  - Can use keys to access values
  - Keys are unique
  - Keys can be strings, integers, or floats
- `dict_name.keys()` - returns the keys of the dictionary
- `dict_name.values()` - returns the values of the dictionary
- `dict_name.items()` - returns the key-value pairs of the dictionary
- `dict_name.get('key')` - returns the value of the key. If the key doesn't exist, it returns `None`.
- `dict_name.get('key', 'default')` - returns the value of the key. If the key doesn't exist, it returns the default value.
- `dict_name["new_key"] = new_value` - adds a new key-value pair to the dictionary.
- `dict_name["key"] = new_value` - updates the value of the key in the dictionary.
- Not accept duplicate keys. If a key is duplicated, the last value is used.

### Sets and Tuples

### Sets

- Set = store unique values. Unchangeable (you can add or remove values but you can't change them).
- Ideal to identify and remove duplicates.
- Quick to search (compared to other data structures such as lists).
- Syntax: `set_name = {value1, value2, value3}` - e.g. `customer_data = {'John', 25, True}`
- Variables can be used in sets. (e.g. `customer_data = {customer_name, customer_age, customer_age}`)
- `type()` function can be used to check the data type of a variable (e.g. `type(customer_data)` returns `<class 'set'>`)
- Sets can be empty. (e.g. `customer_data = set()`)
- Lists can be converted to sets. (e.g. `customer_data = set(['John', 25, True])`)
- Don't have an index. Can't be indexed or sliced. Can't have duplicates.
- Sets are unordered. The order of the elements is not guaranteed. You can use the `sorted()` function to sort the set. (e.g. `sorted(customer_data)`) - returns a list.

### Tuples

- Tuple = store multiple values in a single variable. Immutable (unchangeable). Ordered.
- Can subset with indexing and slicing.
- Syntax: `tuple_name = (value1, value2, value3)` - e.g. `customer_data = ('John', 25, True)`
- Variables can be used in tuples. (e.g. `customer_data = (customer_name, customer_age, customer_age)`)
- `type()` function can be used to check the data type of a variable (e.g. `type(customer_data)` returns `<class 'tuple'>`)
- Tuples can be nested. (e.g. `customer_data = (('John', 25, True), ('Jane', 30, False))`)
- Tuples can be empty. (e.g. `customer_data = ()`)
- Tuples can be accessed by index. (e.g. `customer_data[0]` returns `'John'`)

## Conditional Statements and Operators

###  Booleans

- Booleans = True or False. Used to make comparisons.

### Comparison Operators

- Comparison operators
  - Symbols or combinations of symbols that compare values
  - Used to compare things
  - Similar to symbols for calculations such as `+`, `-`, `*`, `/` etc.
- Comparison operators
  - `==` - Equal to. Ex: `customer_age == 25`
  - `!=` - Not equal to. Ex: `customer_age != 25`
  - `>` - Greater than. Ex: `customer_age > 25`
  - `<` - Less than. Ex: `customer_age < 25`
  - `>=` - Greater than or equal to. Ex: `customer_age >= 25`
  - `<=` - Less than or equal to. Ex: `customer_age <= 25`
- You can use for strings as well. (e.g. `customer_name == 'John'`) - returns `True` or `False`. (`"John" > "Jane"`) - compares the alphabetical order of the strings.

### Conditional Statements

- If True perform an action, else perform another action.
- Syntax:

```python
if condition:
  action
else:
  another_action
```

- Indentation is important in Python. It's used to define the scope of the code block.
- If, elif, else statements can be used to check multiple conditions. (e.g. `if customer_age == 25:` `elif customer_age == 30:` `else:`)

##  For Loops

### What are For Loops?

- For loop = iterate over a sequence (e.g. list, tuple, set, dictionary, string)
- Syntax:

```python
for item in sequence:
  action
```

- sequence = list, tuple, set, dictionary, string. iterable object.
- value = variable that represents the value of the element in the sequence. Placeholder. Can be any name. (e.g. `for customer in customers:`). Generally it is `i`.
- action = code block that is executed for each element in the sequence. Indentation is important.
- `range()` function can be used to generate a sequence of numbers. (e.g. `for i in range(5):`). `range(1, 10, 2)` - returns `[1, 3, 5, 7, 9]`. start, end, step. start is optional. Default is 0. step is optional. Default is 1.
- `enumerate()` function can be used to get the index and value of the elements in the sequence. (e.g. `for i, customer in enumerate(customers):`) - returns the index and value of the elements in the sequence.
- You can use `break` to exit the loop. (e.g. `for customer in customers:` `if customer == 'John':` `break`)
- You can use `continue` to skip the current iteration and continue with the next iteration. (e.g. `for customer in customers:` `if customer == 'John':` `continue`)
- You can iterate over a dictionary. (e.g. `for key, value in customer_data.items():`). Strings are iterable objects. (e.g. `for letter in 'John':`). Lists are iterable objects. (e.g. `for number in [1, 2, 3]:`)
- You can use conditional statements in for loops. (e.g. `for customer in customers:` `if customer == 'John':` `print('Found John!')`)
- You can use nested for loops. (e.g. `for customer in customers:` `for product in products:` `print(customer, product)`). Not recommended for large datasets.

## While Loops

### What are While Loops?

- While loop = execute a block of code as long as a condition is True. Used when you don't know how many times you need to loop.
- Similar to if statements but the code block is executed multiple times.
- Syntax:

```python
while condition:
  action
```

- condition = expression that is evaluated to True or False. If True, the code block is executed. If False, the loop stops.
- action = code block that is executed as long as the condition is True. Indentation is important.
- You can use `break` to exit the loop. (e.g. `while True:` `if customer == 'John':` `break`)
- You can use `continue` to skip the current iteration and continue with the next iteration. (e.g. `while True:` `if customer == 'John':` `continue`)
- Any continuous condition can be used. (e.g. `while customer_age < 30:`)
- Be careful with infinite loops. Make sure the condition will eventually be False. If you enter an infinite loop, you can stop the code execution by pressing Control + C or Command + C in the terminal.
- You can use conditional statements in while loops. (e.g. `while customer_age < 30:` `print('Customer is under 30!')` `customer_age += 1`)

##  Building Workflows

###  Complex Workflows

- Loops through data structures
  - `for`, `while`
- Evaluate multiple conditions
  - `if`, `elif`, `else`, `>`, `<`, `==`, `!=`, `>=`, `<=`
- Update variables
  - `+=`, `-=`, `*=`, `/=`, `//=`, `%=`
- Return outputs
  - `print()`, `return`

### The `in` Operator

- `in` operator = check if a value is in a sequence. (e.g. `if customer in customers:`)
- Can be used with strings, lists, tuples, sets, dictionaries, etc.
- Can be used with conditional statements. (e.g. `if customer in customers:` `print('Found John!')`)

###  The `not` Operator

- `not` operator = check if a value is not in a sequence. (e.g. `if customer not in customers:`)
- Can be used with strings, lists, tuples, sets, dictionaries, etc.
- Can be used with conditional statements. (e.g. `if customer not in customers:` `print('John is not in the list!')`)

###  The `and` Operator

- `and` operator = check if multiple conditions are True. (e.g. `if customer in customers and customer_age == 25:`)
- Can be used with conditional statements. (e.g. `if customer in customers and customer_age == 25:` `print('Found John!')`)
- Both conditions must be True for the code block to be executed.

###  The `or` Operator

- `or` operator = check if at least one condition is True. (e.g. `if customer in customers or customer_age == 25:`)
- Can be used with conditional statements. (e.g. `if customer in customers or customer_age == 25:` `print('Found John!')`)
- At least one condition must be True for the code block to be executed.

###  Adding/Subtracting from Variables

- Combine keywords with operators to update variables. (e.g. `customer_age += 1`)
- `+=` - Add a value to a variable. (e.g. `customer_age += 1`)
- `-=` - Subtract a value from a variable. (e.g. `customer_age -= 1`)

###  Appending

- Store information that meets specific criteria in a list. (e.g. `if customer_age < 30:` `young_customers.append(customer)`)

## Next Steps

- Additional built-in functions
  - `zip()`, `len()`, `sum()`, `min()`, `max()`, `sorted()`, `reversed()`

- Packages and modules
  - `os`, `time`, `venv`, `pandas`, `requests`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `tensorflow`, `keras`

- Building custom functions
