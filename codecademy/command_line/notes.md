# Introduction to Command Line

## What is the Command Line?

- The command line is a text interface for the computer's operating system. You can use it to traverse and edit your computer's filesystem. You can create new files, edit existing files, delete files and run programs.
- On Mac and Linux systems, we can access command line through Bash. Windows users can download Bash.
- This course will take you through the various functionalities of how to use the command line, starting with navigation, and ending with configuring the environment.

## Navigation

- You will learn how to navigate through a computer’s filesystem solely through the command line. You’ll learn how to view the contents of your filesystem, move through the different directories (folders), and make new files and directories.

### Introduction to Navigation

- The command line is a text interface for the computer's operating system. It's a program that takes in commands and passes them on to the computer to run.
- It is like Finder on Mac OS, or Windows Explorer on Windows. The difference is that the command line is fully text-based.
- Its main advantage is that you can run programs, write scripts to automate common tasks, and combine simple commands to handle diffucult tasks.
- In the terminal, the first thing you see is "$". This is called the shell prompt. It is where you enter commands.

### Filesystem

- A filesystem organizes a computer's files and directiories into a tree structure:
    1. The first directory in the filesystem is the root directory. It is the base of the filesystem.
    2. Each parent directory can contain more child directories and files.
    3. Each directory can contain more files or directories. The parent-child relationship continues.
- [Filesystem](filesystem.png)

### ls

- The `ls` command lists the contents of the current directory.
- `ls` stands for "list".

### pwd

- The `pwd` command stands for "print working directory". It outputs the name of the current directory.

### cd

- The `cd` command stands for "change directory". It changes the current directory to the one you specify.
- "cd .." moves up one directory.
- "cd /directory" moves to the specified directory.
- "cd /directory/subdirectory" moves to the specified subdirectory.
- "cd" moves to the home directory.
- "cd ~" moves to the home directory.
- "cd ../.." moves up two directories.
- "cd ../directory" moves up one directory and then to the specified directory.

### mkdir

- The `mkdir` command stands for "make directory". It creates a new directory in the current directory.
- "mkdir directory" creates a new directory called "directory".

### touch

- The `touch` command creates a new file in the current directory.
- "touch file.txt" creates a new file called "file.txt".

### Helper Commands

- "tab" can be used to autocomplete a command.
- "up arrow" can be used to see the previous command.
- "clear" can be used to clear the terminal.
- "down arrow" can be used to see the most previous command.

### Review

- You’ve learned five commands commonly used to navigate the filesystem from the command line. What can we generalize so far?
  - The command line is a text interface for the computer’s operating system. To access the command line, we use the terminal.
  - A filesystem organizes a computer’s files and directories into a tree structure. It starts with the root directory. Each parent directory can contain more child directories and files.
  - From the command line, you can navigate through files and folders on your computer:
    - pwd outputs the name of the current working directory.
    - ls lists all files and directories in the working directory.
    - cd switches you into the directory you specify.
    - mkdir creates a new directory in the working directory.
    - touch creates a new file inside the working directory.
  - You can use helper commands to make navigation easier:
    - clear clears the terminal
    - tab autocompletes the name of a file or directory
    - ↑ and ↓ allow you to cycle through previous commands

## Project: Bicycle World

- Welcome to Bicycle World, the premier text-based bicycle shop! This shop is only accessible to programmers like you, who are familiar with the command line.
- In this project, you’ll use the commands you learned to navigate and edit the filesystem of this special shop.
- The starting filesystem is shown below. (Bicycle World recently changed owners, who named the main directory bicycle-world-ii.)

```bash
bicycle-world-ii
|—— brands.txt
|—— freight/
|   |—— messenger/
|   |—— porteur/
|—— mountain/
|   |—— downhill/
|   |   |—— heavyweight/
|   |   |—— lightweight/
|   |—— hardtail/
|—— racing/
    |—— road/
    |—— track/
```

```bash
# 1. Print the working directory
pwd
# 2. List all files and directories in the working directory
ls
# 3. Change the working directory to the freight directory
cd freight
# 4. List all files and directories in the working directory
ls
# 5. Change the working directory to the porteur directory
cd porteur
# 6. Change the working directory to bicycle-world-ii directory and list all files and directories in the working directory
cd ../../
ls
# 7. Change the working directory to the mountain/downhill directory
cd mountain/downhill
# 8. Create a new file called "dirt.txt"
touch dirt.txt
# 9. Create a new file called "mud.txt"
touch mud.txt
# 10. List all files and directories in the working directory
ls
# 11. Make a directory called "safety"
mkdir safety
# 12. Change the working directory to the bicycle-world-ii directory and list all files and directories in the working directory
cd ../../
ls
# 13. Create a new directory called "bmx"
mkdir bmx
# 14. Without changing the working directory, make a file in the "bmx" directory called "tricks.txt"
touch bmx/tricks.txt
# 15. List all files and directories in the working directory
ls
```

##  Manipulation

- You will learn how to manipulate the contents of the filesystem with the command line. You’ll learn how to move files, delete files and directories, and more.

### Introduction to Manipulation

- We can view directories and files with more detail. We can also use the command line to copy, move, and remove files and directories.

###  ls (revisited)

- The `ls` command lists the contents of the current directory. We can use flags to view more information.
- `ls -a` lists all contents, including hidden files and directories. This command displays all the files and directories, including those starting with a dot. These files are usually hidden.
- `ls -l` lists all contents in long format. This command displays all the files and directories in the current directory in long format. This includes the file permissions, the number of links, the owner, the group, the size, the date, and the name of the file or directory.
- `ls -t` lists all contents by modification time. This command displays all the files and directories in the current directory, ordered by the time they were last modified.
- [Filesystem](ls-command-filesystem.png)

## Redirection

- You will learn how to redirect standard input, standard output, and standard error messages. You’ll learn how to display the contents of a file, write to that file, search through directories, and more.

## Configuration

- You will learn how to configure your local environment. You’ll learn how to set and edit your settings and preferences, assign aliases (shortcuts), how to use nano, and more.
