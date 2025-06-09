
def FindLeaderOfAnArray(arr):
    ans = []
    maxi = float('-inf')

    for i in range(len(arr)-1, 0, -1):
        if maxi < arr[i]:
            ans.append(arr[i])
        maxi = max(maxi, arr[i])

    return ans

def main():
    arr = [10, 22, 12, 3, 0, 6]
    print(FindLeaderOfAnArray(arr))
main()