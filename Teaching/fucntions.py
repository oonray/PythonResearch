"""
@author oonray
@file snooptions.py
@brief Calculator APP

This App calulates stuff!
"""

import sys #import module sys
#
# Input: <action> <n * numbers>
#

arguments = sys.argv # A List of arguents to the program
nargs=len(arguments)
[print("argument {} is {}".format(n,i)) for i,n in zip(arguments,range(len(arguments)))] # Print arguments and their postions

numbers = []

def pluss(nums):
    return sum(nums)

def minus(nums):
    start = nums[0]
    for i in nums[1:]:
        start -= i
    return start

def multiplikasjon(nums):
    start = nums[0]
    for i in nums[1:]:
        start *= i
    return start

def divisjon(nums):
    start = nums[0]
    for i in nums[1:]:
        start /= i
    return start

actions = {pluss.__name__:pluss,
           minus.__name__:minus,
           multiplikasjon.__name__:multiplikasjon,
           divisjon.__name__:divisjon}

if sys.argv[1] not in actions.keys():
    raise(Exception("Not a Valid Action! Valid actions are: {}".format(actions)))

try:
    for i in sys.argv[2:]:
        numbers.append(float(i))
except ValueError as e:
    raise(Exception("One of the numbers is not valid! msg:{}".format(e)))

print(actions)

#if sys.argv[1] == "pluss": pluss(numbers)
#if sys.argv[1] == "minus": minus(numbers)
#if sys.argv[1] == "multiplikasjon": multiplikasjon(numbers)
#if sys.argv[1] == "divisjon": divisjon(numbers)

#if __name__ == "__main__":
#    print(actions[sys.argv[1]])
#    print(pluss)
#    print("Result: {}".format(actions[sys.argv[1]](numbers)))
#    print("Resutl: {}".format(pluss(numbers)))






















