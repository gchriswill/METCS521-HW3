"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/29/2020
Homework Problem: #5
Description: A program that take a file as input, condition the data on file
and writes this same data to a new file.

"""

# Import path library for convenience file check
from os import path


# Print formatting colors
FAIL = "\033[91m"
END_FORMAT = "\033[0m"


# The file to read and write
test_file = "test.txt"


# The new file to create and write
new_test_file = "new_test.txt"


# Error print message
err_msg_file_not_found = "File does not exist"
err_msg_file_req_words = "File doesn't contains the required words (20)..."


# Checks if the file exist
if not (path.isfile(test_file)):
    print("\n\t" + FAIL + err_msg_file_not_found + END_FORMAT + "\n")
    exit(1)


# Performs read file operation
text_read_file = open(test_file, "r")
data = text_read_file.read()
text_read_file.close()


# Replaces the space character with \n
lined = str(data).replace(" ", "\n")


# Create a list of words with new lines enabled
listed_n = lined.splitlines(True)


# Checks if the file does not contains 20 words
if len(listed_n) != 20:
    print("\n\t" + FAIL + err_msg_file_req_words + END_FORMAT + "\n")
    exit(1)


# Performs write file operation
text_write_file = open(test_file, "w")
text_write_file.write(lined)
text_write_file.close()


# Create a list of words with new lines disabled
listed = lined.splitlines(False)


# Performs comprehensive list operation for grouping 5 words in a list of lists
# with new lines for each group
lines = [" ".join(listed[i:i+5]) + "\n" for i in range(0, len(listed), 5)]


# Performs write new file operation
new_text_write_file = open(new_test_file, "w")
new_text_write_file.writelines(lines)
new_text_write_file.close()
