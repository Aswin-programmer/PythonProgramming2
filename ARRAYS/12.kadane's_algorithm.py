import math

def CalculateMaximumSubarraySum(arr):
    sum = 0
    maxi = float('-inf')

    start = 0
    ansStart = -1
    ansEnd = -1

    for i in range(len(arr)):
        if sum == 0:
            start = i
        sum += arr[i]
        if maxi < sum:
            maxi = sum
            ansStart = start
            ansEnd = i
        if sum < 0:
            sum = 0

    return (ansStart, ansEnd, maxi)


def main():
    arr = [-2, -3, 4, 3, 1, 2, 7]
    print(CalculateMaximumSubarraySum(arr))

main()