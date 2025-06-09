
# def ElementMoreThanHalfTimes(arr):
#     elementDict = {}
#     for x in arr:
#         if x in elementDict:
#             elementDict[x] = elementDict[x] + 1
#         else:
#             elementDict[x] = 1
#
#     for x in arr:
#         if elementDict[x] > len(arr)/2:
#             return x
# 
#     return -1

def ElementMoreThanHalfTimesOptimized(arr):
    cnt = 0
    num = -1
    for x in arr:
        if cnt == 0:
            num = x
            cnt = 1
        else:
            if num == x:
                cnt += 1
            else:
                cnt -= 1

    return num




def main():
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(ElementMoreThanHalfTimesOptimized(arr))

main()