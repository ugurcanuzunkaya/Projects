# Days 13 - 20: Python Mega Course

## Day 13 Summary

## Default Arguments in Python

### Brief Summary

Default arguments in Python allow functions to have pre-set parameter values, reducing the need for explicit argument passing. This simplifies function calls and helps avoid errors.

### Key Points

- **Default Arguments**: Pre-set values for function parameters, making some arguments optional.
- **Coffee Analogy**: Ordering coffee without specifying "in a cup" parallels using default arguments.
- **Example Usage**:
  - Function definition: `def get_todos(filepath='todos.txt')`
  - Call without argument: `get_todos()`
  - Call with new value: `get_todos('todos1.txt')`
- **Changing Default Values**: Specify new values in function calls as needed.
- **Error Handling**: Ensure correct argument order and provide necessary arguments.
- **Best Practices**: Use default arguments to simplify code and reduce redundancy.

## Using Docstrings in Python

### Brief Summary - 1

Docstrings are strings that document what a function does, placed at the beginning of the function within triple quotes. They provide in-code documentation accessible via the `help()` function.

### Key Points - 1

- **Docstrings**: Document the purpose of a function.
- **Viewing Docstrings**: Use `help(function_name)` to see the docstring and details.
- **Creating Docstrings**:
  - Short description for simple functions.
  - Detailed explanation for complex functions.
- **Benefits**:
  - **For Others**: Helps understand the function without reading the code.
  - **For Yourself**: Reminds you of the function's purpose when revisiting code.
- **Practical Example**:

  ```python
  def get_todos(filepath='todos.txt'):
      """
      Read a text file and return the list of to-do items.
      """
      # function code here
  help(get_todos)
  ```

## Docstrings and Multi-line Strings in Python

### Brief Summary - 2

Docstrings are used for documentation within functions, while multi-line strings, written with triple quotes, can span multiple lines and are useful for storing large text blocks.

### Key Points - 2

- **Docstrings**: Document functions, using triple quotes.
- **Multi-line Strings**: Store large text blocks, maintaining line breaks without special characters.
- **Comparison with Normal Strings**:
  - Normal strings need `\n` for line breaks.
  - Multi-line strings preserve formatting.
- **Practical Example**:

  ```python
  text = """
  This is a multi-line string.
  It retains line breaks.
  """
  print(text)
  ```

## Decoupling Functions in Python

### Brief Summary - 3

Decoupling functions involves breaking down functions to ensure each performs a single task. This enhances code readability, reusability, and maintainability.

### Key Points - 3

- **Overview**: Functions should focus on a single responsibility.
- **Example Scenario**: Decoupling a function that converts feet and inches to meters.
- **Strategy**:
  - **Parsing Input**: `parse` function extracts feet and inches.
  - **Converting to Meters**: `convert` function converts values to meters.
  - **Integration**: Combine `parse` and `convert` for complete functionality.
- **Benefits**:
  - **Modularity**: Easier to understand and maintain.
  - **Testing**: Functions can be tested independently.
  - **Readability**: Cleaner and more understandable code.

## Understanding Python Versions

### Brief Summary - 4

Understanding Python versions involves knowing the differences between major, minor, and patch releases, and their implications for backward compatibility and code maintenance.

### Key Points - 4

- **Major Releases**: Significant changes, not backward compatible (e.g., Python 2 vs. Python 3).
- **Minor/Patch Releases**: New features and bug fixes, backward compatible within the same major version.
- **Backward Compatibility**: Code runs on newer versions without changes (within the same major version).
- **Practical Implications**:
  - **Maintaining Legacy Code**: Run old code with the appropriate interpreter.
  - **Upgrading**: Modify code for new syntax and use the latest interpreter.
- **Practical Example**:

  ```python
  # Old Python 2 code
  print "Hello"
  raw_input("Enter something: ")

  # Updated Python 3 code
  print("Hello")
  input("Enter something: ")
  ```

Let's add the information about splitting code into multiple modules to the summary.

## Day 14 Summary

## Organizing Code with Functions and Modules

### Brief Summary - 5

Today's lesson focused on the importance of organizing and structuring code using functions and modules for better maintainability and scalability. This practice is essential for keeping code clean and manageable, especially as projects grow in complexity.

### Key Points - 5

- **Improving Code Base**: Use functions to create modular and organized code.
- **Analogy**: Similar to a barista making coffee in a separate space to avoid mess, separate code processes into different files or modules.

### Steps to Separate Functions into Modules

1. **Create a New Python File**: Create a new file, e.g., `functions.py`, in the same directory as `main.py`.
2. **Move Functions to the New File**: Cut and paste functions from `main.py` to `functions.py`.
3. **Update `main.py`**: Import the functions from `functions.py`.

### Import Methods

- **Specific Imports**:

  ```python
  from functions import get_todos, write_todos
  ```

  - Directly use functions: `get_todos()`, `write_todos()`.
- **Module Import**:

  ```python
  import functions
  ```

  - Use functions with module name: `functions.get_todos()`, `functions.write_todos()`.

### Example Code

- **functions.py**:

  ```python
  def get_todos(filepath='todos.txt'):
      with open(filepath, 'r') as file:
          todos = file.readlines()
      return todos

  def write_todos(todos, filepath='todos.txt'):
      with open(filepath, 'w') as file:
          file.writelines(todos)
  ```

- **main.py** (using specific imports):

  ```python
  from functions import get_todos, write_todos

  todos = get_todos()
  todos.append("New task\n")
  write_todos(todos)
  ```

- **main.py** (using module import):

  ```python
  import functions

  todos = functions.get_todos()
  todos.append("New task\n")
  functions.write_todos(todos)
  ```

### Choosing Import Methods

- **Few Functions**: Use specific imports for simplicity.
- **Many Functions**: Use module import to avoid long import lists.

### Creating Directories for Modules

- **Organizing Modules**:
  - Create a directory, e.g., `modules`, to store related files.
  - Update import statements to reflect the new structure.

- **Example**:

  ```python
  from modules.functions import get_todos, write_todos
  ```

- **Directory Structure**:

  ```bash
  project/
    main.py
    modules/
      functions.py
  ```

- **Updated import in `main.py`**:

  ```python
  from modules.functions import get_todos, write_todos
  ```

### Summary

- **Benefits**: Organizing code into modules improves readability and maintainability.
- **Best Practices**: Separate large programs into logical parts using functions and modules.

## Understanding the Anatomy of Python: Classes and Instances

### Brief Summary - 6

The lesson introduced the concept of classes and instances in Python, emphasizing their importance in object-oriented programming. Understanding the distinction between classes (blueprints) and instances (specific realizations) is crucial for effective coding.

### Key Points - 6

- **Program as a Cafe Analogy**: Functions in a program are like actions in a cafe.
- **Functions and Data Types (Classes)**: Functions perform tasks; classes are blueprints for creating objects.
- **Instances vs. Abstract Concepts**: Classes are abstract concepts; instances are specific realizations.
- **Methods**: Functions associated with objects (e.g., `append` for lists).
- **Variables**: Store instances of objects.

### Designing Classes

- **Creating New Classes**: Programmers can design new classes.
- **Using Existing Classes**: Utilize pre-defined classes like lists, dictionaries, and strings.

### Key Takeaways

- **Understanding Classes and Instances**: Classes define structure and behavior; instances are specific realizations.
- **Methods and Functions**: Methods are functions associated with instances of classes.
- **Variables and Data Storage**: Variables store instances for manipulation and access.

### Summary - 6

- **Anatomy of Python**: Distinguish between classes and instances to work effectively with Python.

## Understanding Modules and the `if __name__ == "__main__"` Idiom

### Brief Summary - 7

The lesson explored how Python modules are executed and how to control code execution using the `if __name__ == "__main__"` idiom. This helps manage code that should only run when a script is executed directly, not when imported as a module.

### Key Points - 7

- **Module Execution**: Importing a module executes the entire script.
- **Controlling Code Execution with `if __name__ == "__main__"`**: Ensures certain code runs only when the script is executed directly.

### Experiment 1: Printing from a Module

1. **Add a Print Statement in `functions.py`**:

   ```python
   print("Hello from functions")
   ```

2. **Run `main.py`** and observe the print statement.

### Experiment 2: Introducing an Error

1. **Add an Error in `functions.py`**:

   ```python
   print(x)  # x is not defined
   ```

2. **Run `main.py`** and observe the error traceback.

### Using `if __name__ == "__main__"`

- **Adding the Conditional Block**:

  ```python
  if __name__ == "__main__":
      print("Hello from functions")
  ```

- **Explanation**: `__name__` is set to `"__main__"` when a script is run directly.

### Practical Uses

- **Running `functions.py` Directly**:

  ```bash
  python functions.py
  ```

- **Running `main.py`**:

  ```bash
  python main.py
  ```

### Summary - 7

- **Understanding Module Execution**: Importing a module executes its code.
- **Using `if __name__ == "__main__"`: Control code execution based on how the script is run.

## Splitting Code into Multiple Modules

### Brief Summary - 8

The lesson covered how to split functions into separate modules to improve code structure, maintainability, and scalability. This approach helps manage large codebases more efficiently by organizing functions into logical units.

### Key Points - 8

- **Improving Code Structure**: Organize functions into separate files for better maintainability and scalability.
- **Example Scenario**: Script to convert user input (feet and inches) to meters and check if a kid can use a slide based on their height.

### Steps to Split Functions into Separate Modules

1. **Create a Directory for Modules**: Create a directory, e.g., `bonus`, to store script and module files. Place the main script file (`Bonus14.py`) in this directory.
2. **Move Functions to Separate Files**: Create separate files for parsing and converting functions.

#### Moving the Parse Function

1. **Refactor Parse Function**: Use a refactoring tool to move the parse function to a new file (`parsers14.py`).
2. **Manual Refactoring**:
   - Create `parsers14.py` and move the parse function code to this file.
   - Update `Bonus14.py` to import the parse function:

     ```python
     from parsers14 import parse
     ```

3. **`parsers14.py` File**:

   ```python
   def parse(feet_inches):
       parts = feet_inches.split()
       feet = float(parts[0])
       inches = float(parts[1])
       return {'feet': feet, 'inches': inches}
   ```

#### Moving the Convert Function

1. **Refactor Convert Function**: Use a refactoring tool to move the convert function to a new file (`converters14.py`).
2. **Manual Refactoring**:
   - Create `converters14.py` and move the convert function code to this file.
   - Update `Bonus14.py` to import the convert function:

     ```python
     from converters14 import convert
     ```

3. **`converters14.py` File**:

   ```python
   def convert(feet, inches):
       meters = feet * 0.3048 + inches * 0.0254
       return meters
   ```

#### Updating the Main Script

- **Updated `Bonus14.py`**:

  ```python
  from parsers14 import parse
  from converters14 import convert

  def main():
      feet_inches = input("Enter feet and inches (e.g., 3 12): ")
      parsed = parse(feet_inches)
      result = convert(parsed['feet'], parsed['inches'])
      print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result:.2f} meters")
      if result < 1:
          print("The kid cannot use the slide.")
      else:
          print("The kid can use the slide.")

  if __name__ == "__main__":
      main()
  ```

#### Running the Script

- **Run the Main Script**:

  ```bash
  python Bonus14.py
  ```

### Benefits of Splitting Code

- **Modularity**: Functions are organized into logical units, making the codebase easier to manage and extend.
- **Maintainability**: Clear separation of concerns; parsing and converting functions are in their respective files.
- **Scalability**: Adding new functions becomes straightforward without cluttering the main script.

### Conclusion

- **Organizing Code**: Splitting functions into separate modules improves code clarity and maintainability.
- **Practical Example**: Demonstrated how to refactor a script by moving functions to separate modules.

By following these steps, you can create a well-organized, modular Python project that is easier to maintain and extend.

## Introduction to Version Control and Git

### Brief Summary - 9

The lesson introduced version control and Git, highlighting the importance of tracking changes in code, collaborating with others, and maintaining a history of changes. Git and GitHub are essential tools for managing and sharing code effectively.

### Key Points - 9

- **Version Control**: Practice of tracking and managing changes in code.
- **Problems Without Version Control**: Difficult to undo changes, error-prone manual management.
- **Version Control Systems**: Git is the most popular, others include Apache Subversion, Bazaar, and Mercurial.

### Benefits of Using Git

- **Tracking Changes**: Easily revert to previous versions and view change history.
- **Collaboration**: Multiple people can work on the same codebase simultaneously.
- **Backup and Sharing**: Code can be backed up and shared via platforms like GitHub.

### Git and GitHub

- **Git**: Local version control system for tracking changes.
- **GitHub**: Cloud-based platform for hosting Git repositories, providing collaboration tools.

### Practical Example of Git in Action

1. **Viewing Changes in a Project**: Use Git to view history and compare versions.
2. **Comparing Code Versions**: Highlight differences between versions.

### Using Git and GitHub

- **Setting Up Git**: Install Git and initialize a repository.
- **Committing Changes**: Commit changes with meaningful messages.
- **Pushing to GitHub**: Push commits to GitHub for backup and sharing.

### Summary - 9

- **Version Control**: Essential for managing code changes, collaboration, and backup.
- **GitHub**: Complements Git by offering cloud-based collaboration and sharing capabilities.

By mastering version control with Git and GitHub, you can effectively manage your code, collaborate with others, and ensure your projects are backed up and easily shareable.
![image.png](attachment:image.png)

## Day 15 Summary

## Adding Date and Time to User Output

### Brief Summary - 10

Today's lesson focused on enhancing the user output in Python applications by adding the current date and time using the `time` module. This provides users with timely context and helps in logging events accurately.

### Key Points - 10

- **Objective**: Add the current date and time to the user output.
- **Using the `time` Module**: Import the `time` module and use the `strftime` function to format the current date and time.

### Step-by-Step Implementation

1. **Import the `time` Module**:

   ```python
   import time
   ```

2. **Get the Current Date and Time**:

   ```python
   current_time = time.strftime("%Y-%m-%d %H:%M:%S")
   ```

3. **Print the Date and Time**:

   ```python
   print(f"It is now {current_time}")
   ```

4. **Complete Example**:

   ```python
   import time
   from parsers14 import parse
   from converters14 import convert

   def main():
       current_time = time.strftime("%Y-%m-%d %H:%M:%S")
       print(f"It is now {current_time}")

       feet_inches = input("Enter feet and inches (e.g., 3 12): ")
       parsed = parse(feet_inches)
       result = convert(parsed['feet'], parsed['inches'])
       print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result:.2f} meters")
       if result < 1:
           print("The kid cannot use the slide.")
       else:
           print("The kid can use the slide.")

   if __name__ == "__main__":
       main()
   ```

### Understanding `strftime` Format Codes

- **Common Format Codes**:
  - `%Y`: Year with century (e.g., 2024)
  - `%m`: Month as a zero-padded decimal number (01-12)
  - `%d`: Day of the month as a zero-padded decimal number (01-31)
  - `%H`: Hour (24-hour clock) as a zero-padded decimal number (00-23)
  - `%M`: Minute as a zero-padded decimal number (00-59)
  - `%S`: Second as a zero-padded decimal number (00-59)

### Using Constants in Modules

1. **Defining Constants**:

   ```python
   FILEPATH = "todos.txt"

   def get_todos(filepath=FILEPATH):
       with open(filepath, 'r') as file:
           todos = file.readlines()
       return todos

   def write_todos(todos, filepath=FILEPATH):
       with open(filepath, 'w') as file:
           file.writelines(todos)
   ```

2. **Benefits of Using Constants**:
   - Easy to update: Change the value in one place.
   - Improve readability: Clear what the constant represents.

### Refreshing the Python Console

- Restart the Python console to see changes after updating a module.

### Summary - 10

- **Using the `time` Module**: Format and display the current date and time in your application.
- **Using Constants**: Define constants for file paths and other fixed values to simplify maintenance.

## Exploring Useful Python Modules

### Key Modules

1. **`glob`**: Used for finding files and directories that match a specified pattern.
2. **`csv`**: Provides functionality to read from and write to CSV files.
3. **`shutil`**: Offers a collection of high-level file operations like copying and archiving.
4. **`webbrowser`**: Enables launching web browsers to open URLs.

### Experiment 1: Using the `glob` Module

1. **Create a Python Script (`e1.py`)**:

   ```python
   import glob

   myfiles = glob.glob("Files/*.txt")
   print(myfiles)

   for filepath in myfiles:
       with open(filepath, 'r') as file:
           print(file.read())
   ```

2. **Run the Script**:

   ```bash
   python e1.py
   ```

### Experiment 2: Using the `csv` Module

1. **Create a Python Script (`e2.py`)**:

   ```python
   import csv

   with open('weather.csv', 'r') as file:
       data = list(csv.reader(file))

   print(data)

   city = input("Enter city: ")

   for row in data[1:]:
       if row[0] == city:
           print(f"The temperature in {city} is {row[1]}")
   ```

2. **Run the Script**:

   ```bash
   python e2.py
   ```

### Experiment 3: Using the `shutil` Module

1. **Create a Python Script (`e3.py`)**:

   ```python
   import shutil

   shutil.make_archive("output", "zip", "Files")
   ```

2. **Run the Script**:

   ```bash
   python e3.py
   ```

### Experiment 4: Using the `webbrowser` Module

1. **Create a Python Script (`e4.py`)**:

   ```python
   import webbrowser

   user_term = input("Enter a search term: ").replace(" ", "+")
   url = f"https://www.google.com/search?q={user_term}"
   webbrowser.open(url)
   ```

2. **Run the Script**:

   ```bash
   python e4.py
   ```

### Summary - 11

- **`glob`**: Useful for finding files matching a specific pattern.
- **`csv`**: Essential for handling CSV files, reading data, and processing it.
- **`shutil`**: Great for file operations like copying and archiving.
- **`webbrowser`**: Enables interaction with web browsers, such as opening URLs for searches.

## Building a Quiz App with JSON in Python

### Brief Summary - 12

The lesson focused on building a quiz application that reads questions from a JSON file, allows the user to answer them, and evaluates the answers.

### Steps to Implement the Quiz App

1. **Create the JSON File**:

   ```json
   [
     {
       "question_text": "What are dolphins?",
       "alternatives": [
         "Amphibians",
         "Fish",
         "Mammals",
         "Birds"
       ],
       "correct_answer": 3
     },
     {
       "question_text": "What occupies most of the Earth's surface?",
       "alternatives": [
         "Land",
         "Water"
       ],
       "correct_answer": 2
     }
   ]
   ```

2. **Load and Parse the JSON Data**:

   ```python
   import json

   def load_questions(filename):
       with open(filename, 'r') as file:
           content = file.read()
           data = json.loads(content)
       return data

   questions = load_questions('questions.json')
   ```

3. **Build the Quiz Application**:

   ```python
   score = 0

   for question in questions:
       print(question['question_text'])
       for index, alternative in enumerate(question['alternatives'], 1):
           print(f"{index}. {alternative}")
       user_choice = int(input("Enter your answer: "))

       question['user_choice'] = user_choice

       if user_choice == question['correct_answer']:
           score += 1

   print(f"Your score is {score} out of {len(questions)}")
   ```

4. **Display Results**:

   ```python
   for index, question in enumerate(questions, 1):
       result = "Correct answer" if question['user_choice'] == question['correct_answer'] else "Wrong answer"
       print(f"Question {index}: {result}")
       print(f"Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}")
   ```

### Full Example Code

```python
import json

def load_questions(filename):
    with open(filename, 'r') as file:
        content = file.read()
        data = json.loads(content)
    return data

def main():
    questions = load_questions('questions.json')
    score = 0

    for question in questions:
        print(question['question_text'])
        for index, alternative in enumerate(question['alternatives'], 1):
            print(f"{index}. {alternative}")
        user_choice = int(input("Enter your answer: "))

        question['user_choice'] = user_choice

        if user_choice == question['correct_answer']:
            score += 1

    print(f"Your score is {score} out of {len(questions)}")

    for index, question in enumerate(questions, 1):
        result = "Correct answer" if question['user_choice'] == question['correct_answer'] else "Wrong answer"
        print(f"Question {index}: {result}")
        print(f"Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}")

if __name__ == "__main__":
    main()
```

### Summary - 12

- **Using JSON**: JSON is a versatile data structure suitable for storing complex data like quiz questions.
- **Building the Quiz App**: Load questions from a JSON file, display questions, collect user answers, evaluate the answers, and display the results.

## Introduction to Version Control and Git - Part 2

### Brief Summary - 13

The lesson introduced version control and Git, highlighting the importance of tracking changes in code, collaborating with others, and maintaining a history of changes. Git and GitHub are essential tools for managing and sharing code effectively.

### Key Points - 13

- **Version

 Control**: Practice of tracking and managing changes in code.

- **Problems Without Version Control**: Difficult to undo changes, error-prone manual management.
- **Version Control Systems**: Git is the most popular, others include Apache Subversion, Bazaar, and Mercurial.

### Benefits of Using Git - Part 2

- **Tracking Changes**: Easily revert to previous versions and view change history.
- **Collaboration**: Multiple people can work on the same codebase simultaneously.
- **Backup and Sharing**: Code can be backed up and shared via platforms like GitHub.

### Git and GitHub - Part 2

- **Git**: Local version control system for tracking changes.
- **GitHub**: Cloud-based platform for hosting Git repositories, providing collaboration tools.

### Practical Example of Git in Action - Part 2

1. **Viewing Changes in a Project**: Use Git to view history and compare versions.
2. **Comparing Code Versions**: Highlight differences between versions.

### Using Git and GitHub - Part 2

- **Setting Up Git**: Install Git and initialize a repository.
- **Committing Changes**: Commit changes with meaningful messages.
- **Pushing to GitHub**: Push commits to GitHub for backup and sharing.

### Summary - 13

- **Version Control**: Essential for managing code changes, collaboration, and backup.
- **GitHub**: Complements Git by offering cloud-based collaboration and sharing capabilities.

By mastering version control with Git and GitHub, you can effectively manage your code, collaborate with others, and ensure your projects are backed up and easily shareable.
![image.png](attachment:image.png)

## Day 16 Summary

## Summary and Bullet Points from the Video Transcript on Building GUI with Python

### Summary - 14

Building graphical user interfaces (GUIs) with Python. The focus is on creating a GUI for the todo app we have been developing. The backend functions remain the same, while we develop a new `main.py` file for the frontend using GUI components. The separation of frontend and backend emphasizes the importance of decoupling code, making it easier to extend and modify the application.

### Bullet Points

- **Introduction to GUI**:
  - GUI allows users to interact with the program graphically.
  - Users can click items, type in text boxes, and press buttons.

- **Existing Backend**:
  - The backend (`functions.py`) handles data processing and interactions with `todos.txt`.
  - We will not modify the backend; it remains the same.

- **Creating a New Frontend**:
  - We will write a new `main.py` file for the GUI.
  - The frontend will use the same backend functions to interact with data.

- **Importance of Functions**:
  - Decoupling frontend and backend code makes the program easier to modify and extend.
  - Previously, integrating code directly in `main.py` would have made modifications more complex.

- **Frontend vs Backend**:
  - **Frontend**: Constructs the user interface (CLI or GUI).
  - **Backend**: Handles data processing and sends data to the frontend.

- **Features of the GUI Todo App**:
  - Add new todos using the add button.
  - Edit existing todos by selecting an item and updating it.
  - Complete todos by selecting an item and pressing the complete button.
  - Exit the program using the exit button.

## Summary and Bullet Points from the Video Transcript on Creating Basic GUI with Python

### Summary - 15

Learn how to create a basic graphical user interface (GUI) for our todo app using the `PySimpleGUI` library. The GUI includes a window, a label, an input text box, and a button. We also refactor our project to accommodate multiple frontends, rename the original `main.py` to `cli.py`, and create a new `gui.py` file. The video emphasizes the importance of using functions and modular design to maintain a clean and extendable codebase. Finally, we demonstrate how to commit these changes using Git.

### Bullet Points - 15

- **Introduction to GUI**:
  - GUI allows graphical interaction with the program (clicking items, typing text, pressing buttons).
  - The backend remains the same, only the frontend is modified.

- **Refactoring the Project**:
  - Rename `main.py` to `cli.py` for clarity.
  - Create a new `gui.py` file for the graphical interface.

- **Installing PySimpleGUI**:
  - Use `pip install PySimpleGUI` to install the library.
  - Two methods to install: through PyCharm Preferences or using the terminal.

- **Creating Basic GUI Elements**:
  - Import the necessary modules (`PySimpleGUI` and backend functions).
  - Create a window with `sg.Window`.
  - Add a label with `sg.Text`.
  - Add an input text box with `sg.InputText`.
  - Add a button with `sg.Button`.

- **Constructing the Layout**:
  - Use a list of lists to define the layout of the GUI.
  - Each list represents a row of elements in the window.
  - Connect the elements (label, input box, button) to the window instance.

- **Displaying the GUI**:
  - Use the `read` method to display the window.
  - The `close` method to close the window.

- **Interacting with the GUI**:
  - Basic interaction demonstration with a button.
  - Placeholder for future interactions where button clicks will trigger functions.

- **Using Git for Version Control**:
  - Commit changes at significant milestones.
  - Write meaningful commit messages.
  - Example commit message: "create basic GUI without interactions".

## Summary and Bullet Points from the Video Transcript on GUI Code Experiments

### Summary - 16

Conducted a series of experiments to understand how the layout and structure of the PySimpleGUI elements affect the output of our GUI application. We explored how to properly structure the layout using lists of lists, the importance of using PySimpleGUI widget types, and the effect of different list structures on the arrangement of GUI elements.

### Bullet Points - 16

- **Stopping the Program**:
  - Recommended to stop the program using the stop button in the IDE during development to avoid errors.

- **Distributable File**:
  - Future goal: create an executable file so the program can be run without needing Python installed.

- **Experiments with Layout**:
  - **Flat List**:
    - Removing inner brackets and using a single list caused an error.
    - Each row in the GUI must be a list.
    - Correct structure: outer list containing lists for each row.
  - **Single Row Layout**:
    - When all elements are in one inner list, they appear in a single row.
    - Example: `layout = [[label, input_box, add_button]]`.
  - **Incorrect Elements**:
    - Placing non-PySimpleGUI elements like strings or numbers in the layout list causes errors.
  - **Separate Lists for Each Widget**:
    - Placing each widget in its own list results in each widget being on a separate row.
    - Example: `layout = [[label], [input_box], [add_button]]`.

- **Understanding the Layout**:
  - Each inner list represents a row in the GUI.
  - The outer list contains these row lists.
  - Proper structure ensures correct display of elements in the GUI.

## Summary and Bullet Points from the Video Transcript on Building a File Compressor GUI

### Summary - 17

Started building a file compressor application using the PySimpleGUI library in Python. The focus was on creating the graphical user interface (GUI) with elements like labels, input boxes, and buttons. The GUI allows users to select files to compress and choose a destination folder. Tomorrow's video will implement the actual compression functionality.

### Bullet Points - 17

- **File Compressor App**:
  - The app will compress selected files into a zip file.
  - Users can choose files to compress and a destination folder.

- **Creating GUI Elements**:
  - **Importing PySimpleGUI**:
    - `import PySimpleGUI as sg`
  - **First Row Elements**:
    - `sg.Text` for the label "Select files to compress".
    - `sg.Input` for the input box.
    - `sg.FilesBrowse` for the button labeled "Choose".
  - **Second Row Elements**:
    - `sg.Text` for the label "Select destination folder".
    - `sg.Input` for the input box.
    - `sg.FolderBrowse` for the button labeled "Choose".

- **Constructing the Layout**:
  - The layout is a list of lists, where each inner list represents a row in the GUI.
  - Example layout structure:

    ```python
    layout = [
        [label1, input1, choose_button1],
        [label2, input2, choose_button2],
        [compress_button]
    ]
    ```

  - **Creating the Window**:
    - `sg.Window` to create the window instance with a title "File Compressor".
    - Use `window.read()` to display the window.
    - Use `window.close()` to close the window after interaction.

- **Running the Program**:
  - On running, the GUI displays the labels, input boxes, and buttons.
  - Users can select multiple files using `shift + click`.
  - Selected file paths and the destination folder path are displayed in the input boxes.

- **Next Steps**:
  - Implementing the functionality to compress selected files and save the zip file to the chosen destination.

## Summary and Bullet Points from the Video Transcript on Using GitHub with Visual Studio Code

### Summary - 18

Learned how to set up and use GitHub with a Python project in Visual Studio Code. The process involved creating a GitHub account, creating a repository, connecting the local project to GitHub, and pushing commits to the remote repository. This allows us to manage and share code effectively using GitHub.

### Bullet Points - 18

- **Setting Up GitHub**:
  - Create a GitHub account at [github.com](https://github.com).
  - Sign in and create a new repository.
  - Name your repository (e.g., `todo-app`).
  - Set the repository to public or private.
  - Copy the repository URL.

- **Connecting GitHub with Visual Studio Code**:
  - Open your Visual Studio Code project.
  - Ensure Git is installed and initialized in your project.
  - Open the terminal in Visual Studio Code (`Ctrl +` ` or `View > Terminal`).
  - Add the remote URL:

    ```sh
    git remote add origin <repository URL>
    ```

  - Authenticate with GitHub if prompted.

- **Pushing Changes to GitHub**:
  - Make code changes and commit them in Visual Studio Code.
    - Open the Source Control panel (`Ctrl + Shift + G` or `View > Source Control`).
    - Stage changes by clicking the `+` icon next to the changed files.
    - Write a commit message and click the checkmark icon to commit.
  - Push commits to GitHub:
    - Click the three dots at the top of the Source Control panel and select `Push`.
    - Alternatively, use the terminal:

      ```sh
      git push -u origin master


      ```

- **Using GitHub Features**:
  - View files and directories on GitHub.
  - See the contents of files directly in the GitHub interface.
  - Access the commit history to view changes over time.
  - Check out specific commits to see the state of the project at that point.

- **Best Practices**:
  - Make frequent commits for every significant change or addition.
  - Push commits to GitHub regularly to keep the remote repository up-to-date.
  - Use meaningful commit messages to describe changes clearly.

#### Key Takeaways - 18

- GitHub is essential for version control and collaboration in programming projects.
- Setting up and connecting GitHub with your local project allows seamless code management.
- Regularly committing and pushing changes ensures your project is backed up and can be shared or collaborated on easily.
![image.png](attachment:image.png)

## Day 17 Summary

## Summary and Bullet Points from the Video Transcript on Enhancing and Implementing GUI Features in Visual Studio Code

### Summary - 19

In this video, we enhanced the GUI of our Python program by increasing the font size and implementing the Add button functionality. The Add button allows users to input a todo item and save it to a `todos.txt` file. We also ensured the program continues running after the Add button is pressed and handled the window close event to prevent errors.

### Bullet Points - 19

- **Enhancing GUI Appearance**:
  - Increased font size of the GUI elements:

    ```python
    sg.Window("My To-Do App", layout, font=("Helvetica", 20))
    ```

- **Implementing Add Button Functionality**:
  - Captured events and values from the GUI using `window.read()`:

    ```python
    event, values = window.read()
    ```

  - Used a `while True` loop to keep the window open and responsive:

    ```python
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    ```

  - Added functionality to append a new todo item to the `todos.txt` file:

    ```python
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    ```

- **Handling Window Close Event**:
  - Prevented errors by handling the window close event:

    ```python
    if event == sg.WIN_CLOSED:
        break
    ```

- **Using Git with Visual Studio Code**:
  - Committed and pushed changes after implementing the new feature:

    ```sh
    git commit -m "Implement Add button functionality"
    git push -u origin master
    ```

#### Key Takeaways - 19

- Enhanced the GUI by increasing font size for better visibility.
- Implemented the Add button functionality to save todo items to a file.
- Used a `while True` loop to keep the GUI running and handled the window close event.
- Made commits and pushed changes to GitHub for version control and backup.

## Summary and Bullet Points from the Video Transcript on Implementing the Edit Button in GUI

### Summary - 20

In this video, we implemented the Edit button in our GUI to allow users to edit existing todo items. We displayed the current todo items in a list box and allowed the user to select an item to edit. The selected item appears in the input box for editing, and once edited, it updates the `todos.txt` file and the list box in real-time.

### Bullet Points - 20

- **Enhancing the Layout**:
  - Added a list box and an Edit button:

    ```python
    layout = [
        [label1, input1, add_button],
        [listbox, edit_button]
    ]
    ```

- **Creating List Box and Edit Button**:
  - List Box:

    ```python
    listbox = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
    ```

  - Edit Button:

    ```python
    edit_button = sg.Button("Edit")
    ```

- **Handling Events**:
  - Captured events using `window.read()`.
  - Differentiated between Add and Edit events.
  - Edit Event:

    ```python
    if event == "Edit":
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    ```

- **Synchronizing Input Box with List Box**:
  - Updated the input box to show the selected todo item:

    ```python
    if event == 'todos':
        window['todo'].update(value=values['todos'][0])
    ```

- **Ensuring Real-Time Updates**:
  - Updated the list box when a new todo item is added:

    ```python
    if event == "Add":
        window['todos'].update(values=todos)
    ```

- **Using Git with Visual Studio Code**:
  - Committed and pushed changes after implementing the Edit button:

    ```sh
    git commit -m "Implement Edit button functionality"
    git push -u origin master
    ```

#### Key Takeaways - 20

- Implemented the Edit button to allow users to edit existing todo items.
- Displayed the list of todos in a list box and synchronized it with the input box for editing.
- Ensured real-time updates of the list box and input box when todos are edited or added.
- Committed and pushed changes to GitHub for version control and backup.

## Summary and Bullet Points from the Video Transcript on Experiments with Break Statement and Layout Argument

### Summary - 21

In this video, we conducted two experiments: one to understand the behavior of the break statement compared to the exit function, and another to explore different ways to handle the layout argument in a GUI application. The experiments illustrated the differences in control flow when using break versus exit, and demonstrated how to dynamically construct a layout for the GUI.

### Bullet Points - 21

- **Experiment 1: Break Statement vs. Exit Function**:
  - Break Statement:

    ```python
    while True:
        if condition:
            break
    print("This will be executed after the loop")
    ```

  - Exit Function:

    ```python
    while True:
        if condition:
            exit()
    print("This will not be executed")
    ```

  - Usage Recommendation: Use break for better control of the program flow.

- **Experiment 2: Handling Layout Argument**:
  - Directly in the Argument:

    ```python
    layout = [
        [sg.Text("Label"), sg.Input(), sg.Button("Add")],
        [sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10)), sg.Button("Edit")]
    ]
    window = sg.Window("My App", layout)
    ```

  - Using an Intermediate Variable:

    ```python
    layout = [
        [sg.Text("Label"), sg.Input(), sg.Button("Add")],
        [sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10)), sg.Button("Edit")]
    ]
    window = sg.Window("My App", layout)
    ```

  - Dynamic Construction of Layout:

    ```python
    button_labels = ["Close", "Apply"]
    layout = []
    for bl in button_labels:
        layout.append([sg.Button(bl)])
    window = sg.Window("My App", layout)
    ```

#### Key Takeaways - 21

- **Break Statement**: Use break to stop loops and allow subsequent code execution.
- **Exit Function**: Use exit to completely stop program execution.
- **Handling Layout in GUI**: Define the layout directly or use an intermediate variable for flexibility.
- **Best Practices**: Use intermediate variables for flexible GUI design and break for more controlled loops.

## Summary and Bullet Points from the Video Transcript on Implementing File Compressor Functionalities

### Summary - 22

In this video, we implemented the functionalities of the file compressor application. The GUI created in the previous session was connected to the backend logic, enabling the compression of selected files into a zip archive. The implementation involved reading user inputs, creating the zip file, and providing feedback to the user upon successful compression.

### Bullet Points - 22

- **Setting Up the While Loop**:
  - Continuously read events and values from the GUI.
  - Display selected file paths and destination folder.

- **Reading User Inputs**:
  - Use `values['files']` to get the list of selected file paths.
  - Use `values['folder']` to get the destination folder path.
  - Split the file paths string by semicolons to get a list.

- **Creating the Zip File**:
  - Use `zipfile` standard library for flexible zip file operations:

    ```python
    import zipfile
    from pathlib import Path

    def make_archive(filepaths, dest_dir):
        dest_path = Path(dest_dir) / "compressed.zip"
        with zipfile.ZipFile(dest_path, 'w') as archive:
            for filepath in filepaths:
                filepath = Path(filepath)
                archive.write(filepath, arcname=filepath.name)
    ```

- **Testing the Zip Creation Function**:
  - Manually provide file paths and destination directory.
  - Verify the compressed zip file contains the correct files.

- **Connecting Backend to GUI**:
  - Import and use `make_archive` in the main GUI script.
  - Call `make_archive` with user-selected file paths and destination folder.

- **Providing User Feedback**:
  - Add a label to the GUI to display a "Compression completed" message:

    ```python
    output_label = sg.Text('', key='output')
    layout = [
        [sg.Text("Select files to compress"), sg.Input(), sg.FilesBrowse(key='files')],
        [sg.Text("Select destination folder"), sg.Input(), sg.FolderBrowse(key='folder')],
        [sg.Button("Compress"), output_label]
    ]
    window = sg.Window("File Compressor", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Compress":
            filepaths = values['files'].split(';')
            folder = values['folder']
            make_archive(filepaths, folder)
            window['output'].update("Compression completed", text_color='green')
    ```

#### Key Takeaways - 22

- **Reading User Inputs**: Extract file paths and destination folder from

 GUI inputs.

- **Creating Zip Archives**: Use `zipfile` for flexible and efficient zip file creation.
- **Dynamic GUI Updates**: Provide real-time feedback to users using label updates.
- **Testing and Debugging**: Test backend functions independently before integrating with the GUI.

## Summary and Bullet Points from the Video Transcript on Cloning GitHub Repositories

### Summary - 23

In this video, we learned how to clone a GitHub repository to our local computer using Visual Studio Code. The process involves copying a repository URL, cloning it into VS Code, and managing dependencies using `requirements.txt`. Additionally, we covered how to push changes to a new GitHub repository if you want to share or collaborate on the cloned project.

### Bullet Points - 23

- **Cloning a GitHub Repository**:
  - Search for a Repository: Example: `arditsulceteaching` GitHub account.
  - Manual Download: Click `Code` > `Download ZIP`.
  - Professional Way (Cloning): Click `Code` > `HTTPS` and copy the URL.

    ```sh
    git clone https://github.com/arditsulceteaching/my-todo-app.git
    ```

- **Setting Up the Project in VS Code**:
  - Look for `requirements.txt` in the repository.
  - Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

- **Running the Project**:
  - Use Streamlit to run a web app:

    ```sh
    streamlit run web.py
    ```

- **Managing GitHub Remotes**:
  - Adding a New Remote:

    ```sh
    git remote add origin <new repository URL>
    ```

  - Pushing to a New Repository:

    ```sh
    git push -u origin master
    ```

- **Best Practices and Tips**:
  - Use keys for readability in GUI components.
  - Test backend functions independently before integrating with the GUI.
  - Use the update method to provide real-time feedback to users.

#### Key Takeaways - 23

- **Cloning Repositories**: Clone repositories using HTTPS URLs for professional handling of code.
- **Running and Testing**: Use appropriate commands and virtual environments to run projects locally.
- **Managing GitHub Projects**: Add new remotes to manage where your code is pushed. Always verify successful pushes and ensure repository synchronization.

By following these steps, you can efficiently clone, manage, and run projects from GitHub, enabling collaboration and version control for your Python projects.
![image.png](attachment:image.png)

## Day 18 Summary

## Summary and Bullet Points from the Video Transcript on Adding Complete and Exit Buttons

### Summary - 24

In this video, we enhanced our to-do application by adding a "Complete" button to delete selected to-dos and an "Exit" button to close the program. We updated the layout to accommodate these new buttons, implemented their functionality, and ensured the user interface reflects these changes in real time.

### Bullet Points - 24

- **New Buttons**:
  - **Complete Button**:
    - Placed to the right of the "Edit" button.
    - Deletes the selected to-do from `todos.txt` and updates the list box.
  - **Exit Button**:
    - Placed below the list box.
    - Closes the program when clicked.

- **Layout Updates**:
  - Added a "Complete" button next to the "Edit" button:

    ```python
    complete_button = sg.Button("Complete")
    ```

  - Added an "Exit" button in a new row:

    ```python
    exit_button = sg.Button("Exit")
    ```

- **Implementing the Complete Button**:
  - Added a case for "Complete":

    ```python
    if event == "Complete":
        todo_to_complete = values["todos"][0]
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        window["todos"].update(values=todos)
        window["todo"].update(value="")
    ```

  - This code retrieves the selected to-do, removes it from the list, updates the file, and clears the input box.

- **Implementing the Exit Button**:
  - Added a case for "Exit":

    ```python
    if event == "Exit":
        break
    ```

  - This code breaks the loop to close the program.

- **Testing and Validation**:
  - Tested the application to ensure:
    - The "Complete" button removes the selected to-do from the list and the input box.
    - The "Exit" button closes the application without errors.

- **Committing Changes**:
  - Committed the updates with a message:

    ```sh
    git commit -m "Implement the Complete and Exit buttons"
    ```

#### Key Takeaways - 24

- **Adding Functionality**:
  - New buttons enhance user interaction, making the app more user-friendly.
- **Updating the Layout**:
  - Ensure the layout is adjusted to accommodate new elements seamlessly.
- **Implementing Button Actions**:
  - Retrieve and update the necessary data structures and UI elements to reflect changes.
- **Committing Regularly**:
  - Regular commits help keep track of changes and synchronize with version control systems like GitHub.

By following these steps, we successfully added new features to our to-do application, improving its functionality and user experience.

---

## Summary and Bullet Points from the Video Transcript on Completing the To-Do App

### Summary - 25

In this video, we finalized the development of our to-do application by fixing existing errors, adding a live date and time display, and polishing the user interface with themes and adjusted element sizes. The final touches ensure a smooth and user-friendly experience.

### Bullet Points - 25

- **Fixing Errors**:
  - **Edit Button Error Handling**:
    - Added a `try-except` block to handle `IndexError` when no item is selected.
    - Displayed an error message using `sg.popup`:

      ```python
      try:
          todo_to_edit = values["todos"][0]
      except IndexError:
          sg.popup("Please select an item first", font=("Helvetica", 20))
      ```

  - **Complete Button Error Handling**:
    - Similarly handled errors for the Complete button:

      ```python
      try:
          todo_to_complete = values["todos"][0]
      except IndexError:
          sg.popup("Please select an item first", font=("Helvetica", 20))
      ```

- **Adding Live Date and Time**:
  - **Clock Widget**:
    - Created a clock label:

      ```python
      clock = sg.Text("", key="clock")
      ```

    - Added clock to the layout:

      ```python
      [clock]
      ```

    - Updated the clock every 200 milliseconds:

      ```python
      window.read(timeout=200)
      window["clock"].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))
      ```

- **Polishing the Program**:
  - **Theme and Sizing**:
    - Changed the theme of the GUI:

      ```python
      sg.theme("DarkPurple4")
      ```

    - Adjusted sizes for better visibility and usability:

      ```python
      size=(45, 10)  # Example for list box
      size=(10,)     # Example for button width
      ```

- **Additional Tips**:
  - **Rainbow Brackets Plugin**:
    - Recommended using the Rainbow plugin for PyCharm for better readability of code.
    - Plugin colors brackets, making it easier to match opening and closing brackets.

- **Final Commit**:
  - Committed the final changes:

    ```sh
    git commit -m "Change theme, add clock, handle edit and complete errors"
    ```

#### Key Takeaways - 25

- **Error Handling**:
  - Use `try-except` blocks to handle potential errors and improve user experience by displaying helpful messages.
- **Live Updates**:
  - Implement live date and time displays by using timeouts and updating the GUI at regular intervals.
- **User Interface**:
  - Enhance the visual appeal and usability of the application by changing themes and adjusting the sizes of widgets.
- **Development Tools**:
  - Utilize plugins like Rainbow for better code readability and management.

By following these steps, we completed our to-do application, making it robust and user-friendly. The enhancements ensure a seamless interaction for users, providing real-time updates and a polished interface.

---

## Summary and Bullet Points from the Video Transcript on Building a Zip Extractor Program

### Summary - 26

In this video, we built a Zip Extractor program that extracts files from a zip archive to a specified destination directory. The process involved four main steps: designing the front end, coding the front end, coding the back end, and connecting everything together. This methodical approach ensures a clear understanding of how to start and complete a program.

### Bullet Points - 26

- **Step 1: Designing the Front End**:
  - **Design Approach**:
    - Use paper or software like Figma for complex designs.
    - Sketch the graphical user interface (GUI) layout.
  - **Layout Elements**:
    - Title: "Archive Extractor"
    - Labels: "Select Archive" and "Select Destination Directory"
    - Input boxes and browse buttons for file and directory selection.
    - Extract button and a message label for extraction status.

- **Step 2: Coding the Front End**:
  - **Import PySimpleGUI**:

    ```python
    import PySimpleGUI as sg
    ```

  - **Define Theme**:

    ```python
    sg.theme('Black')
    ```

  - **Create Widgets**:
    - Labels, input boxes, and buttons for archive and directory selection.
    - Extract button and status message label.
  - **Window Layout**:

    ```python
    layout = [
        [sg.Text("Select Archive"), sg.Input(), sg.FileBrowse(key="archive")],
        [sg.Text("Select Destination Directory"), sg.Input(), sg.FolderBrowse(key="folder")],
        [sg.Button("Extract"), sg.Text("", key="output", text_color="green")]
    ]
    ```

  - **Initialize Window**:

    ```python
    window = sg.Window("Archive Extractor", layout)
    window.read()
    window.close()
    ```

- **Step 3: Coding the Back End**:
  - **Import zipfile Module**:

    ```python
    import zipfile
    ```

  - **Define Extraction Function**:

    ```python
    def extract_archive(archive_path, dest_dir):
        with zipfile.ZipFile(archive_path, 'r') as archive:
            archive.extractall(dest_dir)
    ```

  - **Test Function Independently**:

    ```python
    if __name__ == "__main__":
        extract_archive("path/to/compressed.zip", "path/to/destination")
    ```

- **Step 4: Connecting Front End and Back End**:
  - **Add Event Loop**:

    ```python
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Extract":
            archive_path = values["archive"]
            dest_dir = values["folder"]
            extract_archive(archive_path, dest_dir)
            window["output"].update("Extraction completed")
    window.close()
    ```

  - **Handle Errors Gracefully** (Optional):
    - Use `try` and `except` blocks to handle potential errors during extraction.

#### Key Takeaways - 26

- **Methodical Approach**:
  - Design the front end before coding.
  - Code the front end and back end separately, then connect them.
- **Using PySimpleGUI**:
  - PySimpleGUI simplifies creating GUI applications.
- **Backend Functionality**:
  - Use the `zipfile` module to handle zip file extraction.
- **Testing**:
  - Independently test backend functions to ensure they work as expected.
- **Error Handling**:
  - Use `try` and `except` to handle errors and provide user feedback.

This video demonstrated the structured approach to building a functional Zip Extractor program, emphasizing the importance of clear steps and error handling in software development.

---

## Summary and Bullet Points from the Video Transcript on Creating Standalone Executables

### Summary - 27

In this video, we learned how to convert Python

 scripts into standalone executable files for Windows, Mac, and Linux. This process involves using tools like `pyinstaller` for Windows and Linux, and `platypus` for Mac. Additionally, we made sure that our program could handle missing external files, ensuring a smooth user experience.

### Bullet Points - 27

- **Preparation**:
  - Ensure the Python script works without errors.
  - Handle external file dependencies (e.g., `todos.txt`).

- **Handling External File Dependencies**:
  - Use the `os` module to check if `todos.txt` exists.
  - Create the file if it does not exist:

    ```python
    import os

    if not os.path.exists("todos.txt"):
        with open("todos.txt", "w") as file:
            pass
    ```

- **Creating an Executable for Windows**:
  - Ensure `venv` is active:

    ```powershell
    set-executionpolicy remotesigned -scope currentuser
    ```

  - Install `pyinstaller`:

    ```powershell
    pip install pyinstaller
    ```

  - Generate the executable:

    ```powershell
    pyinstaller --onefile --windowed --clean gui.py
    ```

  - Find the executable in the `dist` folder.

- **Creating an Executable for Mac**:
  - Install `platypus` using Homebrew:

    ```sh
    brew install --cask platypus
    ```

  - Open `platypus` and configure:
    - Set the app name, Python interpreter path, and script path.
    - Add `functions.py` to bundled files.
    - Create the app, then optionally remove the text window for the final version.
  - Find the `.app` file in the project directory.

- **Creating an Executable for Linux**:
  - Install `pyinstaller`:

    ```sh
    pip install pyinstaller
    ```

  - Generate the executable:

    ```sh
    pyinstaller --onefile --windowed --clean gui.py
    ```

  - Resolve any missing dependencies (e.g., `python3.10-dev` on Ubuntu):

    ```sh
    sudo apt-get install python3.10-dev
    ```

  - Find the executable in the `dist` folder.

#### Key Takeaways - 27

- **Executable Creation**:
  - Convert Python scripts into standalone executables using `pyinstaller` and `platypus`.
- **File Handling**:
  - Ensure external files are handled gracefully by creating them if they do not exist.
- **Cross-Platform Compatibility**:
  - Each operating system requires a different process for creating executables.
- **User Experience**:
  - Provide a seamless experience by generating necessary files and avoiding command line windows in the final executable.

This video provided a comprehensive guide on distributing Python programs as standalone applications across different operating systems, ensuring that end-users can run the applications without needing to install Python.
![image.png](attachment:image.png)

## Day 19 Summary

## Summary and Bullet Points from the Video Transcript on Creating a Web App with Python

### Summary - 28

In this video, we learned how to create a web app version of our to-do application using Python and the Streamlit library. The instructor demonstrated the steps to set up the web app, add UI elements like checkboxes and input fields, and explained the basic workings of Streamlit. The session concluded with an overview of Streamlit's functionality and its ability to handle multiple user sessions independently.

### Bullet Points - 28

- **Introduction to Web Apps**:
  - Web apps are increasingly popular and easier to maintain.
  - They provide a modern and practical user experience.

- **Demonstration of the Todo Web App**:
  - Users can view, add, and mark to-do items as complete.
  - The backend reuses the same `todos.txt` file.

- **Setting Up the Web App**:
  - **Creating a New Python File**:
    - Named `web.py`.
    - Added to Git version control.
  - **Importing Streamlit**:

    ```python
    import streamlit as st
    ```

- **Installing Streamlit**:
  - Use the PyCharm Python packages interface or terminal:

    ```sh
    pip install streamlit
    ```

- **Basic Streamlit Commands**:
  - **Title and Subheader**:

    ```python
    st.title("My Todo App")
    st.subheader("Increase your productivity")
    ```

  - **Running the Streamlit App**:

    ```sh
    streamlit run web.py
    ```

  - **Viewing the App**:
    - Opens in the browser at `localhost:8502`.

- **Adding UI Elements**:
  - **Text**:

    ```python
    st.write("This app is to increase your productivity")
    ```

  - **Checkboxes**:

    ```python
    st.checkbox("Buy grocery")
    st.checkbox("Clean the house")
    ```

  - **Input Box**:

    ```python
    st.text_input("Enter a todo")
    ```

- **Fetching Todos from Backend**:
  - **Importing and Using Functions**:

    ```python
    import functions

    todos = functions.get_todos()
    for todo in todos:
        st.checkbox(todo)
    ```

- **Understanding Streamlit's Workflow**:
  - The order of function calls determines the layout.
  - The script is executed from top to bottom on each page load.
  - Each user session is independent, handled separately by the server.

- **Interactive Elements (Preview)**:
  - In the next session, interactivity will be added to make the app functional.

#### Key Takeaways - 28

- **Web App Setup**:
  - Streamlit simplifies creating web apps with Python.
  - Easy integration with existing backend functions.
- **UI Elements**:
  - Basic UI components include titles, subheaders, text, checkboxes, and input boxes.
- **Running and Viewing the App**:
  - Use `streamlit run <script>` to run the app and view it in the browser.
- **Streamlit Workflow**:
  - Understand that each page load re-runs the script from top to bottom.
  - Sessions are handled independently, allowing multiple users to interact with the app simultaneously.

This session provided a foundational understanding of creating web apps with Streamlit, setting the stage for adding interactivity and further functionalities in subsequent lessons.

---

## Summary and Bullet Points from the Video Transcript on Implementing the Feature of Adding New Todos

### Summary - 29

In this video, we learned how to implement the feature that allows users to add new to-do items to the list using Streamlit. The instructor explained the importance of maintaining a clean development setup and ensuring that lines of code are not too long for better readability. The video walked through the process of connecting the text input widget to a callback function that appends new to-dos to the list and updates the `todos.txt` file.

### Bullet Points - 29

- **Development Setup Recommendations**:
  - Split your screen between the IDE and the web browser for efficient web development.
  - Keep lines of code under 79 characters for better readability.

- **Preliminary Steps**:
  - Ensure `todos.txt` has a new line at the end to avoid appending new to-dos on the same line.

- **Commit Changes**:
  - Commit the initial setup of the static web interface:

    ```sh
    git commit -m "Create a static web interface"
    ```

- **Connecting Text Input to Actions**:
  - Use the `on_change` argument to link a text input widget to a callback function:

    ```python
    st.text_input(label="", placeholder="Add new todo", on_change=add_todo, key="new_todo")
    ```

- **Callback Function**:
  - Define the `add_todo` function to handle adding new to-dos:

    ```python
    def add_todo():
        todo = st.session_state["new_todo"]
        todos.append(todo + "\n")
        functions.write_todos(todos)
    ```

- **Understanding `st.session_state`**:
  - `st.session_state` acts like a dictionary that stores the state of the application:

    ```python
    # Example to access the session state
    todo = st.session_state["new_todo"]
    ```

- **Updating the Todos List**:
  - Append the new to-do to the list and write it to `todos.txt`:

    ```python
    todos.append(todo + "\n")
    functions.write_todos(todos)
    ```

- **Refreshing the App**:
  - The script executes from top to bottom upon each page load, ensuring the updated to-do list is displayed.

- **Handling New Line Characters**:
  - Add a newline character to each new to-do to ensure proper formatting:

    ```python
    todos.append(todo + "\n")
    ```

- **Commit Changes**:
  - Commit the feature implementation:

    ```sh
    git commit -m "Implement add new todo items feature"
    ```

#### Key Takeaways - 29

- **Interactive Widgets**:
  - Streamlit allows linking widgets to callback functions for interactivity.
- **Session State**:
  - Use `st.session_state` to manage and retrieve the state of input elements.
- **Appending Todos**:
  - Ensure new to-dos are properly formatted and appended to both the UI list and `todos.txt`.
- **Testing and Debugging**:
  - Continuously test and refresh the app to validate changes and debug issues.

By following these steps, we successfully implemented the feature to add new to-do items in our web app, enhancing its functionality and interactivity for the users.

---

## Summary and Bullet Points from the Video Transcript on Implementing the Complete Todo Feature

### Summary - 30

In this video, we implemented the feature to complete to-do items in our web app. This involved removing checked to-do items from both the list displayed on the web app and the `todos.txt` file. We utilized `st.session_state` to track the state of each checkbox, ensuring that changes made in the UI are reflected in the backend.

### Bullet Points - 30

- **Understanding `st.session_state`**:
  - `st.session_state` acts like a dictionary that holds widget states.
  - Checkboxes need a unique key to be tracked in `session_state`.

- **Adding Keys to Checkboxes**:
  - Assign each checkbox a unique key based on the to-do item:

    ```python
    for todo in todos:
        st.checkbox(todo, key=todo)
    ```

- **Printing Session State**:
  - Print `st.session_state` to understand its structure and track widget states:

    ```python
    st.write(st.session_state)
    ```

- **Detecting Checkbox Changes**:
  - Store checkbox states in a variable:

    ```python
    checkbox = st.session_state[todo]
    ```

- **Enumerating Todos**:
  - Use `enumerate` to get the index of each to-do item:

    ```python
    for index, todo in enumerate(todos):
    ```

- **Removing Completed Todos**:
  - Check if a checkbox is selected, then remove the corresponding to-do item:

    ```python
    if st.session_state[todo]:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    ```

- **Using `st.experimental_rerun`**:
  - Refresh the app state after a change:

    ```python
    st.experimental_rerun()
    ```

- **Handling Errors**:
  - Ensure the correct spelling and usage of `st.experimental_rerun`.

- **Testing the Implementation**:
  - Refresh the page to see the changes.
  - Verify that to-do items are removed from both the list and `todos.txt`.

- **Final Code Example**:

  ```python
  import streamlit as st
  import functions

  todos = functions.get_todos()

  def add_todo():
      todo = st.session_state["new_todo"]
      todos.append(todo + "\n")
      functions.write_todos(todos)

  st.title("My Todo App")
  st.subheader("This app is to increase your productivity.")
  st.write("This is a minimalistic todo app.")

  for todo in todos:
      checkbox = st.checkbox(todo, key=todo)
      if checkbox:
          todos.pop(todos.index(todo))
          functions.write_todos(todos)
          del st.session_state[todo]
          st.experimental_rerun()

  st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
  ```

- **Commit Changes**:
  - Commit the new feature

 implementation:
    ```sh
    git commit -m "Implement complete todo items feature"
    ```

#### Key Takeaways - 30

- **Session State Management**:
  - Use `st.session_state` to track and manage the state of interactive widgets.
- **Dynamic Keys for Widgets**:
  - Ensure each interactive element has a unique key for proper state tracking.
- **Enumerate for Indexing**:
  - Use `enumerate` to access both the index and value in loops.
- **Rerun Mechanism**:
  - Use `st.experimental_rerun` to refresh the app state after changes.

By following these steps, we successfully added the feature to complete to-do items, ensuring they are removed from both the UI and the backend data file, making our web app fully functional and interactive.

---

## Summary and Bullet Points from the Video Transcript on Deploying Streamlit Apps

### Summary - 31

In this video, we learned how to deploy a Streamlit app on a live server, making it accessible through a public URL. The process involves creating a standalone project for the web app, installing necessary packages, generating a `requirements.txt` file, pushing the project to GitHub, and deploying it using Streamlit's deployment service.

### Bullet Points - 31

- **Creating a Standalone Project**:
  - Ensure the project contains only files related to the web app.
  - Create a new project and copy the necessary files (`functions.py`, `web.py`, and `todos.txt`).

- **Installing Required Packages**:
  - Install Streamlit via PyCharm or using the terminal:

    ```sh
    pip install streamlit
    ```

- **Testing the App Locally**:
  - Run the Streamlit app locally to ensure it works:

    ```sh
    streamlit run web.py
    ```

- **Generating `requirements.txt`**:
  - Create a `requirements.txt` file listing all dependencies:

    ```sh
    pip freeze > requirements.txt
    ```

- **Pushing the Project to GitHub**:
  - Enable version control in PyCharm.
  - Create a new repository on GitHub.
  - Add the remote URL in PyCharm and push the files:

    ```sh
    git remote add origin <repository_url>
    git push -u origin master
    ```

- **Deploying with Streamlit**:
  - Open the terminal and run the Streamlit app:

    ```sh
    streamlit run web.py
    ```

  - Go to the app menu and select "Deploy this app".
  - Follow the steps to deploy on Streamlit's cloud service.
  - The public URL for the app will be generated after deployment.

- **Verifying Deployment**:
  - Check the deployed app via the provided URL.
  - Use "Manage app" to view logs and troubleshoot any issues.

- **Committing Changes**:
  - Regularly commit and push changes to keep the repository updated:

    ```sh
    git add .
    git commit -m "Initial commit"
    git push
    ```

#### Key Takeaways - 31

- **Streamlit and Deployment**:
  - Streamlit provides both the tools to create web apps and a free cloud service for deployment.
- **Standalone Projects**:
  - Ensure the project directory contains only relevant files for easier management and deployment.
- **Dependency Management**:
  - Use `requirements.txt` to list all necessary packages for the app to function correctly.
- **Version Control**:
  - Regularly use GitHub to manage and share the project, making deployment and updates seamless.
- **Streamlit Deployment**:
  - Deploying with Streamlit's service is straightforward and provides a public URL for the app.

By following these steps, we successfully deployed our Streamlit app, making it accessible to everyone through a public URL, ensuring our web app is live and ready for use.

---

## Summary and Bullet Points from the Video Transcript on Code Experiments

### Summary - 32

In this video, we conducted several code experiments to enhance our understanding of the Streamlit library and its capabilities. These experiments included modifying the order of widgets, applying HTML styles, configuring page layout, and creating multi-page web apps. We also learned how to use Git for managing experimental changes and resetting the code to a previous state.

### Bullet Points - 32

- **Using Git for Experiments**:
  - Ensure all changes are committed before starting experiments.
  - Use Git to reset changes after experiments:

    ```sh
    git reset --hard HEAD
    ```

  - Add and commit files before making changes:

    ```sh
    git add .
    git commit -m "Initial commit"
    ```

- **Widget Order**:
  - The order of widgets affects their placement in the app.
  - Example:

    ```python
    st.text_input("Add new todo")
    for todo in todos:
        st.checkbox(todo)
    ```

- **HTML in Streamlit**:
  - Use `unsafe_allow_html=True` to render HTML in text:

    ```python
    st.write("This app is to <b>increase productivity</b>", unsafe_allow_html=True)
    ```

  - Apply HTML tags for styling:

    ```python
    st.write("<h1>Productivity</h1>", unsafe_allow_html=True)
    ```

- **Page Configuration**:
  - Use `st.set_page_config` to set the layout:

    ```python
    st.set_page_config(layout="wide")
    ```

  - This expands the width of the webpage.

- **Multi-page Web Apps**:
  - Create a `pages` folder in the root directory.
  - Add Python files for each page:

    ```python
    # pages/About.py
    import streamlit as st
    st.write("Hello from the About page")
    ```

  - Streamlit automatically generates a sidebar for page navigation.

- **Resetting Code**:
  - Use Git to revert changes after experiments:

    ```sh
    git reset --hard HEAD
    ```

  - Ensure the project returns to its initial state.

#### Key Takeaways - 32

- **Experimentation**:
  - Experimenting with code helps to understand new features and functionalities.
- **Version Control**:
  - Git is essential for managing code changes and reverting to previous states.
- **HTML Integration**:
  - Streamlit allows HTML integration for enhanced text styling.
- **Responsive Layouts**:
  - Use `st.set_page_config` to create responsive layouts that adapt to different screen sizes.
- **Multi-page Apps**:
  - Easily create multi-page applications in Streamlit by organizing code into separate Python files within a `pages` folder.

By following these steps, we successfully conducted various code experiments, gaining deeper insights into Streamlit's capabilities while maintaining control over our codebase through Git.

---

## Summary and Bullet Points from the Video Transcript on Building a Webcam Image Capture and Grayscale Conversion Web App

### Summary - 33

In this video, we created a web app using Streamlit that allows users to capture images from their computer's webcam and convert those images to grayscale. The process involves using Streamlit for the web interface and the Pillow library for image processing. The app provides an easy-to-use interface for capturing and processing images directly from a web browser.

### Bullet Points - 33

- **Setting Up the Project**:
  - Create a new Python file, `bonus19.py`.
  - Import the necessary libraries:

    ```python
    import streamlit as st
    from PIL import Image
    ```

- **Capturing Webcam Image**:
  - Use `st.camera_input` to start the webcam and capture an image:

    ```python
    camera_image = st.camera_input("Camera")
    ```

- **Installing Pillow Library**:
  - Install the Pillow library if not already installed:

    ```sh
    pip install Pillow
    ```

  - Alternatively, check for installation in the Python packages section in PyCharm.

- **Image Processing**:
  - Convert the captured image to a Pillow image instance and then to grayscale:

    ```python
    if camera_image:
        img = Image.open(camera_image)
        gray_img = img.convert("L")
        st.image(gray_img)
    ```

- **Handling Errors**:
  - Use a conditional to check if an image has been captured before processing:

    ```python
    if camera_image:
        img = Image.open(camera_image)
        gray_img = img.convert("L")
        st.image(gray_img)
    ```

- **Improving User Experience**:
  - Use an expander to control when the camera starts:

    ```python
    with st.expander("Start Camera"):
        camera_image = st.camera_input("Camera")
    ```

  - This prevents the camera from starting automatically when the page loads.

#### Key Takeaways - 33

- **Streamlit Integration**:
  - Streamlit makes it easy to integrate webcam functionality into web apps.
- **Image Processing with Pillow**:
  - The Pillow library provides powerful tools for image manipulation, including converting images to grayscale.
- **User Interface Enhancement**:
  - Use expanders to improve the user interface and control when certain elements are displayed or activated.
- **Error Handling**:
  - Use conditionals to ensure the app runs smoothly and handles cases where an image is not captured yet.

By following these steps, we successfully created a web app that captures images from a webcam and converts them to grayscale, providing an interactive and user-friendly experience.

---

## Summary and Bullet Points from the Video Transcript on Deploying a Streamlit App to Heroku

### Summary - 34

In this video, we learned how to deploy a Streamlit web app to Heroku, a Platform as a Service (PaaS) that allows for scalable web app hosting. This deployment method is more powerful and flexible compared to Streamlit Cloud, providing the capability to handle increased traffic by scaling resources. The process involves setting up a Heroku account, creating a new app, connecting

 it to a GitHub repository, and adding necessary configuration files to ensure the app runs smoothly on the server.

### Bullet Points - 34

- **Deployment Options**:
  - **Streamlit Cloud**:
    - Easy and free but limited scalability.
  - **Platform as a Service (PaaS)**:
    - Examples: Heroku, PythonAnywhere, Google App Engine, AWS.
    - Easier to use, focuses on development without server maintenance.
  - **Infrastructure as a Service (IaaS)**:
    - Examples: DigitalOcean, AWS (also offers PaaS).
    - More flexible, requires maintaining the operating system.
  - **Physical Servers**:
    - Most complex, involves maintaining physical hardware and OS.

- **Setting Up Heroku Deployment**:
  - **Heroku Account**:
    - Sign up and log in to Heroku.
    - Add billing information under account settings.

  - **Creating a New App**:
    - Go to Heroku dashboard and create a new app.
    - Choose a unique name and region (US or Europe).

  - **Connecting GitHub Repository**:
    - Authenticate Heroku with GitHub.
    - Search and connect your repository.
    - Enable automatic deploys for continuous integration.

- **Preparing Project for Deployment**:
  - **Configuration Files**:
    - **setup.sh**:

      ```sh
      mkdir -p ~/.streamlit/
      echo "\
      [general]\n\
      email = \"your-email@example.com\"\n\
      " > ~/.streamlit/credentials.toml
      echo "\
      [server]\n\
      headless = true\n\
      enableCORS=false\n\
      port = $PORT\n\
      " > ~/.streamlit/config.toml
      ```

    - **Procfile**:

      ```sh
      web: sh setup.sh && streamlit run web.py
      ```

    - Add these files to the project root and commit them to Git.

  - **Requirements File**:
    - Ensure `requirements.txt` is present with necessary packages:

      ```sh
      pip freeze > requirements.txt
      ```

- **Deploying the App**:
  - Ensure the app works locally:

    ```sh
    streamlit run web.py
    ```

  - Commit changes and push to GitHub.
  - Deploy the branch from Heroku dashboard.
  - Monitor deployment logs and ensure successful launch.

- **Testing and Scaling**:
  - Verify the deployed app through the provided Heroku URL.
  - Be prepared to scale the app if it gains more traffic, upgrading the Heroku plan as needed.

#### Key Takeaways - 34

- **Ease of Use**:
  - Heroku simplifies the deployment process, focusing on development rather than server maintenance.
- **Scalability**:
  - PaaS like Heroku allows for easy scaling to handle increased traffic.
- **Configuration Management**:
  - Proper configuration files (`setup.sh`, `Procfile`, `requirements.txt`) are crucial for a smooth deployment.
- **Continuous Integration**:
  - Enabling automatic deploys ensures that updates to the codebase are reflected in the live app seamlessly.

By following these steps, we successfully deployed a Streamlit app to Heroku, providing a robust and scalable solution for web app hosting.
![image.png](attachment:image.png)

## Day 20
