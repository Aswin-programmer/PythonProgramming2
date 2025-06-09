# &   # AND
# |   # OR
# ^   # XOR
# ~   # NOT
# <<  # Left shift
# >>  # Right shift

def main():
    missing = [1,2,3,5]
    m1 = 0
    m2 = 0
    for itr in range(0, len(missing)):
        m1 = m1 ^ missing[itr]
        m2 = m2 ^ (itr+1)
    m2 = m2 ^ (len(missing)+1)

    print(m1 ^ m2)

main()