#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.

import math
###############################################################################
# Exercise 6.2
# See 6.1: "write a compare function takes two values, x and y, and returns 1
# if x > y, 0 if x == y, and -1 if x < y."
# When you submit only include your final function: compare
#function to compare the values x and y
def compare(x,y):
    # if x > y return 1
    if(x > y):
        return 1
    # if x == y return 0
    if(x == y):
        return 0
    #if x < y  return -1
    if(x < y):
        return -1
    




###############################################################################
# Exercise 6.2
# See 6.2: "use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given the
# lengths of the other two legs as arguments."
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share in your final push your incremental
# work.
# function to find hypotenuse given the 2 sides
def hypotenuse(side1,side2):
    # the hypotenuse is square root of sum of the squares of other 2 sides
    hypotenuse = math.sqrt(side1**2 + side2**2)
    return round(hypotenuse,2)
    



###############################################################################
# Exercise 6.4
# See 6.4: "write a function is_between(x, y, z) that returns True if x ≤ y ≤ z
# or False otherwise"
# When you submit only include your final function: is_between
#function to check if a value 'y' is between x and y
def is_between(x, y, z):
    #return true if y is greater than or equal to x and less than or equal to z
    if(x <= y <= z):
        return True
    #return false otherwise
    else:
        return False



###############################################################################
# Exercise 3.2
# See "Exercise 3, part 2": "Write a function called is_palindrome that takes a
# string argument and returns True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length of a
# string."
# When you submit only include your final function: is_palindrome

#function to check is a string is palindrome
def is_palindrome(string_val):
    String_length = len(string_val)
    #base case return 1 if length is 1
    if(String_length == 1):
        return True
    #if length is more than 2, compare first and last characters
    if(String_length >= 2):
        if(first(string_val) == last(string_val)):
            #if string is 2 characters and are same-return true
            if(String_length == 2):
                return True
            # else check the remaining string after slicing
            else:
                return is_palindrome(string_val[1:-1])
        #if the first and last characters are not equal - return false
        else:
            return False
    
#helper function for palindrome
        #.lower() method to ignore case
def first(word):
    return word[0:1].lower()
def middle(word):
    return word[1:-1].lower()
def last(word):
    return word[-1].lower()
    


###############################################################################
# Exercise 4
# See "Exercise 4": "A number, a, is a power of b if it is divisible by b and
# a/b is a power of b. Write a function called is_power that takes parameters a
# and b and returns True if a is a power of b. Note: you will have to think
# about the base case."
# Note: Please use the provided definition and only plan for positive integers
# (whole numbers not including zero)
# When you submit only include your final function: is_power

#function to check if a value is the power of another value
def is_power(a,b):
    #if the value after a division call is 1 - it means its the same number
    # which was divided and its a power - if not it would have failed in the % check
    if(a == 1):
        return True
    #if it is divisible without a remainder it is a power
    if ((a % b == 0) and (is_power(a/b,b))):
        return True
    else:
        return False



###############################################################################
def main():
    """Your functions will be called within this function."""
    ###########################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")






    ###########################################################################
    # # Uncomment the below to test and before commiting:
    # # Exercise 1
    print(compare(1, 1))
    print(compare(1, 2))
    print(compare(2, 1))
    # # # Exercise 2
    print(hypotenuse(1, 1))
    print(hypotenuse(3, 4))
    print(hypotenuse(1.2, 12))
    # # # Exercise 3
    print(is_between(1, 2, 3))
    print(is_between(2, 1, 3))
    print(is_between(3, 1, 2))
    print(is_between(1, 1, 2))
    # # # Exercise 6
    print(is_palindrome("Python"))
    print(is_palindrome("evitative"))
    print(is_palindrome("sememes"))
    print(is_palindrome("oooooooooooo"))
    #print(is_palindrome("Racecar"))
    # # # Exercise 7
    print(is_power(28, 3))
    print(is_power(27, 3))
    print(is_power(248832, 12))
    print(is_power(248844, 12))


if __name__ == "__main__":
    main()
