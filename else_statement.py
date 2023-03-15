#!/usr/bin/python3
def hint_username():
    if len(username) < 3:
        print("Invalid username. Must be atleast 3 charaters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")
