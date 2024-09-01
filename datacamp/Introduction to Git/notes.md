# Introduction to Git Course at DataCamp

## Introduction to Version Control with Git

### Version

- Contents of a file at a given point in a time
- Metadata information associated with the file

### Version Control

- Version control is a group of systems and processes
  - to manage changes made to documents, programs, and directories
- Version control is useful for anything that:
  - changes over time
  - needs to be shared
- Track files in different states
- Simultaneous file development
- Combine different versions
- Identify a particular version of a file
- Revert changes

### Git

- Open source, scalable
- Stores everything
- Notifies us when our work conflicts  with someone else’s
- Synchronize work
- Git commands are run on the shell

### Useful Shell Commands

- pwd: see our directory
- ls: see what is inside our directory. “ls -a” shows the hidden files and directories
- cd: go inside the directory inside our directory
- nano: delete, add or change contents of a file. Save changes Ctrl + O, exit the text editor: Ctrl + X
- echo: create or edit a file. > create a file, >> add the new content.

## Saving Files

### Repository

- There are two parts. First is the files and directories that we create and edit. Second is the extra information that Git records about the project’s history. The combination of these two is called a repository.
- Git stores all the extra information in a directory “.git”. Git expects to should not edit or delete this directory.

### Staging and Committing

- “git add .”: add the whole files to staging area.
- git commit -m “log message”: we can commit the staging area to GitHub. Log message need to be short and precise.
- “git status”: Tells us which files in the staging area, and which files have changes that aren’t in the area yet.

## Comparing Files

- git diff [name of the file]: show the differences of the unstated and committed of the file. “-“ is the deleted lines, “+” is the added lines.

- git diff -r HEAD [name of the file]: show the difference between the staged file and last committed file version.

## Storing Data with Git

- Git commits have three parts:
  - Commit: contains the metadata
  - Tree: tracks the names and locations of the files in the repository
  - Blob: binary large object, may contain data of any kind, comporessed snapshot of the file's contents
- Visual of commit structure:
  - [commit structure photo](visual_commit.png)

- Git hash: pseudo-random number generator --hash function
  - Hashes allow data sharing between repositories
    - If two files are the same,
      - then their hashes are the same.
    - Git only need to compare hashes.

- git log: shows the history of the repository
  - git log --oneline: shows the history in one line
  - git log --stat: shows the history with the statistics
  - git log --patch: shows the history with the changes

- git show [hash]: shows the changes of the commit with the hash. We only need the first 6 - 8 characters of the hash.

## Viewing Changes

### The HEAD Shortcut

- git diff -r HEAD
  - Compares staged files to the version in the last commit.
  - Use a tilde (~) to pick a specific commit to compare versions.
    - HEAD~1: the second most recent commit
    - HEAD~2: the third most recent commit
  - Must not use spaces between HEAD and the tilde.
  - [HEAD Commit photo](head_commit.png)
- git show HEAD~1
  - Shows the changes in the second most recent commit.
  - Use the tilde (~) to specify the commit number.
- git diff HEAD~1 HEAD: shows the changes between the last two commits.
- git diff hash1 hash2: shows the changes between the two commits with the hashes.

- git annotate [file]: shows the changes of the file with the commit hashes. Have 5 columns:
  - The commit hash
  - The author
  - The time of the commit
  - The line number
  - The content of the line

### Table of Useful Commands

Command | Function
--- | ---
git show HEAD~1 | Show what changed in the second most recent commit
git diff hash1 hash2 | Show what changed between two commits
git diff HEAD~1 HEAD~2 | Show what changed between the two commits
git annotate [file] | Show line-by-line changes and aassociated metadata

## Undoing Changes Before Committing

- to unstage a single file
  - git reset HEAD [file]
  - nano [file]
  - git add [file]
  - git commit -m "message"
- to unstage all files
  - git reset HEAD

- to undo changes in a file before staging
  - git checkout -- [file]

- checkout means switching to a different version
  - Defaults to the last commit

- This means losing all changes made to the unstaged file forever. Use with caution.

- git checkout . : undo all changes in all files.
  - "." refers to current directory when used in the shell.
  - Undo changes to all unstaged files in the current directory and subdirectories.
  - This command must be run in the main directory of the repository.
  - This command is irreversible. Use with caution.

### Unstaging and undoing

- git reset HEAD
- git checkout .
- git add .
- git commit -m "message"

## Restoring and Reverting

### Customizing the log output

- We can restrict the number of commits displayed using "-" and a number:
  - git log -3: shows the last 3 commits
  - To only look at the commit history of one file:
  - git log -3 [file]
- Restrict "git log" by date:
  - git log --since="MM DD YYYY"
  - Example: git log --since='Apr 2 2022'
  - git log --until="MM DD YYYY"
  - Example: git log --until='Apr 2 2022'
  - git log --since="MM DD YYYY" --until="MM DD YYYY"
  - Example: git log --since='Apr 2 2022' --until='Apr 5 2022'
- Restoring an old version of a file
  - to revert to a version from a specific commit:
    - git checkout [hash] [file]
    - git checkout HEAD~1 [file] # if we want to revert to the second most recent commit
- Cleaning a repository
  - git clean -n: shows the files that will be deleted
  - git clean -f: deletes the files. Use with caution.
  - git clean -f [file]: deletes the file
  - git clean -f [directory]: deletes the directory

## Configure Git

- Levels of settings
  - git config --list
    - Three levels of settings:
      - --local: settings for one specific repository
      - --global: settings for all of our repositories
      - --system: settings for every user on the computer
    - [Settings Level](settings_level.png)
- Changing our settings
  - git config --global setting value
    - Change email address: git config --global user.email [email]
    - Change name: git config --global user.name [name] # use quotation marks if the name has spaces

- Using an alias
  - Set up an alias through global settings
  - Typically used to shorten commands
  - To create an alias for committing files by executing "ci":
    - git config --global alias.ci 'commit -m' # quotation marks are necessary for spaces.
  - To use the alias:
    - git ci "message"

- Creating a custom alias
  - We can create an alias for any command
  - Example: If we often unstage files:
    - git config --global alias.unstage 'reset HEAD'
  - To use the alias:
    - git unstage [file]
  - Be careful not to overwrite existing commands

- Tracking aliases
  - git config --global --list
  - Output format: alias.aliasname=command

- Ignoring specific file
  - Create a file named .gitignore
  - "*" = wildcard
  - Commonly ignored files: APIs, credentials, system files, software dependencies.
  - Example: To ignore all files with the extension .log:
    - *.log

## Branches

- Git uses branches to systematically track multiple versions of files
- In each branch:
  - Some files might be the same.
  - OThers might be different.
  - Some may not exist at all.
- Example: Main, Analysis, Report Branches. [Branches](visual_branches.png)

- Benefits of branches
  - Avoiding endless subdirectories
  - Multiple people can work on the same project simultaneously
  - Everything is tracked
  - Minimizes conflicts between different versions of files

- Identifying branches
  - git branch: shows the branches
        "*" indicates the current branch we are working on
  - git branch [branchname]: creates a new branch
  - git checkout [branchname]: switches to the branch
  - git checkout -b [branchname]: creates and switches to the branch

- The difference between branches
  - git diff [branch1] [branch2]: shows the differences between the two branches

## Working with Branches

- Branches allow us to keep making progress concurrently
- We do merge branches to main branch. Because main is ground truth.
  - Each branch should be for a specific task.
  - Once the task is complete we should merge our changes into main.
  - Keep the main branch clean and up to date.
- Merging branches
  - git merge [source branch] [destination branch]: merges the source branch into the destination branch
  - Type of merge
    - Fast-forward merge: the destination branch is behind the source branch
    - Three-way merge: the destination branch has changes that are not in the source branch

- [Switching Branches](switch_branches.png)

## Handling Conflict

### Conflict

- Occurs when two branches have changes that cannot be merged automatically. A file has different changes in both branches.
- Git will not merge the branches until the conflict is resolved.
- Example of a conflict in the file content in a shell:  

    ```shell
    <<<<<<< HEAD # destination branch
    Content from destination branch
    =======
    Content from source branch
    >>>>>>> [branchname] # source branch
    ```

### Resolving conflicts

- git merge [branchname]: merge the branch
- git status: shows the files with conflicts
- Edit the file to resolve the conflict
- git add [file]: add the file to the staging area
- git commit -m "message": commit the changes

### Avoiding conflicts

- Prevention is better than cure!
- Use branches for specific tasks
- Avoid working on the same file in different branches
- Doesn't guarantee that conflicts won't occur
  - it reduces the likelihood of conflicts
- Communicate with the team
- Regularly merge the main branch into the working branch
- Keep the main branch clean and up to date

## Creating Repos

### Benefits of Repositories

- Systematically track versions
- Collaborate with colleagues
- Git stores everything!

### Creating a repository

- git init [name of the repository]: creates a new repository

### Converting a project

- git init: initializes the repository
- git status: shows the status of the repository
- git add .: adds all files to the staging area
- git commit -m "message": commits the files

### Nested repositories

- Do not create a repository within another repository. Known as a nested repository.
- There will be two .git directories. Git will not know which one to use and confuse.

## Working with Remotes

### Local Repo

- The repository on our computer

### Remote Repo

- The repository on a server
- Allows us to share our work with others
- Allows us to access our work from different devices
- Benefits of using a remote repository:
  - Backup
  - Collaboration
  - Access from different devices

### Cloning locally

- git clone [namme of the repository]: clones the repository to our computer
- git clone [directory]: clones the repository to the directory
- git clone [directory] [name of the repository]: clones the repository to the directory with a different name

### Cloning a remote

- Remote repositories are hosted on servers. Github, Gitlab, Bitbucket, etc.
- To clone a remote repository:
  - git clone [URL]

### Identifying remotes

- When cloning a repo
- Git remembers where the original was
- Git stoes a remote tag in the new repository's configuration
- git remote: shows the remote repositories

### More information

- git remote -v: shows the remote repositories with the URLs
- git remote add [name] [URL]: adds a new remote repository with a name
- When cloning, Git will automatically name the remote "origin"
- Defining remote names is useful for merging branches

## Gathering from a Remote

- Collaborating on Git projects
  - [Collaboration](collaboration.png)

### Fetching from a remote

- git fetch [remote] [branch]: fetches the changes from the remote repository to the local repository

### Synchrnoizing content

- git merge [remote] [branch]: merges the changes from the remote repository to the local repository

### Pulling from a remote

- git pull [remote] [branch]: fetches and merges the changes from the remote repository to the local repository
- git pull is a combination of git fetch and git merge. Git simplifies the process with git pull.
- Pulling with unsaved changes will cause a conflict. Save the changes before pulling.

## Pushing to a Remote

- Pull vs Push
  - [Pull vs Push](pulling_pushing.png)

- git push [remote] [branch]: pushes the changes from the local repository to the remote repository
- Example: git push origin main: pushes the changes from the main branch to the remote repository named origin
- Save the changes before pushing.

### Workflow

- git pull: fetches and merges the changes from the remote repository to the local repository
- git add .: adds the changes to the staging area
- git commit -m "message": commits the changes
- git push [remote] [branch]: pushes the changes from the local repository to the remote repository

### Resolving a conflict

- git pull --no-edit [remote] [branch]: fetches and merges the changes from the remote repository to the local repository without editing the commit message. Not recommended.
- git pull [remote] [branch]: fetches and merges the changes from the remote repository to the local repository. Recommended. Exit editor with add message and ctrl + o (save) and ctrl + x (exit).

## Summary

- What's covered
  - What a version is
  - Why version control is important
  - Using Git to save and compare files
  - How Git stores data
  - Configuration
  - Branches
  - Conflicts
  - Pull and push
  - Git Cheat Sheet: [Git Cheat Sheet Link](https://www.datacamp.com/cheat-sheet/git-cheat-sheet). [Git Cheat Sheet Photo](git_cheat_sheet.png)
