# Bash Scripting

## Introduction to Bash Scripting

- Bash or shell scripting is a great way to automate repetitive tasks and can save you a lot of time.
- Bash scripts execute within a Bash shell interpreter terminal. Any command you can run in your terminal can be run in a Bash script.
- When you have a command or set of commands that you will be using frequently, consider writing a Bash script to save time.

### Begining of Bash Scripting

- There are some conventions that you should follow when writing a Bash script.
- The beginning of script should start with "#!/bin/bash" which is called a shebang.
- When saving the script, it is good practice to place commonly used scripts in the "~/bin/" directory.
- The script files also need to have the execute permission set. This can be done with the chmod command.

```bash
chmod +x script.sh
```

- Your terminal runs a file every time it is opened. This file is called the "~/.bashrc" file in Linux, "~/.bash_profile" in OSX. To ensure that scripts in "~/bin/" are available to run, you must add this directory to your PATH within your configuration file. "PATH=~/bin:$PATH"
- Now any scripts in the "~/bin/" directory can be run from anywhere in the terminal.

## Variables

- Variables are declared by setting the variable name equal to another value. Example: "variable=value". Note that there is no space between the variable name, the equals sign, and the value.
- To access the value of a variable, you must place a dollar sign ($) in front of the variable name. Example: "$variable".

## Conditionals

- You can use conditionals to control which set of commands within the script run. Use "if" to start the conditional, followed by the condition in square brackets. Make sure you leave a space between the square brackets and the condition.
- "then" begins the code that will run if the condition is met. "else" begins the code that will run if the condition is not met.
- Lastly, "fi" ends the conditional.

```bash
if [ condition ]
then
    # code that runs if the condition is true
else
    # code that runs if the condition is false
fi
```

```bash
if  [ $index -lt 5]
then
    echo $index
else
    echo 5
fi
```

- You can use a specific list of operators for comparison. Here are some of the most common operators:
  - "-eq" : equal
  - "-ne" : not equal
  - "-lt" : less than
  - "-le" : less than or equal
  - "-gt" : greater than
  - "-ge" : greater than or equal
  - "-z" : string is null, that is, has zero length
- When comparing strings, it is best practice to put the variable into double quotes (""). This prevents errors if the variable is null or contains spaces. The common operators for comparing strings are:
  - "=" : equal
  - "!=" : not equal
  - "-z" : string is null, that is, has zero length

```bash
if [ "$foo" == "$bar" ]
then
    echo "foo is equal to bar"
fi
```

## Loops

- Loops are used to iterate over a block of code until a condition is met. There are three main types of loops in Bash:

### For Loop

- The for loop is used to iterate over a list of items and perform the same action for each item in the list.

```bash
list="apple banana cherry"
for item in $list
do
    echo $item
done
```

- Note that item is being defined at the beginning of the loop. This is the variable that will hold the value of the current item in the list. When accessing the variable within the loop, you must place a dollar sign ($) in front of the variable name.

### While Loop

- The while loop is used to iterate over a block of code as long as the condition is true.
- Conditions are established the same way as with the if statement.

```bash
while [ $index -lt 5 ]
do
    echo $index
    index=$((index + 1))
done
```

- Note that arithmetic operations are done within double parentheses. This is because the arithmetic operation is evaluated before the result is assigned to the variable.

### Until Loop

- The until loop is used to iterate over a block of code as long as the condition is false.

```bash
until [ $index -eq 5 ]
do
    echo $index
    index=$((index + 1))
done
```

## Inputs

- We need to be able to access data external to the bash script file itself. The first way to do this is by prompting the user for input.
- For this, we use the "read" syntax. To ask the user for input and save it to the "number" variable.

```bash
echo "Enter a number: "
read number
echo "You entered: $number"
```

- Another way to access external data is to have the user add input arguments when running the script.
- These arguments are entered after the script name and are speerated by spaces.

```bash
saycolors red green blue
```

- Within the script, these are accessed by the variables $1, $2, $3, and so on. Wherer $1 is the first argument(red). Note that these are 1 indexed.
- If your script needs to accept an indefinite number of arguments, you can use the "$@" variable. This variable contains all the arguments passed to the script.

```bash
for color in "$@"
do
    echo $color
done
```

- We can access external files to our script. You can assign a set of files to a variable name using standard bash pattern matching using regular expressions.
- Get all files in the a directory, you can use the "*" character. This iterate through each file and print the full path and filename.

```bash
files=/some/directory/*
for file in $files
do
    echo $file
done
```

## Aliases

- You can set up aliases for your bash scripts within your "~/.bashrc" file or ".bash_profile" file to allow scripts without the full filename.
- To create an alias, use the "alias" command followed by the alias name and the command you want to run.

```bash
alias saycolors='/path/to/saycolors.sh'
```

- You can even add standard input arguments to the alias.

```bash
alias saycolors='/path/to/saycolors.sh red green blue'
```

- You can write these commands to terminal. You can also add these to your "~/.bashrc" file or ".bash_profile" file to make them permanent.

## Review

- Review what you’ve learned about
  - Any command that can be run in the terminal can be run in a bash script.
  - Variables are assigned using an equals sign with no space (greeting="hello").
  - Variables are accessed using a dollar sign (echo $greeting).
  - Conditionals use if, then, else, fi syntax.
  - Three types of loops can be used: for, while, and until.
  - Bash scripts use a unique set of comparison operators:
    - Equal: -eq
    - Not equal: -ne
    - Less than or equal: -le
    - Less than: -lt
    - Greater than or equal: -ge
    - Greater than: -gt
    - Is null: -z
  - Input arguments can be passed to a bash script after the script name, separated by spaces (myScript.sh “hello” “how are you”).
  - Input can be requested from the script user with the read keyword.
  - Aliases can be created in the .bashrc or .bash_profile using the alias keyword.

# Project: Build a Build Script

- One common use of bash scripts is for releasing a “build” of your source code. Sometimes your private source code may contain developer resources or private information that you don’t want to release in the published version.
- In this project, you’ll create a release script to copy certain files from a source directory into a build directory.

```bash
#!/bin/bash
echo "🔥🔥🔥 Beginning build!! 🔥🔥🔥"
firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< $firstline
version=${splitfirstline[1]}
echo "You are building version" $version
echo "Do you want to continue? (enter "1" for yes, "0" for no)"
read versioncontinue
if [ $versioncontinue -eq 1 ]
then
  echo "OK"
else
  echo "Please come back when you are ready"
fi
for filename in source/*
do
  echo $filename
  if [ "$filename" == "source/secretinfo.md" ]
  then
    echo "Not copying" $filename
  else
    echo "Copying" $filename
    cp $filename build/.
  fi
done
cd build/
echo "Build version $version contains:"
ls
cd ..
```

- This script will copy all files from the source directory to the build directory except for the secretinfo.md file.
