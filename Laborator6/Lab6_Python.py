import os
import sys

# 1. Create a Python script that does the following:
# Takes a directory path and a file extension as command line
# arguments (use sys.argv).
# Searches for all files with the given extension in the specified 
# directory (use os module).
# For each file found, read its contents and print them.
# Implement exception handling for invalid directory paths, 
# incorrect file extensions, and file access errors.

try:
    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.isdir(directory):
        raise Exception("invalid path")
    
    for i in os.listdir(directory):
        if i.endswith(extension):
            path = os.path.join(directory,i)
            try:
                fis = open(path,'r')
                content = fis.read()
                print(content)
            except:
                print("incorrect file extension")
except:
    print("file access error")

# 2.Write a script using the os module that renames all files in a
# specified directory to have a sequential number prefix. For 
# example, file1.txt, file2.txt, etc. Include error handling for 
# cases like the directory not existing or files that can't be renamed.

def already_numbered(file_name):
    parts = file_name.split('.')
    if len(parts) == 2:
        prefix, extension = parts
        return prefix.startswith('file') and prefix[4:].isdigit()
    return False

def file_number(directory):
    list_files = os.listdir(directory)
    filtered_files = []

    for file in list_files:
        if already_numbered(file):
            filtered_files.append(file)
    if filtered_files:
        highest_numbers = []
        for file in filtered_files:
            number_part = file.split('.')[0][4:]
            highest_numbers.append(int(number_part))
        highest_number = max(highest_numbers)
        return highest_number
    else:
        return 0


def rename(directory):
    try:
        if not os.path.isdir(directory):
            raise Exception("invalid path")

        highest_number = file_number(directory)

        list_files = []
        for file in os.listdir(directory):
            if not already_numbered(file):
                list_files.append(file)
        list_files.sort()

        for i, file in enumerate(list_files, start=highest_number + 1):
            extension = os.path.splitext(file)[1]
            new_file = f"file{i}{extension}"
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_file)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {file} in {new_file}")

            except PermissionError:
                print(f"error: permission error: unable to rename {file}")
            except FileNotFoundError:
                print(f"error: {file} not found.")

    except Exception as e:
        print(f"Error: {e}")

directory = "C:/Users/eliza/Desktop/Facultate/An3/Python/Laborator6/ex2"
rename(directory)

# 3. Create a Python script that calculates the total size of all 
# files in a directory provided as a command line argument. The 
# script should:
# Use the sys module to read the directory path from the command line.
# Utilize the os module to iterate through all the files in the 
# given directory and its subdirectories.
# Sum up the sizes of all files and display the total size in bytes.
# Implement exception handling for cases like the directory not 
# existing, permission errors, or other file access issues.

def calculate_size(directory):
    try:
        if not os.path.isdir(directory):
            raise Exception("invalid path")

        size = 0
        for root, dirs, files in os.walk(directory):
            for i in files:
                file_path = os.path.join(root, i)
                try:
                    size += os.path.getsize(file_path)
                except Exception as e:
                    print(f"Error accessing {file_path}: {e}")

        print(f"total size {size} bytes")
    except PermissionError:
                print(f"error: permission error {file_path}")
    except Exception as ex:
        print(f"Error: {ex}")

if len(sys.argv) != 2:
    print("not enough parameters")
else:
    directory = sys.argv[1]
    calculate_size(directory)

# 4. Write a Python script that counts the number of files with 
# each extension in a given directory. The script should:
# Accept a directory path as a command line argument (using sys.argv).
# Use the os module to list all files in the directory.
# Count the number of files for each extension (e.g., .txt, .py, .jpg)
# and print out the counts.
# Include error handling for scenarios such as the directory not 
# being found, no read permissions, or the directory being empty.

def count_extensions(directory):
    try:
        if not os.path.exists(directory):
            raise Exception("directory doesn't exists")

        if not os.path.isdir(directory):
            raise Exception("invalid path")

        file_list = os.listdir(directory)

        count_ext = {}
        no_extension = 0
        for i in file_list:
            name, extension = os.path.splitext(i)
            if extension:
                count_ext[extension] = count_ext.get(extension, 0) + 1
            else:
                no_extension += 1
        if len(count_ext) == 0 and no_extension == 0:
            print("empty folder")
        else:
            print("extensios number:", len(count_ext))
            for extension, count in count_ext.items():
                print(f"{extension}: {count} files")

        if no_extension > 0:
            print(f"no extension: {no_extension} files")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: Permission error - {e}")
    except Exception as e:
        print(f"unexpected error occurred: {e}")

if len(sys.argv) != 2:
    print("not enough parameters")
else:
    directory = sys.argv[1]
    count_extensions(directory)
