# Mini Apps
This repository contains mini projects as part of the Udacity Full Stack Web Developer Nanodegree program.

### Contents
1) "Take a break"
2) "Rename files"
3) "Drawing a Circle from Squares"
4) "Send a text"

### Description
Several mini apps using functions and classes in Python.
1) "Take a break" is a program that plays a youtube video every two hours for
three consecutive breaks.
2) "Rename files" is a program that renames files by stripping their names of any numbers.
3) "Drawing a Circle from Squares" is a program that uses the turtle module to draw shapes.
It draws a circle out of drawing consecutive squares.
4) "Send a text" is a program that sends a text message using twilio platform.

### Required Libraries and Dependencies
Python 3.x is required to run these projects. You can either run these programs using Anaconda IDE or natively with Python 3.x. The turtle module is used to run "Drawing a Circle from Squares" program. You need to create an account with Twilio in order to run the "Send a text" program.

### How to Run the Projects
Download the project zip file to your computer and unzip it, or clone this repository.

*Using Anaconda IDE*

1) Open Anaconda Navigator and Launch your preferred environment (e.g. spyder, notebook or jupyterlab)
2) From the root/project directory, open and run entertainment_center.py

*Using Python 3.x*

1) Open the operating system's command prompt
2) From the root/project directory, run python your_selected_project_name.py in the command line

Download and install twilio

*Using Windows*

- You can then either type `easy_install twilio` or `pip install twilio` in the Command Prompt to download and install Twilio (provided that your computer's PATH has Python added).

*Using Macintosh or Linux*

- Load up the Terminal application and type in `sudo easy_install twilio` and enter in your password to give `easy_install` permissions to write to your system folders.

Register with twilio

[Twilio Sign Up Page](https://www.twilio.com/try-twilio)

Once you created an account, check out the Dashboard page, then click the link, "Show API Credentials" to find the SID and Auth Token that will be used in the code. You need to add your own account's SID and Auth Token in the code in order to run the "Send a text" program.
