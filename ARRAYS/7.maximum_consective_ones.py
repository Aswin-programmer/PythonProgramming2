
def main():
    onesList = [1, 1, 0, 1, 1, 1, 0, 1]

    count = 0
    maxi = 0

    for itr in onesList:
        if itr == 1:
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    print(maxi)

main()