# Days 21 - 25: Python Mega Course

## Day 21

### Summary of the Prototyping with Figma Video

In this video, the instructor introduces the concept of prototyping for app development, demonstrating how to use Figma to create visual representations of applications before coding them. This practice helps in saving time, improving design, and communicating ideas with clients or investors.

### Key Takeaways - 1

- **Definition of Prototype**:
  - A prototype is a preliminary version of an app, serving as a visual representation rather than the functional product.
  - It helps visualize the final product, making the coding process easier and more structured.

- **Importance of Prototyping**:
  - Saves time by providing a clear visual guide for development.
  - Allows for feedback and iterations before investing time in coding.
  - Essential for professional-level development, especially when working with clients or investors.

- **Tool for Prototyping**:
  - **Figma**: An industry-standard tool for creating prototypes.
  - **Access**: Available as a browser-based application and as a desktop app for both macOS and Windows.

- **Steps to Create a Prototype in Figma**:
  1. **Sign Up**: Create a free account on Figma.com and log in to access the dashboard.
  2. **Creating a New Design**:
     - Click on "New Design File" to start a new blank document.
     - Use the toolbar to create frames, shapes, and text elements.
  3. **Using Frames**:
     - Frames represent pages of the app.
     - Adjust frame properties such as dimensions and positions.
  4. **Adding Shapes and Text**:
     - Use the shape tool to create elements like buttons and checkboxes.
     - Add and customize text elements, including font size, weight, and color.
  5. **Creating Checkboxes**:
     - Draw rectangles and adjust their properties to create checkboxes.
     - Use plugins like Font Awesome Icons for symbols.
  6. **Auto Layout**:
     - Group elements together for easier manipulation.
     - Useful for creating rows of checkboxes and labels.
  7. **Final Adjustments**:
     - Customize the prototype by adding backgrounds, adjusting paddings, and refining the layout.

- **Practical Example**:
  - The instructor walks through creating a prototype for a Todo app, including frames, text, checkboxes, and an input box.

### Example Prototype Elements in Figma

1. **Frame**:
   - Represents a page in the app.
   - Set dimensions to desktop size.

2. **Shapes and Text**:
   - Create rectangles for buttons and checkboxes.
   - Add and style text for app titles and descriptions.

3. **Checkboxes**:
   - Use rectangles with adjusted properties for borders and fill.
   - Include both checked and unchecked versions.

4. **Auto Layout**:
   - Group related elements (e.g., checkbox and label) for easier movement and alignment.

5. **Input Box**:
   - Use text elements with auto layout to create input fields.
   - Customize background, padding, and corner radius.

### Benefits of Figma

- Facilitates the creation of detailed prototypes that guide the coding process.
- Enhances communication with stakeholders by providing a visual reference.
- Builds skills in a tool widely used in the industry, complementing Python programming knowledge.

By mastering prototyping with Figma, developers can streamline their workflow, reduce development time, and produce more polished and well-designed applications.

-------------------------

### Summary of the Hand-Drawn Design Video

In this video, the instructor explains the importance of creating a design before coding an application and discusses when it is appropriate to use a hand-drawn sketch instead of a digital tool like Figma. The focus is on efficiently planning simple, personal projects.

### Key Takeaways - 2

- **Design Before Coding**:
  - It is crucial to have a design plan before starting to code an application.
  - A design helps guide the coding process, making it more structured and efficient.

- **When to Use Hand-Drawn Sketches**:
  - For simple, personal projects, hand-drawn sketches can be more efficient than using digital tools like Figma.
  - Drawing by hand is quicker and sufficient for small-scale apps without clients or investors.
  - The simplicity and speed of hand-drawing make it ideal for straightforward projects.

- **Example Project**:
  - The instructor provides a hand-drawn sketch for a personal app with two pages: a homepage and a "Contact Me" page.
  - **Homepage**:
    - Includes a photo, some text, and app thumbnails with titles, descriptions, and source code links.
  - **Contact Me Page**:
    - Simple contact form for user interaction.

- **Efficiency Analogy**:
  - Using Figma for very simple projects is compared to using a crane to move a small package, whereas a hand-drawn sketch is like moving the package by hand—more practical and time-saving.

### Example Design Elements

1. **Homepage**:
   - A photo of the developer.
   - Text introducing the developer or the site.
   - Thumbnails of apps created, including titles, descriptions, and source code links.

2. **Contact Me Page**:
   - Simple contact form for visitors to reach out to the developer.

### Practical Advice

- **Efficiency in Design**:
  - Choose the appropriate design method based on the project's complexity and requirements.
  - Hand-drawn sketches are sufficient for quick, personal projects and help save time.

### Next Steps

- The instructor will transition to coding the application based on the hand-drawn design in the next video.

By understanding when to use hand-drawn sketches versus digital tools like Figma, developers can optimize their workflow, ensuring they use their time and resources effectively for each project's needs.

-------------------------

### Summary of Setting Up a Project in PyCharm and Connecting to Git Video

In this video, the instructor demonstrates how to set up a new project in PyCharm and connect it to a Git repository. This ensures that changes in the code are tracked and managed effectively.

### Key Takeaways - 3

- **Creating a New Project in PyCharm**:
  - Open a new project via the File menu and select New Project.
  - Choose a location to save the project and create an empty folder (e.g., App2-Portfolio).
  - Use a virtual environment (venv) for the project to manage dependencies.

- **Setting Up a Virtual Environment**:
  - Verify that the virtual environment is active by checking the terminal prompt, which should display the venv text.
  - Ensure that Python commands and code executions use the virtual environment.

- **Enabling Git Version Control**:
  - Enable Git by navigating to the VCS menu and selecting Enable version control integration.
  - A Git repository is created within the project.

- **Creating a .gitignore File**:
  - Create a .gitignore file to exclude certain files and directories (e.g., venv and .idea) from being tracked by Git.
  - Ensure the .gitignore file is correctly named and added to the repository.

- **Creating a README.md File**:
  - Create a README.md file to provide a description of the project.
  - Use Markdown syntax for formatting (e.g., `#` for H1 headings, `##` for H2 headings).

- **Committing Changes**:
  - Commit the initial changes (e.g., creation of .gitignore and README.md files) with a message (e.g., "Initial commit").
  - Verify that the committed files are added to the staging area and tracked by Git.

### Example Project Setup Steps

1. **Create a New Project**:

   ```python
   # Create a new project folder named App2-Portfolio
   ```

2. **Set Up Virtual Environment**:
   - Ensure the terminal shows the venv text.
   - Use the virtual environment for Python commands.

3. **Enable Git Version Control**:
   - Go to VCS > Enable version control integration > Select Git.

4. **Create .gitignore File**:

   ```plaintext
   # .gitignore
   venv/
   .idea/
   ```

5. **Create README.md File**:

   ```markdown
   # What is this project?
   To showcase Python projects.

   ## Features
   - Personal app portfolio
   - Contact form
   ```

6. **Commit Initial Changes**:
   - Go to the Commit tab, ensure .gitignore and README.md are checked.
   - Write a commit message (e.g., "Initial commit") and commit the changes.

### Final Notes

- By following these steps, you ensure that your project is well-organized and that changes are tracked efficiently.
- The setup process includes creating a virtual environment, enabling version control, and documenting the project with a README file.
- This foundational setup prepares you for coding the application in the next video.

By understanding and implementing these steps, developers can efficiently manage their projects and collaborate effectively using Git version control.

-------------------------

### Summary of Adding Data Sources and Images Video

In this video, the instructor explains how to identify repetitive items in your app design and use external data sources to handle them efficiently. The instructor then demonstrates how to add a CSV file and images to a project in PyCharm and commit these changes to a Git repository.

### Key Takeaways - 4

- **Identifying Data Sources**:
  - Look for repetitive items in your app design to determine the need for external data sources.
  - Examples: Titles, descriptions, images, and links that are repeated for multiple items.

- **Choosing a Data Format**:
  - For simple, non-nested data without relationships, CSV is preferred over JSON.
  - CSV files are easier to manually edit using tools like Microsoft Excel.

- **Setting Up Data Files**:
  - Create a `data.csv` file containing app information (titles, descriptions, URLs, and image paths).
  - Use a folder for storing image thumbnails corresponding to each app.

- **Example Data Structure**:
  - **CSV File**: Contains columns for title, description, URL, and image name.
  - **Images Folder**: Contains image files named to match entries in the CSV file.

- **Steps to Add Data Sources in PyCharm**:
  1. **Add `data.csv` File**:
     - Create a `data.csv` file with the necessary columns.
     - Include this file in the project folder.
  2. **Add Images Folder**:
     - Create a folder named `images` and include the image files.
     - Ensure each image file corresponds to an entry in the CSV file.

- **Data Handling in Python**:
  - The Python code will read the `data.csv` file and use the data to generate components on the website.
  - External data files ensure that updates to the data are reflected in the app without modifying the code.

- **Committing Changes to Git**:
  - Commit the `data.csv` file and images to the Git repository.
  - Use a commit message that describes the changes (e.g., "Add data source and image files").
  - Ensure all files are added to the repository and commit the changes.

### Example Project Setup Steps for Data Sources

1. **Create `data.csv` File**:

   ```plaintext
   Title;Description;URL;Image
   Todo App;A simple todo app;http://example.com;1.png
   Portfolio Website;Showcase of my projects;http://example.com;2.png
   ```

2. **Add Images Folder**:
   - Create a folder named `images` and include image files named `1.png`, `2.png`, etc.

3. **Commit Changes to Git**:
   - Go to the Git commit tab, ensure `data.csv` and images are checked.
   - Write a commit message (e.g., "Add data source and image files") and commit the changes.

### Final Notes - 4

- By using external data sources like CSV files and image folders, you can efficiently manage repetitive data in your app.
- This approach simplifies updates and ensures that the app structure is flexible and easy to maintain.
- The next step will involve coding the app to read and display this data, which will be covered in the following video.

By understanding how to set up and use external data sources, developers can create more dynamic and easily updatable applications.

-------------------------

### Summary of Coding the Homepage with Streamlit Video

In this video, the instructor begins coding the homepage of the personal app using Streamlit. The focus is on setting up the page layout, adding a photo, title, and a description about the developer.

### Key Takeaways - 5

- **Project Setup**:
  - Create a `main.py` file in the project directory.
  - The project structure includes `main.py`, `data.csv`, and an `images` folder.

- **Streamlit Installation**:
  - Install Streamlit using `pip install streamlit`.
  - Import Streamlit in the `main.py` file (`import streamlit as st`).

- **Setting Up the Homepage Layout**:
  - Use columns to structure the webpage with `st.columns(2)`.
  - Create two columns (`col1` and `col2`) using the `columns` method.

- **Adding Content to Columns**:
  - **Column 1**: Add an image using `st.image('images/photo.png')`.
  - **Column 2**: Add a title with the developer's name and a description using `st.write` or `st.info`.

- **Code Example for the Homepage**:

  ```python
  import streamlit as st

  st.set_page_config(layout="wide")

  col1, col2 = st.columns(2)

  with col1:
      st.image("images/photo.png", width=600)

  with col2:
      st.title("Your Name")
      description = """
      Your multi-line description about yourself goes here.
      """
      st.info(description)

  if __name__ == "__main__":
      st.run("main.py")
  ```

- **Running the Streamlit App**:
  - Use the terminal command `streamlit run main.py` to run the app.
  - The webpage will open in a browser, displaying the content in two columns.

- **Commit Changes**:
  - Commit the changes to the Git repository with a message like "Add initial homepage layout".

### Steps to Develop the Homepage

1. **Setup Project Structure**:
   - Ensure `main.py`, `data.csv`, and `images` folder are in place.

2. **Install Streamlit**:
   - Run `pip install streamlit` to install Streamlit.

3. **Import Streamlit**:
   - Import Streamlit in the `main.py` file.

4. **Configure Page Layout**:
   - Use `st.set_page_config(layout="wide")` to set the page layout to wide.

5. **Create Columns**:
   - Define two columns using `st.columns(2)`.

6. **Add Content**:
   - Add an image to the first column.
   - Add a title and description to the second column.

7. **Run the App**:
   - Use `streamlit run main.py` to run the app and view it in the browser.

8. **Commit Changes**:
   - Commit the initial setup to Git with a descriptive message.

### Final Notes - 5

- By following these steps, developers can set up a basic homepage with a structured layout using Streamlit.
- The next steps involve adding additional components to the homepage and coding the "Contact Me" page, as well as implementing navigation.

This approach ensures a clear and organized method to develop a web app using Streamlit, allowing for easy updates and enhancements as the project progresses.

-------------------------

### Summary of Real-World Exercise Introduction Video

In this video, the instructor introduces a real-world exercise that mimics tasks developers commonly perform, such as developing new features, adding to existing apps, and fixing bugs. The focus is on adding a new feature to the current project, reinforcing practical coding skills.

### Key Takeaways - 6

- **Real-World Developer Tasks**:
  - **Developing Apps from Scratch**: Creating new applications from the ground up.
  - **Adding Features**: Enhancing existing applications with new functionalities.
  - **Fixing Bugs**: Identifying and resolving issues in existing code.

- **Exercise Structure**:
  - **Feature Addition**: The current exercise involves adding a new content area to the existing app.
  - **Requirements**: The new content should stretch the full width of the webpage, below the existing columns.
  - **Resources**:
    - Existing code and resources are provided for convenience.
    - Example photo and other necessary files are included in the lecture resources.

- **Practical Skills**:
  - Learning to add new features and enhance existing projects.
  - Understanding the structure and layout adjustments in Streamlit.

### Exercise Requirements

1. **Add New Content Area**:
   - The new content should not be within the existing columns.
   - It should stretch across the full width of the webpage.
   - The content can be a simple text or any other relevant information.

2. **Utilize Provided Resources**:
   - Use the provided code and resources as a base.
   - Implement the changes according to the given requirements.

3. **Prepare for Further Enhancements**:
   - The current task is an introduction to adding features.
   - Be ready to add more columns and content in future exercises.

### Final Notes - 6

- This exercise is designed to simulate real-world tasks and enhance practical coding skills.
- Completing such exercises helps in understanding how to enhance and maintain existing projects efficiently.
- The next video will provide a solution and further guidance on the exercise.

By following these steps, developers can practice adding features to an existing project, preparing them for similar tasks in their professional careers.

-------------------------

### Summary of Real-World Exercise Introduction Video - 2

In this video, the instructor introduces a real-world exercise that mimics tasks developers commonly perform, such as developing new features, adding to existing apps, and fixing bugs. The focus is on adding a new feature to the current project, reinforcing practical coding skills.

### Key Takeaways

- **Real-World Developer Tasks**:
  - **Developing Apps from Scratch**: Creating new applications from the ground up.
  - **Adding Features**: Enhancing existing applications with new functionalities.
  - **Fixing Bugs**: Identifying and resolving issues in existing code.

- **Exercise Structure**:
  - **Feature Addition**: The current exercise involves adding a new content area to the existing app.
  - **Requirements**: The new content should stretch the full width of the webpage, below the existing columns.
  - **Resources**:
    - Existing code and resources are provided for convenience.
    - Example photo and other necessary files are included in the lecture resources.

- **Practical Skills**:
  - Learning to add new features and enhance existing projects.
  - Understanding the structure and layout adjustments in Streamlit.

### Exercise Requirements - 2

1. **Add New Content Area**:
   - The new content should not be within the existing columns.
   - It should stretch across the full width of the webpage.
   - The content can be a simple text or any other relevant information.

2. **Utilize Provided Resources**:
   - Use the provided code and resources as a base.
   - Implement the changes according to the given requirements.

3. **Prepare for Further Enhancements**:
   - The current task is an introduction to adding features.
   - Be ready to add more columns and content in future exercises.

### Example Code to Add New Content

```python
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Your Name")
    description = """
    Your multi-line description about yourself goes here.
    """
    st.info(description)

# New content area
st.write("### New Content Area")
st.write("This is the new content that stretches across the full width of the webpage. Add any relevant text or information here.")

if __name__ == "__main__":
    st.run("main.py")
```

### Steps to Complete the Exercise

1. **Review Existing Code**:
   - Ensure you understand the current structure and layout of the app.

2. **Add New Content**:
   - Use `st.write` or any relevant Streamlit method to add the new content area.
   - Ensure the content stretches across the full width of the webpage.

3. **Test the Changes**:
   - Run the app using `streamlit run main.py` to verify the new content appears as expected.

4. **Commit Changes**:
   - Commit the changes to the Git repository with a descriptive message (e.g., "Add new content area to homepage").

### Final Notes - 2

- This exercise is designed to simulate real-world tasks and enhance practical coding skills.
- Completing such exercises helps in understanding how to enhance and maintain existing projects efficiently.
- The next video will provide a solution and further guidance on the exercise.

By following these steps, developers can practice adding features to an existing project, preparing them for similar tasks in their professional careers.

-------------------------

## Day 22

### Summary of Adding Data to Columns with Pandas Video

In this video, the instructor demonstrates how to use Pandas to read data from a CSV file and display it in a Streamlit app. The focus is on rendering app titles into two columns on the webpage.

### Key Takeaways - 7

- **App Structure**:
  - The app displays app titles, descriptions, image thumbnails, and source code links in two columns.
  - Data for the app is stored in a `data.csv` file and images are stored in an `images` folder.

- **Using Pandas**:
  - **Importing Pandas**: Import Pandas using `import pandas as pd`.
  - **Reading CSV Data**: Use `pd.read_csv('data.csv', sep=';')` to read the CSV file.
  - **Iterating Over Rows**: Use `df.iterrows()` to iterate over the rows of the DataFrame.

- **Setting Up Columns**:
  - Create two new columns (`col3` and `col4`) using `st.columns(2)`.
  - Display data in the columns by iterating over the DataFrame rows and writing the titles to the respective columns.

### Code Example

```python
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Existing columns for photo and introduction
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Your Name")
    description = """
    Your multi-line description about yourself goes here.
    """
    st.info(description)

# Read data from CSV file
df = pd.read_csv('data.csv', sep=';')

# New columns for app titles
col3, col4 = st.columns(2)

# Display first 10 app titles in col3
with col3:
    for index, row in df.iloc[:10].iterrows():
        st.header(row['Title'])

# Display last 10 app titles in col4
with col4:
    for index, row in df.iloc[10:].iterrows():
        st.header(row['Title'])

if __name__ == "__main__":
    st.run("main.py")
```

### Steps to Implement

1. **Set Up Project Structure**:
   - Ensure `main.py`, `data.csv`, and `images` folder are in place.

2. **Install and Import Pandas**:
   - Install Pandas if not already installed (`pip install pandas`).
   - Import Pandas in the `main.py` file (`import pandas as pd`).

3. **Read CSV Data**:
   - Use `pd.read_csv('data.csv', sep=';')` to read the CSV file into a DataFrame.

4. **Create Columns**:
   - Use `st.columns(2)` to create two columns (`col3` and `col4`).

5. **Iterate Over DataFrame**:
   - Use `df.iterrows()` to iterate over the rows of the DataFrame.
   - Display titles in the respective columns using `st.header(row['Title'])`.

6. **Run the App**:
   - Use the terminal command `streamlit run main.py` to run the app.
   - Verify that the titles are displayed in two columns on the webpage.

7. **Commit Changes**:
   - Commit the changes to the Git repository with a descriptive message (e.g., "Render app titles into columns").

### Final Notes - 7

- By using Pandas to read and process CSV data, developers can efficiently manage and display structured data in their applications.
- This approach enhances the flexibility and maintainability of the app, allowing for easy updates and modifications.
- The next steps will involve adding more content and features to the app, further utilizing the power of Pandas and Streamlit.

By following these steps, developers can create a dynamic and organized web app, effectively displaying data in a user-friendly manner.

-------------------------

### Summary of Independent Project Introduction Video

In this video, the instructor assigns the first independent project, where learners will create a company webpage using Python and Streamlit. The goal is to apply the skills learned so far by building a real-world app based on given requirements.

### Key Takeaways - 8

- **Project Description**:
  - Build a company webpage for "The Best Company."
  - The webpage includes a company description, headers, team member photos, names, and roles.
  - Data for the project is provided in CSV files.

- **Project Requirements**:
  - Create a new PyCharm project and add the provided data files (`data.csv` and `images` folder).
  - Build the webpage to match the provided sketch.

- **Data Files**:
  - **data.csv**: Contains team member information (first name, last name, role, image file name).
  - **images**: Folder containing photos of team members.

- **Project Structure**:
  - Set up a new project in PyCharm.
  - Create a Python file (`main.py`) to code the webpage.

### Example Steps to Build the Webpage

1. **Set Up Project**:
   - Create a new PyCharm project.
   - Add the `data.csv` file and `images` folder to the project.

2. **Import Necessary Libraries**:
   - Import Streamlit and Pandas.
   - Ensure all necessary packages are installed.

3. **Read Data from CSV**:
   - Use Pandas to read `data.csv` and load the data into a DataFrame.

4. **Set Up Streamlit Page**:
   - Configure the Streamlit page layout.
   - Add a title and company description.

5. **Display Team Members**:
   - Create columns for displaying team member photos, names, and roles.
   - Iterate over the DataFrame to populate the columns with data.

### Final Notes - 8

- This exercise is designed to simulate real-world development tasks, reinforcing the skills learned throughout the course.
- Starting from scratch ensures you practice coding and become more comfortable with Python syntax and Streamlit usage.
- The next video will provide the instructor's solution and further guidance on the project.

By following these steps, you will create a fully functional company webpage, demonstrating your ability to apply Python and Streamlit in a practical project.

-------------------------

### Solution to the Independent Project - Company Webpage

In this video, the instructor walks through their solution to building the company webpage, providing a detailed explanation of each step and the corresponding code.

### Key Steps and Code Explanation

1. **Project Setup**:
   - The project includes an `images` folder with photos of team members and a `data.csv` file with team member information.

2. **Imports and Configuration**:
   - Import necessary libraries: Streamlit and Pandas.
   - Set the page layout to wide using `st.set_page_config(layout="wide")`.

3. **Header and Text**:
   - Add a header and a multi-line description using `st.header` and `st.write`.

4. **Reading Data**:
   - Read the `data.csv` file into a Pandas DataFrame without specifying a separator, as the default comma separator is used.

5. **Displaying Team Members**:
   - Create three columns using `st.columns(3)`.
   - Iterate over the DataFrame to extract and display team member information in the columns.
   - Use subheaders, write methods, and image methods to render the data.

### Example Code

```python
import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(layout="wide")

# Add header and description
st.header("The Best Company")
st.write("""
    Welcome to the official website of The Best Company. 
    We are dedicated to providing the best services in the industry.
    Our team consists of highly skilled professionals committed to excellence.
""")
st.subheader("Our Team")

# Create columns for team members
col1, col2, col3 = st.columns(3)

# Read data from CSV file
df = pd.read_csv('data.csv')

# Display team members in columns
for index, row in df.iloc[:4].iterrows():
    with col1:
        st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}", width=150)

for index, row in df.iloc[4:8].iterrows():
    with col2:
        st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}", width=150)

for index, row in df.iloc[8:12].iterrows():
    with col3:
        st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}", width=150)

if __name__ == "__main__":
    st.run("main.py")
```

### Detailed Explanation

1. **Import Statements**:
   - `import streamlit as st`
   - `import pandas as pd`

2. **Page Configuration**:

   ```python
   st.set_page_config(layout="wide")
   ```

3. **Header and Description**:

   ```python
   st.header("The Best Company")
   st.write("""
       Welcome to the official website of The Best Company. 
       We are dedicated to providing the best services in the industry.
       Our team consists of highly skilled professionals committed to excellence.
   """)
   st.subheader("Our Team")
   ```

4. **Creating Columns**:

   ```python
   col1, col2, col3 = st.columns(3)
   ```

5. **Reading Data from CSV**:

   ```python
   df = pd.read_csv('data.csv')
   ```

6. **Displaying Data in Columns**:
   - For the first four rows:

     ```python
     for index, row in df.iloc[:4].iterrows():
         with col1:
             st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
             st.write(row['role'])
             st.image(f"images/{row['image']}", width=150)
     ```

   - For the next four rows:

     ```python
     for index, row in df.iloc[4:8].iterrows():
         with col2:
             st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
             st.write(row['role'])
             st.image(f"images/{row['image']}", width=150)
     ```

   - For the last four rows:

     ```python
     for index, row in df.iloc[8:12].iterrows():
         with col3:
             st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
             st.write(row['role'])
             st.image(f"images/{row['image']}", width=150)
     ```

### Final Notes - 9

- This project demonstrates the application of Streamlit and Pandas to create a dynamic and data-driven web page.
- The exercise encourages independent coding practice, reinforcing the concepts learned in previous lessons.
- Comparing your solution with the instructor's code helps identify areas for improvement and understand different coding approaches.

By following this detailed explanation and example code, you can build a professional and functional company webpage, showcasing your ability to use Python and Streamlit effectively.

-------------------------

### Summary of Manual Python App Setup Without an IDE Video

In this video, the instructor demonstrates how to manually set up a Python project and create a virtual environment without using an IDE like PyCharm. This helps in understanding the underlying processes and making one a better programmer by avoiding the "black box" nature of IDEs.

### Key Takeaways - 10

- **Manual Project Setup**:
  - Learn to create Python projects without relying on an IDE.
  - Understand the steps to set up a virtual environment and manage Python files manually.

- **Steps for Manual Setup**:
  1. **Create a Project Directory**:
     - Create an empty folder for your project (e.g., `without_pycharm`).

  2. **Open Terminal in Project Directory**:
     - Navigate to the project directory and open a terminal window.

  3. **Create a Virtual Environment**:
     - Use the command `py -3.11 -m venv venv` on Windows or `python3.11 -m venv venv` on macOS/Linux.
     - This creates a `venv` folder containing the virtual environment.

  4. **Create a Python File**:
     - Create a `main.py` file using a text editor.
     - On macOS/Linux, you can use the `touch main.py` command in the terminal.

  5. **Edit the Python File**:
     - Open the `main.py` file in a simple text editor.
     - Write Python code (e.g., `print("Hello")`).

  6. **Run the Python File**:
     - Use the virtual environment's Python interpreter to run the file.
     - Command: `venv\Scripts\python main.py` on Windows or `venv/bin/python main.py` on macOS/Linux.

### Example Steps to Create and Run a Python File Manually

1. **Set Up Project Directory**:
   - Create an empty folder named `without_pycharm`.

2. **Open Terminal**:
   - Right-click the folder and select "Open in Terminal."

3. **Create Virtual Environment**:
   - Run the command:

     ```sh
     py -3.11 -m venv venv  # Windows
     python3.11 -m venv venv  # macOS/Linux
     ```

4. **Create Python File**:
   - Right-click in the folder and create a new text document named `main.py`.

5. **Edit Python File**:
   - Open `main.py` in a text editor and write:

     ```python
     print("Hello")
     ```

6. **Run Python File**:
   - In the terminal, run:

     ```sh
     venv\Scripts\python main.py  # Windows
     venv/bin/python main.py  # macOS/Linux
     ```

### Troubleshooting PyCharm Virtual Environment Issues

- **Setting Up Interpreter**:
  - If PyCharm does not recognize the virtual environment, go to settings and add a new interpreter.
  - Navigate to Project > Python Interpreter > Add.

- **Handling Existing Virtual Environment Issues**:
  - If there are issues with the existing virtual environment, delete the `venv` folder and create a new one.

### Final Notes - 10

- Understanding how to manually set up and run Python projects without an IDE enhances your programming skills.
- This knowledge helps in troubleshooting and managing Python environments more effectively.
- The next steps involve using the virtual environment and manually created files to further build and run Python applications.

By following these steps, you gain a deeper understanding of the processes involved in setting up and running Python projects, making you a more proficient and adaptable programmer.

-------------------------

## Day 23

### Summary of Adding a Navigation Menu with Streamlit Video

In this video, the instructor demonstrates how to add a navigation menu to a Streamlit web application. The navigation menu will allow users to switch between different pages of the website, such as the homepage and a contact page.

### Key Takeaways - 11

- **Adding a Sidebar Navigation Menu**:
  - Streamlit provides a simple way to create a multi-page app using a sidebar navigation menu.
  - The pages are organized in a specific directory named `pages`.

- **Steps to Add Pages**:
  1. **Create a Pages Directory**:
     - Create a directory named `pages` in the root project directory.
  2. **Add Python Files for Each Page**:
     - Create new Python files inside the `pages` directory for each page.
     - The names of these files will be used to generate the names of the pages in the sidebar.
  3. **Import Streamlit and Add Components**:
     - For each page, import Streamlit and add components such as headers or text.

- **Example Pages**:
  - **Contact Us Page**:
    - Create a `contact_us.py` file in the `pages` directory.
    - Add a header using `st.header("Contact Us")`.
  - **Test Page**:
    - Create a `test.py` file in the `pages` directory.
    - Add a text component using `st.write("Hello")`.

- **Renaming the Homepage**:
  - Rename the `main.py` file to `Home.py` to change the homepage title in the sidebar.

- **Running the Streamlit App**:
  - Restart the Streamlit app with the updated `Home.py` file to reflect the changes.

### Example Code and Steps

1. **Creating the `pages` Directory and Files**:
   - **Project Structure**:

     ```bash
     my_project/
     ├── Home.py
     ├── pages/
     │   ├── contact_us.py
     │   └── test.py
     ```

2. **Code for `contact_us.py`**:

   ```python
   import streamlit as st

   st.header("Contact Us")
   ```

3. **Code for `test.py`**:

   ```python
   import streamlit as st

   st.write("Hello")
   ```

4. **Renaming `main.py` to `Home.py`**:
   - Rename the file and update the Streamlit run command:

     ```sh
     streamlit run Home.py
     ```

### Steps to Implement the Navigation Menu

1. **Create the Pages Directory**:
   - Right-click in your project directory and create a new folder named `pages`.

2. **Add Python Files for Each Page**:
   - Create `contact_us.py` and `test.py` inside the `pages` folder.

3. **Add Content to Each Page**:
   - Open `contact_us.py` and add the following code:

     ```python
     import streamlit as st

     st.header("Contact Us")
     ```

   - Open `test.py` and add the following code:

     ```python
     import streamlit as st

     st.write("Hello")
     ```

4. **Rename the Homepage**:
   - Rename `main.py` to `Home.py` to update the homepage title.

5. **Run the Streamlit App**:
   - Stop any running Streamlit app.
   - Run the app with the new homepage file:

     ```sh
     streamlit run Home.py
     ```

6. **Verify the Changes**:
   - Open the web browser and verify that the sidebar contains links to "Home," "Contact Us," and "Test" pages.

7. **Commit the Changes**:
   - Commit the changes to your Git repository with a message like "Add navigation menu and contact us page."

### Final Notes - 11

- This video demonstrates the ease of creating a multi-page web application with Streamlit.
- By organizing pages into a `pages` directory and using appropriate file names, you can quickly set up a navigable sidebar.
- The next steps involve adding functionality to the contact form and implementing email sending capabilities.

By following these steps, you can enhance your Streamlit application with a user-friendly navigation menu, making it easier for users to navigate between different pages of your website.

-------------------------

### Summary of Building a Contact Form with Streamlit Video

In this video, the instructor demonstrates how to create a contact form using Python and Streamlit. The form allows visitors to input their email address and message, which will be sent to the website owner via email.

### Key Takeaways - 12

- **Form Components**:
  - A label for the form header.
  - A text input for the visitor's email address.
  - A text area for the visitor's message.
  - A submit button to send the form data.

- **Form Submission**:
  - When the submit button is pressed, the form data is processed.
  - The form data can be sent to a database, used to trigger an email, or display another page.

### Example Code to Create the Contact Form

1. **Import Streamlit**:

   ```python
   import streamlit as st
   ```

2. **Create the Form**:

   ```python
   st.header("Contact Us")

   with st.form(key='contact_form'):
       user_email = st.text_input("Your email address")
       message = st.text_area("Your message")
       submit_button = st.form_submit_button(label="Submit")
   
   if submit_button:
       st.write("Form submitted!")
       # Here you would add the code to send an email
   ```

3. **Explanation of Code**:
   - **Header**: `st.header("Contact Us")` adds a header to the contact page.
   - **Form**: The `st.form(key='contact_form')` creates a form with a unique key.
   - **Email Input**: `st.text_input("Your email address")` creates a text input for the user's email.
   - **Message Input**: `st.text_area("Your message")` creates a text area for the user's message.
   - **Submit Button**: `st.form_submit_button(label="Submit")` adds a submit button.
   - **Form Submission**: When the button is pressed, a message is displayed, and the form data can be processed (e.g., sent via email).

### Steps to Implement the Contact Form

1. **Set Up the Project**:
   - Ensure your Streamlit project is set up with a `contact_us.py` file in the `pages` directory.

2. **Create the Contact Form**:
   - Open `contact_us.py` and write the code to create the contact form.

3. **Run the Streamlit App**:
   - Start the Streamlit app using `streamlit run Home.py`.

4. **Test the Form**:
   - Open the web browser and navigate to the "Contact Us" page.
   - Fill out the form and press the submit button to see the form submission message.

5. **Prepare for Email Sending**:
   - Plan to add email sending functionality in the next steps.

### Final Notes - 12

- This video focuses on building the structure of the contact form.
- The next video will cover the functionality for sending emails when the form is submitted.
- Using the `st.form` and `st.form_submit_button` methods simplifies form creation and handling in Streamlit.

By following these steps, you can create a functional contact form on your Streamlit web application, ready to be enhanced with email sending capabilities in the next steps.

-------------------------

### Summary of Sending Emails with Python Video

In this video, the instructor demonstrates how to send emails using Python. The process is divided into two parts: writing a standalone script to send emails and integrating this script with a Streamlit contact form to send emails upon form submission.

### Key Takeaways - 13

- **Setting Up Email Sending**:
  - Use Gmail for simplicity and reliability.
  - Create an app password in Gmail for secure authentication in the script.

- **Writing the Email Sending Script**:
  - Store the sender's email address and app password in variables.
  - Use the `smtplib` library to create an email client session.
  - Configure the SMTP server and port for Gmail.
  - Use the `ssl` library to create a secure context.
  - Log in to the email server using the app password.
  - Send an email from the sender to the receiver.

### Step-by-Step Guide to Writing the Email Sending Script

1. **Set Up Gmail App Password**:
   - Enable two-step verification in your Gmail account.
   - Create an app password for Python.

2. **Write the Script**:

   ```python
   import smtplib
   import ssl

   # Gmail account credentials
   username = "your_email@gmail.com"
   password = "your_app_password"

   # SMTP server configuration
   smtp_server = "smtp.gmail.com"
   port = 465

   # Create secure SSL context
   context = ssl.create_default_context()

   # Email content
   receiver_email = "receiver_email@gmail.com"
   subject = "Hi"
   body = "How are you?\n\nBye"
   message = f"Subject: {subject}\n\n{body}"

   # Send email
   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
       server.login(username, password)
       server.sendmail(username, receiver_email, message)

   print("Email sent successfully.")
   ```

3. **Explanation of the Code**:
   - **Import Libraries**: Import `smtplib` for email sending and `ssl` for secure connections.
   - **Credentials**: Store the Gmail username and app password.
   - **SMTP Configuration**: Set the SMTP server (`smtp.gmail.com`) and port (465) for Gmail.
   - **SSL Context**: Create a secure SSL context.
   - **Email Content**: Define the receiver's email, subject, and body of the email.
   - **Send Email**: Use `smtplib.SMTP_SSL` to create a secure session, log in, and send the email.

### Testing the Script

1. **Run the Script**:
   - Execute the script and verify that an email is sent from the sender to the receiver.
   - Check the receiver's inbox to confirm receipt of the email.

2. **Handle Errors**:
   - If you encounter SSL errors on macOS, run the "Install Certificates.command" from the Python directory.
   - Ensure the correct use of argument names and values when creating the SMTP session.

### Integrating the Script with Streamlit Form

1. **Create a Contact Form in Streamlit**:
   - Create a contact form using `st.form`.
   - Add input fields for the user's email and message.
   - Add a submit button to the form.

2. **Connect the Form to the Email Script**:
   - When the form is submitted, use the email sending script to send the user's email and message to the website owner.

### Final Notes - 13

- This video provides a foundational understanding of how to send emails using Python.
- The next steps involve integrating this functionality with a web form in Streamlit, providing a complete and practical solution for contact forms on web applications.
- Ensure secure handling of credentials and consider using environment variables for added security.

By following these steps, you can create a Python script to send emails and integrate it with a web form to enhance your web applications with email functionality.

-------------------------

### Exercise: Adding a Contact Us Page with Streamlit

In this exercise, your task is to add a "Contact Us" page to the website. This page will allow users to send a message to the company, including their email address and a selected topic. The topics will be loaded from a CSV file. The email should be sent to a specified email address, including the user's email, the selected topic, and the message.

### Key Requirements

1. **Form Components**:
   - Text input for the user's email address.
   - Text area for the user's message.
   - Select box for the user to choose a topic (loaded from a CSV file).
   - Submit button.

2. **CSV File**:
   - The topics should be loaded from `topics.csv`, which contains the options "Job Inquiries", "Project Proposals", and "Other".

3. **Sending the Email**:
   - When the form is submitted, send an email containing the user's email, the selected topic, and the message.

### Steps to Implement the Exercise

1. **Set Up the Project**:
   - Ensure you have the `topics.csv` file in your project directory.
   - Create a `contact_us.py` file in the `pages` directory.

2. **Load Topics from CSV**:
   - Use Pandas to read the topics from `topics.csv`.

3. **Create the Form**:
   - Add the form components: text input for email, text area for message, select box for topics, and submit button.

4. **Handle Form Submission**:
   - On form submission, gather the data and send an email using the email sending script.

### Final Notes - 14

- This exercise combines form handling, reading data from a CSV file, and sending emails, providing a comprehensive practice scenario.
- The solution demonstrates the integration of various Python libraries to build a practical web application feature.
- Ensure you test the form thoroughly to confirm that emails are sent correctly with the provided details.

By completing this exercise, you will enhance your skills in creating interactive web forms, handling data, and integrating email functionality using Python and Streamlit.

-------------------------

### Solution to Adding a Contact Us Page with Streamlit

In this video, the instructor walks through the solution for adding a "Contact Us" page to the website. The page allows users to enter their email address, select a topic, and write a message. Upon form submission, an email is sent to the company.

### Key Steps in the Solution

1. **Import Necessary Libraries**:
   - Import Streamlit for building the web form.
   - Import the email sending script.
   - Import Pandas for reading the topics from a CSV file.

2. **Load Topics from CSV**:
   - Read the `topics.csv` file into a Pandas DataFrame.
   - Extract the topics as a list-like object to populate the select box.

3. **Create the Form**:
   - Add input fields for the user's email address and message.
   - Add a select box for the user to choose a topic.
   - Add a submit button.

4. **Handle Form Submission**:
   - Gather the form data when the submit button is pressed.
   - Construct the email body with the user's details.
   - Send the email using the email sending script.

### Complete Code

```python
import streamlit as st
import pandas as pd
import smtplib
import ssl

# Function to send email
def send_email(user_email, topic, message):
    sender_email = "your_email@gmail.com"
    app_password = "your_app_password"
    receiver_email = "receiver_email@gmail.com"
    subject = f"New Contact Us Message: {topic}"
    body = f"From: {user_email}\nTopic: {topic}\n\n{message}"
    email_message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, email_message)

# Load topics from CSV
topics_df = pd.read_csv('topics.csv')
topics = topics_df['topic'].tolist()

st.header("Contact Us")

# Create the form
with st.form(key='contact_form'):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("Topic", options=topics)
    message = st.text_area("Your message")
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    send_email(user_email, topic, message)
    st.success("Your message has been sent successfully!")
```

### Explanation of the Code

1. **Import Libraries**:
   - `import streamlit as st`: Import Streamlit for building the web application.
   - `import pandas as pd`: Import Pandas for reading CSV files.
   - `import smtplib, ssl`: Import libraries for sending emails securely.

2. **Send Email Function**:
   - Define a function `send_email` to send the email using the provided details.
   - Set up SMTP server configuration for Gmail.
   - Log in using the app password and send the email.

3. **Load Topics from CSV**:
   - Read the `topics.csv` file into a DataFrame.
   - Extract the topics column as a list.

4. **Create the Contact Form**:
   - Use `st.form` to create a form with a unique key.
   - Add a text input for the user's email address.
   - Add a select box for the topic using the loaded topics list.
   - Add a text area for the user's message.
   - Add a submit button.

5. **Handle Form Submission**:
   - When the form is submitted, call the `send_email` function with the form data.
   - Display a success message upon successful email sending.

### Testing the Solution

1. **Run the Streamlit App**:
   - Start the Streamlit app using `streamlit run contact_us.py`.

2. **Fill Out the Form**:
   - Enter an email address, select a topic, and write a message.
   - Press the submit button.

3. **Verify Email Sending**:
   - Check the receiver's inbox to confirm receipt of the email.

### Final Notes - 15

- This solution integrates form handling, CSV data reading, and email sending, providing a comprehensive and practical web application feature.
- Ensure secure handling of email credentials and consider using environment variables for added security.
- The ability to add dynamic components like a select box and handle form submissions is a valuable skill in web development.

By following this solution, you can create a functional "Contact Us" page that enhances your web application with user interaction and email functionality.

-------------------------

### Summary of Storing Passwords Securely with Environment Variables

In this video, the instructor demonstrates how to store passwords securely using environment variables. This is essential for protecting sensitive information, especially when collaborating with others or uploading code to version control platforms like GitHub.

### Key Takeaways - 16

1. **Problem Statement**:
   - Storing passwords directly in code as plain strings is insecure.
   - Sensitive information should be protected to prevent unauthorized access.

2. **Solution**:
   - Use environment variables to store sensitive information securely.
   - Environment variables are managed by the operating system and can be accessed by Python scripts without exposing the actual values in the code.

3. **Implementation Steps**:
   - Import the `os` module in Python.
   - Use `os.getenv()` to retrieve the environment variable's value.

### Steps to Store and Access Environment Variables

#### Windows

1. **Create Environment Variable**:
   - Open the Start menu and search for "Environment Variables."
   - Click on "Edit the system environment variables."
   - Click on the "Environment Variables" button.
   - Under "User variables," click "New."
   - Set the "Variable name" to `PASSWORD`.
   - Set the "Variable value" to your actual password.
   - Click "OK" to save.

2. **Access Environment Variable in Python**:

   ```python
   import os

   password = os.getenv("PASSWORD")
   print(password)  # This will print the password stored in the environment variable
   ```

#### macOS and Linux

1. **Create Environment Variable**:
   - Open the Terminal app.
   - Run the following commands:

     ```sh
     touch ~/.zshrc
     open ~/.zshrc
     ```

   - Add the following line to the file:

     ```sh
     export PASSWORD="your_password"
     ```

   - Save and close the file.

2. **Reload Environment Variables**:
   - Run the following command to reload the `.zshrc` file:

     ```sh
     source ~/.zshrc
     ```

3. **Access Environment Variable in Python**:

   ```python
   import os

   password = os.getenv("PASSWORD")
   print(password)  # This will print the password stored in the environment variable
   ```

### Integrating Environment Variables into the Email Sending Script

1. **Modify the Email Script**:
   - Use `os.getenv()` to retrieve the environment variables for the email credentials.

2. **Example Updated Script**:

   ```python
   import smtplib
   import ssl
   import os

   # Retrieve credentials from environment variables
   username = os.getenv("EMAIL_USER")
   password = os.getenv("EMAIL_PASSWORD")

   # SMTP server configuration
   smtp_server = "smtp.gmail.com"
   port = 465

   # Create secure SSL context
   context = ssl.create_default_context()

   # Email content
   receiver_email = "receiver_email@gmail.com"
   subject = "Hi"
   body = "How are you?\n\nBye"
   message = f"Subject: {subject}\n\n{body}"

   # Send email
   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
       server.login(username, password)
       server.sendmail(username, receiver_email, message)

   print("Email sent successfully.")
   ```

### Final Notes - 16

- Storing passwords securely using environment variables is a best practice for protecting sensitive information in your code.
- Environment variables ensure that passwords and other sensitive data are not exposed in the code, reducing the risk of unauthorized access.
- This approach is particularly important when sharing code with others or storing it in version control systems.

By following these steps, you can enhance the security of your Python applications, ensuring that sensitive information like passwords are stored securely and accessed safely.

## Day 24

### Summary of Building a PDF Template Generation App with Python

In this video, the instructor demonstrates how to start building a PDF template generation app using Python. The app will generate PDF documents programmatically, starting with creating a single-page PDF and then expanding to multiple pages. The FPDF library is used for this purpose.

### Key Takeaways - 17

1. **Set Up the Project**:
   - Create a new project directory.
   - Install and set up a virtual environment.
   - Install the FPDF library.

2. **Creating a Single Page PDF**:
   - Import the FPDF library.
   - Create an instance of the FPDF class.
   - Add a page to the PDF document.
   - Add text to the PDF using the `cell` method.
   - Set font and other text properties.

3. **Generating Multiple Pages**:
   - Use a loop to add multiple pages programmatically.
   - Automate the process of adding content to each page.

### Steps to Implement the PDF Generation

#### 1. Set Up the Project

1. **Create a New Project Directory**:
   - Create a new folder for the project (e.g., `app4_pdf_template`).

2. **Set Up Virtual Environment**:
   - Use PyCharm to create a new project with a virtual environment.
   - Alternatively, use the terminal to create a virtual environment:

     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install FPDF**:
   - Install the FPDF library:

     ```sh
     pip install fpdf
     ```

#### 2. Creating a Single Page PDF

1. **Import Libraries**:

   ```python
   from fpdf import FPDF
   ```

2. **Create PDF Instance**:

   ```python
   pdf = FPDF(orientation='P', unit='mm', format='A4')
   ```

3. **Add a Page**:

   ```python
   pdf.add_page()
   ```

4. **Set Font**:

   ```python
   pdf.set_font("Times", size=12)
   ```

5. **Add Text**:

   ```python
   pdf.cell(200, 10, txt="Hello there", ln=1, align='L', border=1)
   pdf.cell(200, 10, txt="Hi there", ln=1, align='L', border=1)
   ```

6. **Output PDF**:

   ```python
   pdf.output("output.pdf")
   ```

#### 3. Generating Multiple Pages

1. **Add Multiple Pages with Loop**:

   ```python
   for i in range(2):
       pdf.add_page()
       pdf.cell(200, 10, txt=f"Page {i+1}", ln=1, align='L', border=1)
   ```

2. **Output PDF with Multiple Pages**:

   ```python
   pdf.output("output_multiple_pages.pdf")
   ```

### Example Complete Code

```python
from fpdf import FPDF

# Create a PDF instance
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Times", size=12)

# Add text to the first page
pdf.cell(200, 10, txt="Hello there", ln=1, align='L', border=1)
pdf.cell(200, 10, txt="Hi there", ln=1, align='L', border=1)

# Add a second page
pdf.add_page()
pdf.cell(200, 10, txt="Second page", ln=1, align='L', border=1)

# Output the PDF
pdf.output("output.pdf")
```

### Final Notes - 17

- The `FPDF` library allows for flexible PDF generation, including setting font properties, adding text, and managing multiple pages.
- Understanding how to use loops to automate PDF content generation is crucial for handling documents with many pages.
- Future steps involve using data from CSV files and other sources to dynamically generate PDF content.

By following these steps, you can create a basic PDF generation app and expand it to generate complex PDF documents with multiple pages and dynamic content.

-------------------------

### Summary of Generating a PDF from CSV Data

In this video, the instructor demonstrates how to generate a PDF file from a CSV file using Python. The CSV file contains topics and page counts, which are used to create a structured PDF document with headers and multiple pages.

### Key Takeaways - 18

1. **Reading CSV Data**:
   - Use the `pandas` library to read and process CSV data into a DataFrame.
   - Iterate through the DataFrame to access each row's data.

2. **Generating PDF with FPDF**:
   - Use the `FPDF` library to create PDF documents.
   - Add pages and headers dynamically based on CSV data.

3. **Customizing PDF Content**:
   - Customize text properties like font size, color, and alignment.
   - Draw lines and other shapes to enhance the PDF layout.

### Steps to Implement PDF Generation from CSV

#### 1. Set Up the Project for PDF Generation - 1

1. **Create a New Project Directory**:
   - Create a new folder for the project (e.g., `app4_pdf_template`).

2. **Set Up Virtual Environment**:
   - Use PyCharm to create a new project with a virtual environment.
   - Alternatively, use the terminal to create a virtual environment:

     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install Required Libraries**:
   - Install the `pandas` and `FPDF` libraries:

     ```sh
     pip install pandas fpdf
     ```

4. **Prepare CSV File**:
   - Ensure the `topics.csv` file is in the project directory.

#### 2. Reading CSV Data

1. **Import Libraries**:

   ```python
   import pandas as pd
   from fpdf import FPDF
   ```

2. **Read CSV Data**:

   ```python
   df = pd.read_csv('topics.csv')
   ```

#### 3. Generating PDF with Headers and Pages

1. **Create PDF Instance**:

   ```python
   pdf = FPDF(orientation='P', unit='mm', format='A4')
   ```

2. **Iterate Through DataFrame**:

   ```python
   for index, row in df.iterrows():
       pdf.add_page()
       pdf.set_font("Arial", size=24)
       pdf.set_text_color(100, 100, 100)
       pdf.cell(0, 10, txt=row['Topic'], ln=True, align='L')
       pdf.line(10, 21, 200, 21)
   ```

3. **Output PDF**:

   ```python
   pdf.output("output.pdf")
   ```

#### 4. Customizing PDF Content

1. **Set Font and Text Color**:

   ```python
   pdf.set_font("Arial", size=24)
   pdf.set_text_color(100, 100, 100)
   ```

2. **Draw Lines**:

   ```python
   pdf.line(10, 21, 200, 21)
   ```

### Example Complete Code - 18

```python
import pandas as pd
from fpdf import FPDF

# Read CSV Data
df = pd.read_csv('topics.csv')

# Create PDF Instance
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Iterate Through DataFrame
for index, row in df.iterrows():
    # Add a new page
    pdf.add_page()
    
    # Set font and text color
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(100, 100, 100)
    
    # Add header
    pdf.cell(0, 10, txt=row['Topic'], ln=True, align='L')
    
    # Draw line below header
    pdf.line(10, 21, 200, 21)

# Output PDF
pdf.output("output.pdf")
```

### Final Notes - 18

- Using `pandas` for data manipulation and `FPDF` for PDF generation allows for flexible and dynamic document creation.
- Customizing the PDF content with different fonts, colors, and shapes enhances the document's readability and presentation.
- Iterating through CSV data and dynamically creating PDF pages ensures scalability for larger datasets.

By following these steps, you can create a robust PDF generation app that reads data from CSV files and produces well-structured PDF documents with multiple pages and custom content.

-------------------------

### Summary of Adding Multiple Pages for Each Topic in PDF

In this video, the instructor demonstrates how to generate a PDF file with multiple pages for each topic listed in a CSV file using Python. The CSV file contains topics and the number of pages each topic should have. The instructor emphasizes the use of for loops, specifically nested for loops, to achieve this task.

### Key Takeaways - 19

1. **Using Nested For Loops**:
   - A nested for loop is used to iterate through the topics and create the required number of pages for each topic.

2. **Working with Python Ranges**:
   - The `range()` function is used to create a list-like sequence of numbers, which helps in iterating a specific number of times.

3. **Dynamic PDF Page Creation**:
   - The `FPDF` library is utilized to create a PDF document with multiple pages dynamically based on the input data from the CSV file.

### Steps to Implement Multiple Pages for Each Topic in PDF

#### 1. Set Up the Project for PDF Generation - 2

1. **Create a New Project Directory**:
   - Create a new folder for the project (e.g., `app4_pdf_template`).

2. **Set Up Virtual Environment**:
   - Use PyCharm to create a new project with a virtual environment.
   - Alternatively, use the terminal to create a virtual environment:

     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install Required Libraries**:
   - Install the `pandas` and `FPDF` libraries:

     ```sh
     pip install pandas fpdf
     ```

4. **Prepare CSV File**:
   - Ensure the `topics.csv` file is in the project directory.

#### 2. Reading CSV Data - 2

1. **Import Libraries**:

   ```python
   import pandas as pd
   from fpdf import FPDF
   ```

2. **Read CSV Data**:

   ```python
   df = pd.read_csv('topics.csv')
   ```

#### 3. Generating PDF with Headers and Multiple Pages

1. **Create PDF Instance**:

   ```python
   pdf = FPDF(orientation='P', unit='mm', format='A4')
   ```

2. **Iterate Through DataFrame**:

   ```python
   for index, row in df.iterrows():
       # Add the initial page with header
       pdf.add_page()
       pdf.set_font("Arial", size=24)
       pdf.set_text_color(100, 100, 100)
       pdf.cell(0, 10, txt=row['Topic'], ln=True, align='L')
       pdf.line(10, 21, 200, 21)
       
       # Add additional pages
       for _ in range(row['Pages'] - 1):
           pdf.add_page()
   ```

3. **Output PDF**:

   ```python
   pdf.output("output.pdf")
   ```

### Example Complete Code - 19

```python
import pandas as pd
from fpdf import FPDF

# Read CSV Data
df = pd.read_csv('topics.csv')

# Create PDF Instance
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Iterate Through DataFrame
for index, row in df.iterrows():
    # Add the initial page with header
    pdf.add_page()
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, txt=row['Topic'], ln=True, align='L')
    pdf.line(10, 21, 200, 21)
    
    # Add additional pages
    for _ in range(row['Pages'] - 1):
        pdf.add_page()

# Output PDF
pdf.output("output.pdf")
```

### Final Notes - 19

- Using nested for loops and the `range()` function allows for efficient and dynamic creation of multiple pages in a PDF.
- Customizing the PDF content with different fonts, colors, and shapes enhances the document's readability and presentation.
- Iterating through CSV data and dynamically creating PDF pages ensures scalability for larger datasets.

By following these steps, you can create a robust PDF generation app that reads data from CSV files and produces well-structured PDF documents with multiple pages and custom content for each topic.

-------------------------

### Summary of Adding Footers to Each Page in PDF

In this video, the instructor explains how to add footers to each page of a PDF document generated using Python. The footers will include the topic name, ensuring that users can keep track of the pages they are working on. The focus is on using for loops to iterate through the pages and adding the footer at the appropriate position on each page.

### Key Takeaways - 20

1. **Adding Footers to PDF Pages**:
   - Learn how to add footers to each page in a PDF document.
   - Understand the importance of setting the correct position for footers.

2. **Using FPDF Library**:
   - Utilize the `FPDF` library to create and manipulate PDF files.

3. **Configuring Auto Page Breaks**:
   - Disable automatic page breaks to manually control the placement of footers.

4. **Nested For Loops**:
   - Use nested for loops to iterate through each topic and its respective pages to add the footer.

### Steps to Implement Footers in PDF

#### 1. Set Up the Project for PDF Generation - 3

1. **Create or Open Project**:
   - Continue with the existing project or create a new one in PyCharm.
   - Ensure you have the `topics.csv` file in the project directory.

2. **Install Required Libraries**:
   - Ensure `pandas` and `FPDF` libraries are installed:

     ```sh
     pip install pandas fpdf
     ```

#### 2. Reading CSV Data - 3

1. **Import Libraries**:

   ```python
   import pandas as pd
   from fpdf import FPDF
   ```

2. **Read CSV Data**:

   ```python
   df = pd.read_csv('topics.csv')
   ```

#### 3. Generating PDF with Headers, Multiple Pages, and Footers

1. **Create PDF Instance**:

   ```python
   pdf = FPDF(orientation='P', unit='mm', format='A4')
   pdf.set_auto_page_break(auto=False, margin=0)
   ```

2. **Iterate Through DataFrame**:

   ```python
   for index, row in df.iterrows():
       # Add the initial page with header
       pdf.add_page()
       pdf.set_font("Arial", size=24)
       pdf.set_text_color(100, 100, 100)
       pdf.cell(0, 10, txt=row['Topic'], ln=True, align='L')
       pdf.line(10, 21, 200, 21)
       
       # Add footer for the master page
       pdf.ln(270)
       pdf.set_font("Arial", style='I', size=8)
       pdf.set_text_color(180, 180, 180)
       pdf.cell(0, 10, txt=row['Topic'], ln=True, align='R')
       
       # Add additional pages
       for _ in range(row['Pages'] - 1):
           pdf.add_page()
           # Add footer for additional pages
           pdf.ln(277)
           pdf.set_font("Arial", style='I', size=8)
           pdf.set_text_color(180, 180, 180)
           pdf.cell(0, 10, txt=row['Topic'], ln=True, align='R')
   ```

3. **Output PDF**:

   ```python
   pdf.output("output.pdf")
   ```

### Example Complete Code - 20

```python
import pandas as pd
from fpdf import FPDF

# Read CSV Data
df = pd.read_csv('topics.csv')

# Create PDF Instance
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

# Iterate Through DataFrame
for index, row in df.iterrows():
    # Add the initial page with header
    pdf.add_page()
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, txt=row['Topic'], ln=True, align='L')
    pdf.line(10, 21, 200, 21)
    
    # Add footer for the master page
    pdf.ln(270)
    pdf.set_font("Arial", style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, txt=row['Topic'], ln=True, align='R')
    
    # Add additional pages
    for _ in range(row['Pages'] - 1):
        pdf.add_page()
        # Add footer for additional pages
        pdf.ln(277)
        pdf.set_font("Arial", style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=row['Topic'], ln=True, align='R')

# Output PDF
pdf.output("output.pdf")
```

### Final Notes - 20

- Adding footers to each page ensures users can keep track of the pages they are working on.
- Disabling automatic page breaks gives more control over the layout of the PDF document.
- Using nested for loops allows for efficient handling of multiple topics and their respective pages.

By following these steps, you can create a well-structured PDF document with multiple pages per topic and custom footers on each page, enhancing the usability of the document for note-taking and other purposes.

-------------------------

### Exercise: Adding Horizontal Lines to PDF Pages

The task for this exercise is to improve the existing PDF generation program by adding horizontal lines to each page of the document. The lines should be evenly spaced, with a suggested distance of 10 millimeters between them. The other elements of the document, such as the headers and footers, should remain the same.

### Steps to Add Horizontal Lines

1. **Set Up the Project**:
   - Ensure you have the existing project set up with `main.py` and `topics.csv`.
   - Ensure `pandas` and `FPDF` libraries are installed.

2. **Read CSV Data**:
   - Import the necessary libraries and read the CSV file as done previously.

3. **Generate PDF with Headers, Footers, and Horizontal Lines**:
   - Create the PDF instance.
   - Iterate through the DataFrame to add pages, headers, footers, and horizontal lines.

### Final Notes - 21

- Adjust the `y_start` and `line_height` values in the `add_horizontal_lines` function as needed to change the starting position and distance between lines.
- Ensure the text color and font settings match your requirements.
- Save and run the script to generate the updated PDF document with horizontal lines on each page.

By following these steps, you can create a well-structured PDF document with headers, footers, and horizontal lines, enhancing the usability of the document for note-taking and other purposes.

-------------------------

### Summary of Video on Python Code Style Guide (PEP 8)

In this video, the instructor covers PEP 8, the style guide for Python code, which provides recommendations for making Python code more readable and standardized. The instructor emphasizes that adhering to PEP 8 ensures consistency and readability, which is crucial for collaboration among programmers.

### Key Takeaways - 22

- **PEP 8 Introduction**
  - PEP 8 is the style guide for Python code, providing recommendations to enhance code readability and consistency.
  - Available at [PEP 8](https://peps.python.org/pep-0008).

- **Indentation**
  - Use four spaces per indentation level.
  - Avoid using tabs; prefer spaces for indentation.

- **Line Length**
  - Limit lines to a maximum of 79 characters.
  - Use a vertical line in the code editor to indicate the 79-character limit.

- **Line Breaks**
  - Break lines before operators.
  - Ensure lines are broken logically for readability.

- **Blank Lines**
  - Use blank lines to separate related blocks of code.
  - Functions should have two blank lines around them.

- **Import Statements**
  - Place all import statements at the top of the file.

- **String Quotes**
  - Be consistent with using single or double quotes for strings.
  - Use triple double quotes for multi-line strings.

- **White Space**
  - Use white space around operators but not inside parentheses, brackets, or braces.
  - Follow English grammar rules for spacing.

- **Comments**
  - Begin comments with a space after the `#` symbol.
  - Write comments as complete sentences.
  - Avoid inline comments; place comments above the relevant code.

- **Documentation Strings (Docstrings)**
  - Place docstrings immediately after the function definition.
  - Docstrings should describe what the function does.

- **Naming Conventions**
  - Use lowercase and underscores for variable and function names.
  - Use uppercase and underscores for constants.
  - Use CamelCase for class names.

These guidelines help ensure that Python code is clean, readable, and maintainable, facilitating better collaboration among developers.

-------------------------

## Day 25

### Summary of Video on Building an Excel Processing App

In this video, the instructor introduces the fourth app project in the course, which focuses on processing Excel files to generate PDF invoices. The instructor demonstrates what the final app will look like and explains the key functionalities and learning benefits for the students.

### Key Takeaways - 23

- **App Overview**
  - The app will process Excel files containing invoice data and generate corresponding PDF invoices.
  - Each Excel file represents a separate invoice with data about products or services purchased, including quantity and price.

- **Excel Files**
  - The app will read multiple Excel files from a specified folder.
  - Each file contains invoice data entered by company employees.
  - The file names include the invoice number and date, which will be extracted by the app.

- **PDF Invoice Generation**
  - The app will generate a PDF invoice for each Excel file.
  - Invoice details such as invoice number, date, product details, and total price will be included.
  - The total price will be calculated by the app and displayed on the PDF invoice.

- **Learning Benefits**
  - **Pandas Library**: Gain deeper knowledge of using the pandas library for reading and processing Excel files (also applicable to CSV files).
  - **File Handling**: Improve skills in working with files, including extracting information from file paths and file names.
  - **For Loops**: Practice and enhance the use of for loops for iterating over data.

This app project aims to enhance practical skills in file processing, data extraction, and automation using Python, making it a valuable exercise for learners.

-------------------------

### Summary of Video on Starting the Excel Processing App

In this video, the instructor provides a tip to enhance learning, explains the initial setup for the new project, and discusses the decision on whether to include a graphical user interface (GUI) for the app.

### Key Takeaways - 24

- **Learning Tip**
  - Pause the video before the instructor writes code to try coding it yourself. This helps in problem-solving and learning from mistakes.

- **Project Setup**
  - Create a new project in your IDE.
  - Place the provided Excel files in a directory within the project.
  - Enable version control (Git) and create a `.gitignore` file to exclude unnecessary files from version control.
  - Create a `README.md` file to describe the project.

- **Understanding the App**
  - The app will process Excel files containing invoice data and convert them into PDF invoices.
  - Each Excel file corresponds to an invoice with details such as product ID, product name, quantity purchased, price per unit, and total price.

- **GUI Considerations**
  - Decide whether the app needs a graphical user interface based on the intended users.
  - For a wide audience, consider a web app or desktop GUI.
  - For internal use or a small pool of users, a command-line script might suffice.
  - This app will be a command-line script for simplicity and automation.

This setup and initial planning are crucial for understanding the scope of the project and preparing the environment for efficient development.

-------------------------
