#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program finds factors


def main():
    # Function finds factors

    print("Give me a number and I will give you all of its factors")

    while True:
        # Input
        number_string = input("Enter number: ")

        # Process
        try:
            number = int(number_string)
            assert number > 0
            break
        except AssertionError:
            # Output
            print("This isn't a valid input")
        except Exception:
            # Output
            print("This isn't a valid input")

    factors = []  # Prior knowledge

    for loop_counter in range(number + 1):
        loop_counter = loop_counter + 1
        if number % loop_counter == 0:
            factors.append(loop_counter)  # Prior knowledge

    # https://www.askpython.com/python/array/print-an-array-in-python
    print("The factors of {} are:".format(number), factors)


if __name__ == "__main__":
    main()
