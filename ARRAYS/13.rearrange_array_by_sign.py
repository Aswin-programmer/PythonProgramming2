# This problem has two main cases:
# 1. When the number of positive and negative elements are equal.(BruteForce + OptimalApproach)
# 2. When the number of positive elements and negative elements are not equal. (BruteForce)

# def RearrangeCase1(arr):
#     positiveElm = []
#     negativeElm = []
#     for x in arr:
#         if x > 0:
#             positiveElm.append(x)
#         else:
#             negativeElm.append(x)
#
#     ans = []
#     for i in range(0, len(positiveElm)):
#         ans.insert(2*i, positiveElm[i])
#         ans.insert(2*i + 1, negativeElm[i])
#
#     return ans

def RearrangeCase1Optimal(arr):
    positiveIndex = 0
    negativeIndex = 1

    ans = []

    for i in range(0, len(arr)):
        if arr[i] > 0:
            ans.insert(positiveIndex, arr[i])
        else:
            ans.insert(negativeIndex, arr[i])
    return ans


def main():
    arr = [3, 1, -2, -5, 2, -4]
    print(RearrangeCase1Optimal(arr))
main()