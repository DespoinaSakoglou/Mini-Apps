# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:20:34 2018

@author: Despoina
"""

import os
def rename_files():
    # (1) Get file names from a folder. r in front of the path means to take path as it is
    file_list = os.listdir(r"C:\Users\Despoina\Desktop\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Despoina\Desktop\prank")
    
    # (2) For each file, rename 
    for file_name in file_list:
        print("Old name - "+file_name)
        print("New name - "+file_name.strip('0123456789'))
        os.rename(file_name, file_name.strip('0123456789'))
    
    os.chdir(saved_path)
rename_files()
    