#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program is a positive number only sum calculator with
#     a Continue statement


import random


def main():
    # This function finds the sum of all positive numbers

    # Input
    counter = 0
    sum = 0

    while True:
        num_addends_str = input("Enter the number of addends: ")

        try:
            num_addends_int = int(num_addends_str)
        except Exception:
            print("That is not an integer, please input the number of"
                  " addends!")
            print("")
        else:
            if num_addends_int < 2:
                print("You have not a valid number of addends, please input 2"
                      " or more!")
                print("")
            else:
                break

    # Process
    while counter < num_addends_int:
        counter += 1

        addend_str = input("Enter a number: ")

        try:
            addend_int = int(addend_str)
        except Exception:
            print("That is not an integer, please input a number!")
            print("")
            counter -= 1
        else:
            if addend_int <= 0:
                continue
            else:
                sum += addend_int
    # Output
    print("The sum of all positive numbers is {0}".format(sum))


if __name__ == "__main__":
    main()
