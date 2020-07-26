#!/usr/bin/env python3

# Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:
#
#     Prompts the user for a message to echo.
#     Prompts the user for the number of times to repeat the message. If no response is given, then the count should
#     default to 1.
#     Defines a function that takes a message and count then prints the message that many times.
#
# To end the script, call the function with the user-defined values to print to the screen.


message = input("Enter a message: ")
count = input("Number of repeats [1]: ").strip()

if count:
    count = int(count)
else:
    count = 1


def multi_echo(message_input, count_input):
    while count_input > 0:
        print(message_input)
        count_input -= 1


multi_echo(message, count)
