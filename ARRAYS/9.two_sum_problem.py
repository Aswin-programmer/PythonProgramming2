# # Brute Force:
# def TwoSum(arr, target):
#     for i in arr:
#         for j in arr:
#             if (i != j):
#                 if (i + j == target):
#                     return (i, j)
#     return (-1, -1)
# def main():
#     arr = [2, 6, 5, 8, 11]
#     target = 14
#     (a, b) = TwoSum(arr, target)
#     print(a,b)
# main()

# Optimal Approach:
def TwoSumOptimal(arr, target):
    map = {}
    for x in arr:
        if x in map:
            return (x, map[x])
        map[target - x] = x
    return (-1, -1)

def main():
    arr = [2, 6, 5, 8, 11]
    target = 14
    (a, b) = TwoSumOptimal(arr, target)
    print(a,b)
main()

# # Optimal approach for only saying yes or no
# def TwoSumOptimalYesOrNo(arr, target):
#     arr.sort()
#     i = 0
#     j = len(arr)-1
#     while (i<j):
#         if arr[i] + arr[j] == target:
#             return True
#         elif arr[i] + arr[j] <= target:
#             i+=1
#         else:
#             j-=1
#     return False
#
# def main():
#     arr = [2, 6, 5, 8, 11]
#     target = 14
#     p = TwoSumOptimalYesOrNo(arr, target)
#     print(p)
# main()