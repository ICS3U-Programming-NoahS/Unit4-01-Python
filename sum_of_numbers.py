#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 6th, 2023
# This program asks the user to enter a positive integer
# then tells the user the sum of the numbers from 0 to that number


def main():
    # Get the number
    num_string = input("Enter a positive integer: ")

    # Initialize the counter
    counter = 0

    # Initialize the sum
    sum = 0

    # Making sure the number is an integer
    try:
        num_int = int(num_string)

        # Check if the number is negative
        if num_int < 0:
            print("{} is not a positive integer.".format(num_int))
        else:
            # While loop to find the sum
            while counter <= num_int:
                print("{} times through the loop.".format(counter))
                sum = sum + counter
                counter = counter + 1
            else:
                print("The sum of the numbers from 0 to {} is {}".format(num_int, sum))
    except:
        print("{} is not an integer!".format(num_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
