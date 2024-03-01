#!/usr/bin/env python3

def happy_new_year():
    i = 10 
    while i > 0:
        print(i)
        i -= 10 
        print("Happy New Year!")
    # code goes here!
    pass

def square_integers(int_list):
    squared_integers = [x ** 2 for x in int_list]
    return squared_integers
    # code goes here!
    pass

def fizzbuzz():
    for num in range (1,100) :
        if num % 3 == 0 and num % 5 == 0 :
            print("FizzBuzz")
        elif num % 3 == 0 :
            print("Fizz")
        elif num % 5 == 0 :
            print("Buzz")
        else:
            print(num)
    # code goes here!
    pass





