#!/usr/bin/python
# -*- coding: utf-8 -*-

# def testfunc(myname):
#     print('Hello, %s' % myname)

# testfunc('Oleg')

# def spaceship_building(cans):
#     total_cans = 0
#     for week in range(1, 53):
#         total_cans = total_cans + cans
#         print('Week %s, cans: %s' % (week, total_cans))

# spaceship_building(2)

# import time

# print(time.asctime());

# def silly_age_joke(age):
#     print('How old you are?')
#     age = int(sys.stdin.readline())
#     if age >= 10 and age <=13:
#         print('13 + 49 + 84+ 155+ 97: What you get? Head pain!')
#     else:
#         print('Something?')

# silly_age_joke()
import sys
from decimal import *

def convert_celsius_to_fahrenheit():
    print('What you weather degree in °C (function automatic convert it in fahrenheit)?')
    # strip – function will remove leading and trailing whitespaces. 
    celsius = str(sys.stdin.readline()).strip()    
    # isdigit() - Return true if all characters in the string are digits and there is 
    # at least one character, false otherwise.
    if celsius.strip('-+.').replace(".", "", 1).isdigit():
        fahrenheit =  (Decimal(celsius) * Decimal(9)/Decimal(5)) + 32
        print('Weather in fahrenheit is %s °F' % Decimal(fahrenheit).quantize(Decimal('1.0')))
    else:
        print('Celsius is not a number')

convert_celsius_to_fahrenheit()
