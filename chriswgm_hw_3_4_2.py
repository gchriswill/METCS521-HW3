"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/27/2020
Homework Problem: #2
Description: A program to demonstrate the usage of method that ease string
manipulation.

"""

# Constants for the odd string and the relevant message
ODD_STR = "Christopher"
RELEVANT_MSG = "This odd string is not odd at all"


# Checks if the string is not odd
if len(ODD_STR) % 2 == 0:
    exit("\n\t" + "\033[91m" + RELEVANT_MSG + "\033[0m" + "\n")


# Prints the required statements
print("\"{}\", \"{}\"".format(ODD_STR, len(ODD_STR)))
print("\"{}\"".format(ODD_STR[int(len(ODD_STR)/2)::int(len(ODD_STR)/2)+1]))
print("\"{}\"".format(ODD_STR[:int(len(ODD_STR)/2)]))
print("\"{}\"".format(ODD_STR[int(len(ODD_STR)/2)+1:]))



