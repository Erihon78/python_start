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

import sys

# def silly_age_joke(age):
#     print('How old you are?')
#     age = int(sys.stdin.readline())
#     if age >= 10 and age <=13:
#         print('13 + 49 + 84+ 155+ 97: What you get? Head pain!')
#     else:
#         print('Something?')

# silly_age_joke()

def convert_celsius_to_fahrenheit():
    print('You weather degree in °C?')
    celsius = int(sys.stdin.readline())
    fahrenheit = (celsius * 9/5) + 32
    print('Weather in fahrenheit is %s' % fahrenheit)

convert_celsius_to_fahrenheit()
