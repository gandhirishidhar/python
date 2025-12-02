import os

# Specify the directory you want to list
#specify the path or directory you want to list
# '.' means the "Current Directory" (where this file is saved)
# '.' means the current directory 
directory_path = '/' 

# Get the list of files and folders
# Get the list of the files and folders     in the specified directory
contents = os.listdir(directory_path)

# Print the results
print("--- Directory Contents ---")
for item in contents:
    print(item)