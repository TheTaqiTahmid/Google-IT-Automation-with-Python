#!/usr/bin/env python3

import re
import csv
import operator
import sys

error= {}
per_user = {}

with open("syslog.log") as logfile:
    for f in logfile:
        user = re.search(r" \((.*)\)", f).group(1)
        error_msg = re.search(r"ERROR (.*) ", f)
        if user not in per_user:
            per_user[user] = {'INFO':0, 'ERROR':0}
        if "INFO" in f:
            per_user[user]['INFO'] += 1
        if "ERROR" in f:
            per_user[user]['ERROR'] += 1
            if error_msg.group(1) not in error:
                error[error_msg.group(1)] = 0
            error[error_msg.group(1)] += 1

error_list = []
for e,f in error.items():
    error_list.append({'Error':e, 'Count':f})

per_user_list = []
for user, value in per_user.items():
    per_user_list.append({"Username":str(user), "INFO":value['INFO'], "ERROR":value['ERROR']})

# Idea got from w3schools https://www.w3schools.com/python/ref_list_sort.asp
def myFunc(e):
  return e['Username']

def myFunc2(e):
  return e['Count']

per_user_list.sort(key=myFunc)
error_list.sort(reverse=True, key=myFunc2)

error_keys = ['Error', 'Count']
with open("error_message.csv", 'w') as csv_file:
     writers = csv.DictWriter(csv_file, fieldnames=error_keys)
     writers.writeheader()
     writers.writerows(error_list)

user_keys = ['Username', 'INFO', 'ERROR']

with open("user_statistics.csv", 'w') as csv_f:
     writers = csv.DictWriter(csv_f, fieldnames=user_keys)
     writers.writeheader()
     writers.writerows(per_user_list)