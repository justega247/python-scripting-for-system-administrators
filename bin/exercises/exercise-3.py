#!/usr/bin/env python3.7

# Building on top of the conditional exercise, write a script that will loop through a list of users where each item
# is a user dictionary from the previous exercise printing out each user’s status on a separate line. Additionally,
# print the line number at the beginning of each line, starting with line 1. Be sure to include a variety of user
# configurations in the users list.
#
# User Keys:
#
#     'admin' - a boolean representing whether the user is an admin user.
#     'active' - a boolean representing whether the user is currently active.
#     'name' - a string that is the user’s name.
#
# Depending on the values of the user, print one of the following to the screen when you run the script.
#
#     Print (ADMIN) followed by the user’s name if the user is an admin.
#     Print ACTIVE - followed by the user’s name if the user is active.
#     Print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active.
#     Print the user’s name if neither active nor an admin.

user_list = [
    {'admin': True, 'active': True, 'name': 'Kevin'},
    {'admin': False, 'active': True, 'name': 'Kingsley'},
    {'admin': True, 'active': False, 'name': 'Kelechi'},
    {'admin': False, 'active': False, 'name': 'Kess'}
]


def user_status(user):
    prefix = ""

    if user['admin'] and user['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix = "(ADMIN) "
    elif user['active']:
        prefix = "ACTIVE - "

    return prefix + user['name']


for index, person in enumerate(user_list, start=1):
    print(f"{index} {user_status(person)}")
