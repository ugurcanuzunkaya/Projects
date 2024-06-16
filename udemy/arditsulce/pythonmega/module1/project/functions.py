def file_operations(filename, listname, operation):
    """
    Performs read or write operations on a file.

    Parameters:
    filename (str): The name of the file to be read from or written to.
    listname (list): The list to be written to the file or to store the contents of the file.
    operation (str): The operation to be performed. 'w' for write and 'r' for read.

    Returns:
    list: The list after performing the operation. If 'w', it's the same list that was written to the file. 
    If 'r', it's the list populated with the contents of the file.
    """
    if operation == "w":
        with open(filename, "w") as file:
            for counter, item in enumerate(listname):
                file.write(f"{counter + 1} - {item}\n")
                
    elif operation == "r":
        listname.clear()
        with open(filename, "r") as file:
            for line in file:
                line = line.rstrip("\n")
                listname.append(line)
                print(line)

    return listname

