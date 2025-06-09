# Finding the largest element in the array:

import math


def largestElement(a):
    max = float('-inf')
    for x in a:
        if x > max:
            max = x
    return max


def SecondLargestElement(a):
    max = float('-inf')
    secondMax = float('-inf')

    for x in a:
        if x > max:
            secondMax = max
            max = x
        if x > secondMax and x != max:
            secondMax = x
    return secondMax


def main():
    a = [7, 33, 4, 2]
    print(largestElement(a))
    print(SecondLargestElement(a))


main()