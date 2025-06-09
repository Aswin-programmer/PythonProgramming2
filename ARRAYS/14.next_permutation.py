
def CustomListReverse(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1

def NextGreatestPermutation(arr):
    index = -1
    swapIndex = -1
    for i in range(len(arr)-1, 1, -1):
        if arr[i] > arr[i-1]:
            index = i-1
            break

    if index == -1:
        return [-1]

    for i in range(len(arr)-1, index, -1):
        if arr[i] > arr[index]:
            swapIndex = i
            break

    # Swaping
    temp = arr[index]
    arr[index] = arr[swapIndex]
    arr[swapIndex] = temp

    CustomListReverse(arr, index+1, len(arr) - 1)
    #arr[2 : 6 : -1]

    return arr


def main():
    arr = [3, 1, 2]
    print(NextGreatestPermutation(arr))
main()