
"""
A program that plays a youtube video every two hours for
three consecutive breaks.

Created on Mon Mar 19 13:15:35 2018

@author: Despoina
"""

# import time module to use: 1)current time function-shows program start 2)sleep function-adds 2-hour intervals between breaks
import time
# import webbrowser-opens the youtube video
import webbrowser

# set number of total_breaks 
total_breaks = 3
# initialize counter for while loop iterations
total_count = 0

# print out start time of program
print("This program starts on: "+time.ctime())
# use a while loop to repeat the break 3 times
while (total_count < total_breaks):
    # pause the program for 2 hours (in seconds)
    time.sleep(2*60*60)
    # after 2 hours, open the youtube video
    webbrowser.open("https://www.youtube.com/watch?v=o3NndBTqC3Y")
    # increment counter for next iteration
    total_count=total_count+1
