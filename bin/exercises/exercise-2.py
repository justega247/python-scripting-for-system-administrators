#!/usr/bin/env python3.7

# Exercise: Working with If/Else
# Exercise Instructions
# Solution
# Mark as Completed
#
# Create a script that has a single variable you can set at the top called user. This user is a dictionary containing
# the keys:
#
#     'admin' - a boolean representing whether the user is an admin user.
#     'active' - a boolean representing whether the user is currently active.
#     'name' - a string that is the user’s name.
#
# Example:
#
#     user = { 'admin': True, 'active': True, 'name': 'Kevin' }
#
# Depending on the values of user print one of the following to the screen when you run the script.
#
#     Print (ADMIN) followed by the user’s name if the user is an admin.
#     Print ACTIVE - followed by the user’s name if the user is active.
#     Print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active.
#     Print the user’s name if neither active nor an admin.
#
# Change the values of user and re-run the script multiple times to ensure that it works.

# SOLUTION


user = {'admin': True, 'active': True, 'name': 'Kevin'}
prefix = ""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN) "
elif user['admin']:
    prefix = "(ADMIN) "
elif user['active']:
    prefix = "ACTIVE - "

print(prefix + user['name'])
