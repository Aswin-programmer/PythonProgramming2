
def rotateList(arr, start, end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1

def rotateArrayByKPlaces(arr, k):
    rotateList(arr,0,k-1)
    rotateList(arr,k,len(arr)-1)
    rotateList(arr,0,len(arr)-1)

def main():
    a = [1,2,3,4,5]
    rotateArrayByKPlaces(a,3)
    print(a)

main()