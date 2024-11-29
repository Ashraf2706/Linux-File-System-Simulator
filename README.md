
# Linux File System Simulator

## Overview
This Python program simulates the functionality of a Linux file system. It allows users to navigate directories, create files and directories, locate files, delete files or directories, and perform other file system operations.

## Features
- **Directory Navigation**: Change directories using `cd` commands.
- **File and Directory Creation**: Create new files with `touch` and directories with `mkdir`.
- **File Search**: Locate files within the file system using the `locate` command.
- **File and Directory Deletion**: Delete specified files or directories using `rm`.
- **Directory Listing**: View the contents of directories with the `ls` command.
- **Path Display**: Show the current directory path using `pwd`.

## Files
- **`file_system.py`**: Contains the implementation of all file system operations.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Save the `file_system.py` file to your working directory.

## How to Use
1. Run the program from the command line:
   ```bash
   python3 file_system.py
   ```
2. Use the following commands to interact with the simulated file system:

### Commands
- **`pwd`**: Displays the current directory path.
- **`cd <directory>`**: Changes to the specified directory.
- **`mkdir <directory>`**: Creates a new directory.
- **`touch <file>`**: Creates a new file.
- **`locate <file>`**: Searches for a file in the system.
- **`ls`**: Lists the contents of the current directory.
- **`rm <file/directory>`**: Deletes a specified file or directory.
- **`exit`**: Exits the program.

### Example Commands
- Create a directory:
  ```bash
  mkdir my_directory
  ```
- Navigate into a directory:
  ```bash
  cd my_directory
  ```
- Create a file:
  ```bash
  touch my_file.txt
  ```
- List the contents of the current directory:
  ```bash
  ls
  ```
- Locate a file:
  ```bash
  locate my_file.txt
  ```
- Remove a file:
  ```bash
  rm my_file.txt
  ```

## Dependencies
- Python 3.x

## Author
- **Ashraf Kawooya**
- **Date**: 12/1/2022
- **E-mail**: ashrafk1@umbc.edu

## License
This project is for educational purposes and does not include warranties or guarantees.
