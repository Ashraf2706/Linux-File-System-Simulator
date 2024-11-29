"""
File:    file_system.py
Author:  Ashraf Kawooya
Date:    12/1/2022
Section: 11
E-mail:  ashrafk1@umbc.edu
Description:
   THE PROGRAM DUPLICATES HOW A LINUX FILE SERVER FUNCTIONS
"""

def is_valid_file_name(file_name):
    """
    Check if the given file name is valid.
    :param file_name: the name of the file to check.
    :return: a boolean indicating whether the file name is valid.
    """
    # if the file name is empty, it is considered valid
    if len(file_name) <= 0:
        return True
    # if the file name contains more than one character and starts with a slash, it is considered invalid
    if len(file_name) != 1 and file_name[0] == "/":
        return False
    # otherwise, check if the rest of the file name is valid
    else:
        return is_valid_file_name(file_name[1:])


def split_path(path):
    """
    Split the given path into its component parts.
    :param path: the path to split.
    :return: a list of the path components.
    """
    path_split = path.split("/")
    # remove any empty elements from the path
    for i in range(len(path_split) - 1):
        if path_split[i] == "":
            del path_split[i]
    return path_split


def navigate_to_directory(path, root):
    """
    Navigate to the given directory using the given path.
    :param path: the path to the directory.
    :param root: the root directory of the file system.
    :return: the target directory.
    """
    current_location = root
    path_split = split_path(path)
    # Iterate through each part of the path
    for directory_name in path_split:
        if directory_name + "/" in current_location:
            # If it does, move to that directory
            current_location = current_location[directory_name + "/"]
    # Return the final location
    return current_location


def find_file(file, root, pathway):
    """
    Find the given file in the file system.
    :param file: the file to find.
    :param root: the root directory of the file system.
    :param pathway: the current path in the file system.
    :return: the file location or 0 if not found.
    """
    if is_valid_file(file):
        file_location = []
        current_location = navigate_to_directory(pathway, root)
        # Check if the current location is empty or if it is a file (in which case it will only have one entry)
        if len(current_location) < 1:
            return 0
        elif len(current_location) == 1 and pathway != "/":
            return 0
        # Check if the file exists in the current location
        if file in current_location:
            return (pathway + file)
        else:
            # If the file is not in the current location, iterate through the current directory's entries
            for x in current_location:
                current_directory = x
                # If the entry is a directory (not a file), search that directory for the file
                if current_directory[-1] == "/" and current_directory != "../":
                    new_pathway = pathway + current_directory
                    found_file = find_file(file, root, new_pathway)
                    # If the file is found, add its location to the list of locations
                    if found_file != 0:
                        file_location.append(str(found_file))
        # Return the list of locations where the file was found
        return file_location

    else:
        print("Invalid file name")


def is_valid_file(file):
    """
    Check if the given file is valid.
    :param file: the file to check.
    :return: a boolean indicating whether the file is valid.
    """
    valid = True
    for item in file:
    # If the file name contains a forward slash, it is not valid
        if item == "/":
            valid = False
    return valid


def directory_change(current_pathway, root, new_directory):
    """
    Changes the current directory to a specified pathway
    :param current_pathway: the current pathway of the system
    :param root: the root directory of the system
    :param new_directory: new directory to change to
    :return: new directory path
    """
    # Find the current directory
    current = navigate_to_directory(current_pathway, root)
    
    if new_directory[-1] != '/':
        new_directory += '/'

    if new_directory in current:
        new_pathway = current_pathway + new_directory

        if new_directory == '../':
            new_pathway_split = split_path(new_pathway)
            del new_pathway_split[-1] , new_pathway_split[-1]
            if new_pathway_split != []:
                new_pathway = '/' + '/'.join(new_pathway_split) + '/'
            else:
                new_pathway = '/'
            return new_pathway
        else:
            return new_pathway
    else:
        print('Directory not found')

    

def create(pathway, root_dir, file):
    """
    creates a new file or directory
    :param pathway: the current pathway of the system
    :param root_dir: root directory of the system
    :param file: file that is needed to be created
    :return: file created 
    """
    pathway_split = split_path(pathway)

    command = file[0]
    append = file[1]

    current_location = root_dir

    if command == 'touch':
        touch_command = is_valid_file(append)

        if touch_command:
            current_location = navigate_to_directory(pathway, root_dir)

            current_location[append] = ""
        else:
            print('Invalid file')
    if command == "mkdir":
        if is_valid_file_name(append):
            if append[-1] != '/':
                append += '/'

            current_location = navigate_to_directory(pathway, root_dir)
            if append not in current_location:
                current_location[append] = {}
                current_location[append]['../'] = current_location
            else:
                print('Directory already exists')

        else:
            print('Invalid directory name')


def analyze(root_directory, pathway, file_split):
    """
    Analyzes a list of command-line arguments and performs actions on the file system.
    
    :param root_directory: The root directory of the file system.
    :param pathway: The current directory in the file system.
    :param file_split: A list of command-line arguments.
    """
    command_line = file_split[0] # The first argument is the command type.
    if len(file_split) > 1:
        variable = file_split[1] # The second argument is the command variable.

    if command_line == 'pwd':
        # Print the current directory.
        print(pathway)
    elif command_line == 'cd':
        # Change the current directory.
        if len(file_split) > 1: # Check if a directory was provided.
            pathway = directory_change(pathway, root_directory, variable)
            return pathway
        else:
            print('Directory not found')
    elif command_line == 'mkdir' or command_line == 'touch':
        # Create a new file or directory.
        if len(file_split) > 1: # Check if a file or directory name was provided.
            create(pathway, root_directory, file_split)
        else:
            print('Directory not found')
    elif command_line == 'locate':
        # find the location of the given file
        if len(file_split) > 1:
            locations = find_file(variable, root_directory, '/')
            if locations:
                for value in locations:
                    print(value)
            else:
                print('File not found')
    elif command_line == 'rm':
        # Delete a file or directory.
        path_split = split_path(pathway)
        data = navigate_to_directory(pathway, root_directory)
        if variable in data:
            del data[variable]
        else:
            print(variable, 'not found')
    elif command_line == 'ls':
        # List the contents of the current directory.
        if len(file_split) == 1:
            path_split = split_path(pathway)
            location = navigate_to_directory(pathway, root_directory)
            print(f'Contents for /{path_split[-1]}')
            for item in location:
                print(f'\t{item}')  
        else:
            # List the contents of a specified directory.
            path_split = split_path(variable)
            location = navigate_to_directory(variable, root_directory)
            print(f'Contents for /{path_split[-1]}')
            for item in location:
                print(f'\t{item}') 
    else:
        print('Invalid command')


if __name__ == "__main__":
    root_directory = {}
    initial_pathway = '/'
    command = input('[cmsc201 proj3]$ ').lower()
    command_split = command.split(' ')

    while command != 'exit':
        if command_split[0] == 'cd':
            new_pathway = analyze(root_directory, initial_pathway, command_split)
            if new_pathway != None:
                initial_pathway = new_pathway
        else:
            analyze(root_directory, initial_pathway, command_split)

        command = input('[cmsc201 proj3]$ ').lower() 
        command_split = command.split(' ')

   

