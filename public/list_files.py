# import requests
# import mysql.connector
# import pandas as pd

# initializations goes here
import os
import re
# we can later pass "/root/data"
current_directory = "/root/data"
# set to store unique ips when found
unique_ips = set()
list_of_files = []
# TO-DO: iterate over the directory base path recursively to list all the files:

# def check_ip_validity(ip_addree):
def list_all_files(directory):
    unique_ips = set()
    for root, dirs, files in os.walk(directory):
    
        for file in files:
            # print(os.path.join(root, file))
            list_of_files.append(os.path.join(root, file))
            with open(os.path.join(root, file)) as f:
                content = f.read()
                regex_pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
                
                list_of_ips = re.findall(regex_pattern, content)
                # print(list_of_ips)
                for each_ip in list_of_ips:
                    unique_ips.add(each_ip)

    return list(unique_ips)
                
all_valid_ips = list_all_files(current_directory)

    

def lexicographically_sort(strings):
    return sorted(strings)

sorted_strings = lexicographically_sort(all_valid_ips)

for each_valid_sorted_ip in sorted_strings:
    print(each_valid_sorted_ip)