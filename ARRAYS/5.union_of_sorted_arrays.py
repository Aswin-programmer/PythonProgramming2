#BruteForce:
#Using map

# def main():
#     unionMap = {} #Dictionary can be used as map in python
#     array1 = [1,2,3,4,5,5]
#     array2 = [1,2,3,4,4,6]
#
#     for item in array1:
#         if not item in unionMap:
#             unionMap[item]=1
#         else:
#             unionMap[item]+=1
#     for item in array2:
#         if not item in unionMap:
#             unionMap[item]=1
#         else:
#             unionMap[item]+=1
#     print(list(unionMap.keys()))
#
# main()

# #using set:
#
# def main():
#     #unionSet = set()
#     array1 = [1, 2, 3, 4, 5, 5]
#     array2 = [1,2,3,4,4,6]
#
#     unionSet1 = set(array1)
#     unionSet2 = set(array2)
#
#     print(unionSet1 | unionSet2)
#
#     # #Set operations
#     # a = {1, 2, 3}
#     # b = {3, 4, 5}
#     #
#     # a | b  # Union: {1, 2, 3, 4, 5}
#     # a & b  # Intersection: {3}
#     # a - b  # Difference: {1, 2}
#     # a ^ b  # Symmetric Difference: {1, 2, 4, 5}
# main()

#Optimal Approach:
def main():
    array1 = [1, 2, 3, 4, 5, 6]
    array2 = [1, 3, 5, 6, 8, 9]

    i = 0
    j = 0
    unionList = []
    while ((i < len(array1)) and (j < len(array2))):
        if array1[i] <= array2[j]:
            if len(unionList)==0 or unionList[-1]!=array1[i]:
                unionList.append(array1[i])
            i+=1
        else:
            if len(unionList)==0 or unionList[-1]!=array2[j]:
                unionList.append(array2[j])
            j+=1
    while i < len(array1):
        if unionList[-1] != array1[i]:
            unionList.append(array1[i])
        i+=1
    while j < len(array2):
        if unionList[-1] != array2[j]:
            unionList.append(array2[j])
        j+=1

    for element in unionList:
        print(element)

main()