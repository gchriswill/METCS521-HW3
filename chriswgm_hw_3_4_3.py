"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/27/2020
Homework Problem: #3
Description: A program that calculates the count of uppercase, lowercase, digits
and punctuations. Then it print these values to the console.

"""

# Imports the string library for convenience constants
import string


# Gathers the input for the user
input_str = input("Please provide a sentence:")


# Gets the uppercase characters into list
uppercase = [str(s) for s in input_str if str(s) in string.ascii_uppercase]


# Gets the lowercase characters into list
lowercase = [str(s) for s in input_str if str(s) in string.ascii_lowercase]


# Gets the digits characters into list
digits = [str(s) for s in input_str if str(s) in string.digits]


# Gets the punctuation characters into list
punctuations = [str(s) for s in input_str if str(s) in string.punctuation]


# Provides format with columns and inserts the required values
print_msg = """
# Upper # Lower # Digits # Punct.
-------- ------- -------- --------
   {}       {}      {}       {}
""".format(len(uppercase), len(lowercase), len(digits), len(punctuations))


# Prints the results
print(print_msg)
