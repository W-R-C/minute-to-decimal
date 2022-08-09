#!/usr/bin/env/python3
from os import system, name

# This is a simply program to translate minutes to decmials.
# This helps me create faster senior project time tables

def welcome():
    number = input("\nPlease enter an integer: ")
    try:
        verification(number)
        input()
        clear()
    except:
        clear()
        print("Hello, Welcome to the minute to decimal conversion program.\nTo continue, please enter an integer or wildcard\nHit ctrl+c to stop at anytime.\n------------------------------------------------------------\n\nPlease enter a valid integer or wildcard")
        welcome()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def verification(x):
    if x == "*":
        print("Printing all numbers...\n")
        print_all()
    else:
        verified = int(x)
        conversion(verified)

def print_all():
    for i in range (0,60):
        conversion(i)
    input()
    clear()

def conversion(x):
    float_output = float(x) / 60
    number_str = str(x)
    output_rnd = format(float_output, '.3f');
    output_str = str(output_rnd)
    print(number_str + " minutes is equal to " + output_str)

def again():
    main()

def main():
    print("Hello, Welcome to the minute to decimal conversion program.\nTo continue, please enter an integer or wildcard\nHit ctrl+c to stop at anytime.\n------------------------------------------------------------")
    welcome()
    again()

if __name__=="__main__":
    main()