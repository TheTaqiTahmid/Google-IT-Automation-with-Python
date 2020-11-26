# Reading data interactively

# Creating a function that takes hours, minutes, and seconds as input and convert them to seconds.
# def to_seconds(hours, minutes, seconds):
#     return hours * 3600 + minutes * 60 + seconds
#
#
# cont = "y"
#
# while cont.lower() == "y":
#     hours = input("Please insert the number of hours: ")
#     minutes = input("Please insert the number of minutes: ")
#     seconds = input("Please insert the number of seconds: ")
#     print("Total time in seconds is {} seconds".format(to_seconds(int(hours), int(minutes), int(seconds))))
#     print()
#     cont = input("Do uou want to continue? [y to continue] ")
#
# print("Thanks for trying this script")


# Standard Streams
# I/O streams is the basic mechanism for performing input and output operations in programs
# Most OS supply three different I/O stream by default.
# STDIN - Standard Input (input)
# STDOUT - Standard output (print)
# STDERR - Standard error (error message)
# A shell is a command line interface that interact with OS
# echo is a command that we use to write text in a linux shell
# We can read the environmental variables in python

# import os
# import sys
#
# print("Home: " + os.environ.get("HOME", ""))
# print("SHELL: " + os.environ.get("SHELL", ""))
# # The get module allows us to specify what will be returned if there is no env variable of that name
#
# # To create an environmental variable in linux shell:
# # export <variable name>=<Variable value>
#
# # Command line arguments: These are parameters that are passed to a program when it is started
# # The list of command line arguments passed to a Python script
# print(sys.argv)
# Then we can utilize these arguments in our script by selecting any of the argument for further use.
# For example we can pass the python script and a log file in the command line. We can access the log file in our scrip
# By using 'sys.argv[<argument number>]'
# testscript:
# import sys
# logfile = sys.argv[1]
# .....
# user@ubuntu: ~s ./testscript.py syslog

# Exit status is the value returned by a program to the shell. In unix shell environments exit status 0 means success
# and other status means failure with each value with certain significance.
# To check the the values of lines, words and characters for our Python script write the following command on shell
# wc variables.py
# echo $?  # This is to check the exit status of our last executed program

# Running System Commands in Python. Subprocess module allows running system command within python script.
import subprocess

# # The subprocess will wait for the child process to finish and then it will move forward with the rest of the script
# subprocess.run(['sleep', '2'])
# result = subprocess.run(['ls', 'This file does not exist'])
# print(result.returncode)
# The above commands are linux shell commands and will not work on windows
# x = subprocess.run(['ping', '10.220.220.221'])  # This process will run on windows (CMD or powershell)
# This process cannot save the output of system command. And can only be seen on the display. Can only check the
# return code to see if the process was a success or not.
# print(x)  # Nothing

# # Obtaining the output of system command
# result = subprocess.run(['host', '8.8.8.8'], capture_output=True)  # (Linux command)
# # The capture output allows to capture the output of the system command
# print(result.returncode)  # outputs the return code
# print(result.stdout.decode().split())
# Outputs the output of the system command. The decoder decodes the output into usable string (default UTF-8)
# We can modify this output to use as we wish in our script

# # To see the output of stderr:
# result = subprocess.run(['rm', 'does-not_exist'], capture_output=True)
# print(result.returncode)  # Linux system command
# print(result.stderr)  # Linux system command

# # Advanced subprocess management
# # In this example we have added a new path in out system path variable to run a new type of executable file
# import os
# import subprocess
#
# my_env = os.environ.copy()
# my_env['PATH'] = os.pathsep.join(['path directory to run a particular executable file', my_env['PATH']])
#
# result = subprocess.run(['myapp'], env=my_env)

import re


def show_time_of_pid(line):
    pattern = r'^([A-Za-z]{3} [0-9]+ [\w:]+).*\[([0-9]+)\]'
    result = re.search(pattern, line)
    return result[1] + ' ''pid:'+result[2]


print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))
# r'^([\w .-]*), ([\w .-]*)$'
# [0 - 9] + [0 - 9:]+