

def removeDuplatedFromASortedArray(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return arr[0:i+1]


def main():
    a = [1,1,2,2,4,5,5]
    #print(set(a)) #Simple way but not optimized.
    print(removeDuplatedFromASortedArray(a))

main()