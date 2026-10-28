#!/usr/bin/env python3
# Created by Sereke
# Created on: October, 22, 2026
# This program asks for user age and if therr older than 25 and younger than 25
# it approvwes you to date a someone grandson. if you type something else exept integer it will
# display a message, user_input is invalid age. and if they didnt meet the reguirement
# it display sorry, You didnt meet the required age.

import constants

print(
    "Welcome, if you are interested in dating my grandchild.\n You have to answer one question."
)


def main():

    # here we will use try to
    try:

        # Here we take the user input as string
        user_input = input("How old are you?: ")

        # Then cast it or try to covert it to an integer
        user_age = int(user_input)
        user_age >= 0

        if user_age < 0:
            print(user_age, "is invalid age")
        elif user_age > constants.MIN_AGE and user_age < constants.MAX_AGE:
            print("Congralations, you meet the required age to date my grandchild.")

        elif user_age <= 0 < constants.MIN_AGE:
            print("You are too young to date my grandchild.")

        else:
            user_age >= constants.MAX_AGE
            print("You are too old to date my grandchild.")
    except ValueError:
        print(user_input, "is not a valid age or integer.")
    finally:
        print("Thank You, for your interestes in my grandchild.")


if __name__ == "__main__":
    main()
