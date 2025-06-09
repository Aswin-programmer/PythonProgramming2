
def swapNumbers(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while (mid <= high):
        if arr[mid] == 0:
            swapNumbers(arr, mid, low)
            low+=1
            mid+=1
        elif arr[mid] == 2:
            swapNumbers(arr, mid, high)
            high-=1
        else:
            mid+=1
    return arr

def main():
    arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(sortArray(arr))

main()
