"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/27/2020
Homework Problem: #1
Description: A program that gathers and prints odds, evens, squared and
cubes for integers in a range of 2 to 130.

"""
import math

# Constants for the range
START = 2
END = 130


# Even variables
total_even = 0
even_range = range(0, 0)


# Odd variables
total_odd = 0
odd_range = range(0, 0)


# Square variables
total_squares = 0
squares_list = []


# Cube variables
total_cubes = 0
cubes_list = []


for i in range(START, END+1):

    # Check for Odd cases and prints
    if i % 2 != 0:

        total_odd += 1

        if odd_range.start == 0:
            odd_range = range(i, END)

        if i == END-1:
            odd_range = range(odd_range.start, i)
            print("Odd ({}): ".format(total_odd),
                  end="{}\n".format(odd_range))

    # Check for even cases and prints
    if i % 2 == 0:
        total_even += 1

        if even_range.start == 0:
            even_range = range(i, END)

        if i == END:
            even_range = range(even_range.start, i)
            print("Even ({}): ".format(total_even),
                  end="{}\n".format(even_range))

    # Check for squared cases
    if (int(math.sqrt(i) + 0.5) ** 2) == i:
        total_squares += 1
        squares_list += [i]

    # Check for cubed cases
    if round(abs(i) ** (1 / 3)) ** 3 == i:
        total_cubes += 1
        cubes_list += [i]

    # # Check for the end and prints
    if i == END:
        print("Square ({}): ".format(total_squares),
              end="{}\n".format(squares_list))

        print("Cube ({}): ".format(total_cubes),
              end="{}\n".format(cubes_list))

