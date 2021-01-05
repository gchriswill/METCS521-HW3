"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/29/2020
Homework Problem: #6
Description: A program that read the string records from a file and converts
each record into a programmatic object and print the object to the console.
The record's format follows the given example in records.txt file included
in this project.

"""

# Import path library for convenience file check
from os import path


# Print formatting colors
FAIL = "\033[91m"
END_FORMAT = "\033[0m"


# The file to read
records_file = "records.txt"


# Error print message
err_msg_file_not_found = "File does not exist"
err_msg_file_req_records = "File doesn't contains the required records..."


# Checks if the file exist
if not (path.isfile(records_file)):
    print("\n\t" + FAIL + err_msg_file_not_found + END_FORMAT + "\n")
    exit(1)


# Performs read file operation
text_read_file = open(records_file, "r")
data = text_read_file.read()
text_read_file.close()


# Split the lines, removes the new-line character and store result in list
records = data.splitlines(False)


# Checks if the records file does not contains any records
if len(records) == 0:
    print("\n\t" + FAIL + err_msg_file_req_records + END_FORMAT + "\n")
    exit(1)


# Performs comprehensive list operation for breaking down each record into a
# list with the items of the given record and then stores each listed record
# into a master list.
listed_records = [records[i].split(sep=", ") for i in range(0, len(records), 1)]


# Prints to the console the total records found
print("Total Records: {}".format(len(listed_records)))


# Prints to the console the listed record
print(listed_records)




