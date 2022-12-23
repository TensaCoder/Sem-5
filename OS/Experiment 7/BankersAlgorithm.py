if __name__ =="__main__":
    numOfProcess = 5
    numOfResources = 3

    numOfProcess = 4
    numOfResources = 1

    #Given resources at the start
    # available = [10, 5, 7]
    available = [150]

    # Allocation Matrix
    # allocation = [[0, 1, 0 ], [ 2, 0, 0 ], [3, 0, 2 ], [2, 1, 1], [ 0, 0, 2]]
    allocation = [[45], [40], [15], [35]]

    # MAX Matrix
    # max = [[7, 5, 3 ], [3, 2, 2 ], [ 9, 0, 2 ], [2, 2, 2], [4, 3, 3]]
    max = [[70], [60], [60], [60]]

    # creating the matrix for showing the available resources
    for i in range(numOfProcess):
        for j in range(numOfResources):
            available[j] -= allocation[i][j]
        # available[0] -= allocation[i][0]
        # available[1] -= allocation[i][1]
        # available[2] -= allocation[i][2]
    
    # print(available)

    finished = [0] * numOfProcess
    #to store the sequence in which the process are finished in
    safeSequence = []  
    index = 0

    need = [[ 0 for i in range(numOfResources)]for i in range(numOfProcess)]

    for i in range(numOfProcess):
        for j in range(numOfResources):
            need[i][j] = max[i][j] - allocation[i][j]
    print("Need : ",need)
    
    for k in range(10):
        for i in range(numOfProcess):
            if (finished[i] == 0):
                flag=0
                for j in range(numOfResources):
                    if (need[i][j] > available[j]):
                        flag = 1
                        print("\nSkipping Process ",i)
                        break
                    
                if (flag == 0):
                    safeSequence.append(i)
                    for y in range(numOfResources):
                        available[y] += allocation[i][y]
                    print("\nCompleted Process",i)
                    finished[i] = 1
                    print("Available : ",available)
    
    print("\nFollowing is the Sequence : ")
    for i in range(len(safeSequence)-1):
        print(" P", safeSequence[i], " ->", sep="", end="")
    print(" P", safeSequence[numOfProcess - 1], sep="")
    