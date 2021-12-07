import sys #For using CLI arguments. Change to argparse in future versions

def printAll(a): #Prints all triplets with sum 0
    N = len(a)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if a[i]+a[j]+a[k] == 0:
                    print(str(a[i]) + " " + str(a[j]) + " " + str(a[k])

def count(a): #Returns count of triplets with sum 0
    N = len(a)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if a[i]+a[j]+a[k] == 0:
                    count += 1
    return count

def main():
    zero_threesum_count = count([int(i) for i in sys.argv[1:]]) #Unable to pass files. Improve with argparse
    print("Number of zero-sum triplets\t:\t", zero_threesum_count)

if __name__ == "__main__":
    main()
