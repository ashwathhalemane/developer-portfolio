# vercada mock test on codesignal 
# initializations goes here
import os
import re

# current directory of files
current_directory = "/root/data"
# set to store unique ips when found
unique_ips = set()

# list to store files with their directory
list_of_files = []

def list_all_files(directory):
    
    # using os.walk to go over directories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            list_of_files.append(os.path.join(root, file))
            # read each file and process for ip address
            with open(os.path.join(root, file)) as f:
                # get the content of the file
                content = f.read()
                # regex pattern to filter valid ip in format: x.x.x.x where x is 0-255 inclusive
                regex_pattern = r"\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
                # get the list of valid ips from regex pattern matching, room for improvement here in regex pattern for large texts
                list_of_ips = re.findall(regex_pattern, content)
                
                # add ips to set to filter only the unique ones
                for each_ip in list_of_ips:
                    unique_ips.add(each_ip)
    # converting set to list for easier processing 
    return list(unique_ips)

def lexicographically_sort(strings):
    return sorted(strings)

# returns all valid ips in list format
all_valid_ips = list_all_files(current_directory)

# lexicographically sort using simple sorted build-in function in python 
sorted_ips = lexicographically_sort(all_valid_ips)

for each_valid_sorted_ip in sorted_ips:
    print(each_valid_sorted_ip)
