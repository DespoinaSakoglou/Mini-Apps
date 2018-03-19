# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:15:35 2018

@author: Despoina
"""

import time
import webbrowser

total_breaks = 3
total_count = 0

print("This program starts on: "+time.ctime())
while (total_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=hiVyZkR6uPk&list=RDhiVyZkR6uPk")
    total_count=total_count+1
