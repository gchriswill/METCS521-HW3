"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/29/2020
Homework Problem: #4
Description: A program that take input form the user and validates the input is
a 3 digit number, contains no digit duplication and is in ascending order.

"""

# Print formatting colors
SUCCESS = "\033[94m"
FAIL = "\033[91m"
END_FORMAT = "\033[0m"


# Main print message
input_msg = "Please enter a 3-digit integer:"


# Success print message
success_msg = "Number Accepted"


# Error print message
err_msg_3_digits = "You did not enter a 3-digit number."
err_msg_duplicates = "Your number contains duplication."
err_msg_not_integer = "This is not an integer. Please re-enter."
err_msg_not_ascending = "The digits are not in ascending order."


# Print function for printing success formatting
def print_success(msg):
    print("\n\t" + SUCCESS + msg + END_FORMAT + "\n")


# Print function for printing error formatting
def print_err(msg):
    print("\n\t" + FAIL + msg + END_FORMAT + "\n")


# Validator function for validating the input
def input_validator(i):

    # Validation for if no value was provided
    if str(i) is "":
        print_err(err_msg_3_digits)
        return False

    # Validation for value is not a number
    if not (str(i).isnumeric()):

        print_err(err_msg_not_integer)
        return False

    # Check if the collection does not contains 3 items
    if len(str(i)) != 3:
        print_err(err_msg_3_digits)
        return False

    # Check if the input contains duplicates
    duplicates = (str(i)[0] == str(i)[1]) or (str(i)[0] == str(i)[2]) or \
                 (str(i)[1] == str(i)[2])

    if duplicates:
        print_err(err_msg_duplicates)
        return False

    # Check if the input is in not ascending order
    not_ascending = (int(str(i)[0]) > int(str(i)[1])) or (int(str(i)[1]) > int(str(i)[2]))

    if not_ascending:
        print_err(err_msg_not_ascending)
        return False

    # Returns True as success
    return True


# Program Starter function for restarting the program if necessary
def start_program():

    # Gets the input from the user
    input_str = input(input_msg)

    # Gets the validation results from the validator function
    input_validation = input_validator(input_str)

    # Confirms that the validation from the validator
    if input_validation:
        print_success(success_msg)
    else:
        start_program()


start_program()
