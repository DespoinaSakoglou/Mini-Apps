
"""
A program that renames files by stripping their names of any numbers.

Created on Mon Mar 19 14:20:34 2018

"""

# import miscellaneous operating system interfaces 
import os

# define the function to rename files
def rename_files():
    # (1) Get file names from a folder. Use the path to your folder
    file_list = os.listdir("/folder_name")
    print(file_list)
    # save the current working directory
    saved_path = os.getcwd()
    # change the current working directory to the one containing the folder with the files.Use the path to your folder
    os.chdir("/folder_name")
    
    # (2) For each file, rename 
    for file_name in file_list:
        # optionally print out old and new names for comparison
        print("Old name - "+file_name)
        print("New name - "+file_name.strip('0123456789'))
        # use rename function to replace the old name with the new one, stripped of numerals
        os.rename(file_name, file_name.strip('0123456789'))
    # change current working directory back
    os.chdir(saved_path)
    
#call the rename_files() function
rename_files()
    
