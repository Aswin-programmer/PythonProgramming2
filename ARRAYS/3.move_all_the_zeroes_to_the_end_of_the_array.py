
def MoveAllTheZeroesToTheEnd(arr):
    for i in range(0,len(arr)):
        if arr[i] == 0:
            j = i
            break
    for k in range(j+1,len(arr)):
        if arr[k]!=0:
            temp=arr[k]
            arr[k]=arr[j]
            arr[j]=temp
            j+=1
    return arr


def main():
    arr = [0,2,3,2,0,0,0,5,0]
    print(MoveAllTheZeroesToTheEnd(arr))

main()