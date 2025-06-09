# #Brute Force:
#
# def main():
#     numbers = [1,1,2,2,3,4,4]
#     numberMap = {}
#
#     for num in numbers:
#         if num in numberMap:
#             numberMap[num]+=1
#         else:
#             numberMap[num]=1
#     for a,b in numberMap.items():
#         if b == 1:
#             print(a)
#
# main()


# Optimal Approach:

def main():
    numbers = [1, 1, 2, 2, 3, 4, 4]
    ans = 0
    for num in numbers:
        ans = ans ^ num
    print(ans)

main()

