def checkPresence(completedProcessIndices, index):
    for i in range(len(completedProcessIndices)):
        if index == completedProcessIndices[i]:
            return False
    return True


def findShortestProcess(readyQueue, time, completedProcessIndices):
    shortestProcess = readyQueue[0]
    index = 0
    for i in range(numberOfProcess):
        indexNotPresent = checkPresence(completedProcessIndices, i)
        if indexNotPresent:
            shortestProcess = readyQueue[i]
        else:
            continue
    for i in range(numberOfProcess):

        condition1 = readyQueue[i][0] <= time                          # checking if the arrival time is less than or equal to the current time
        condition2 = readyQueue[i][1] <= shortestProcess[1]             # checking if the burst time is less than the shortest process
        condition3 = checkPresence(completedProcessIndices, i)          # checking if the process is not completed

        if condition1 and condition2 and condition3:
            shortestProcess = readyQueue[i]
            index=i
    return index

def SJF():
    completedProcessIndices = []
    time = 0
    shortestProcessIndex = findShortestProcess(readyQueue, time, completedProcessIndices)
    # Appending the waitingTime[2], completionTime[3] and turnAroundTime[4] for the first process to the finalProcessList
    # finalProcessList = [arrivalTime, burstTime, waitingTime, completionTime, turnAroundTime]
    finalProcessList[shortestProcessIndex].append(0)    #waiting time
    finalProcessList[shortestProcessIndex].append(finalProcessList[shortestProcessIndex][0] + finalProcessList[shortestProcessIndex][1])       # completionTime
    finalProcessList[shortestProcessIndex].append(finalProcessList[shortestProcessIndex][3] - finalProcessList[shortestProcessIndex][0])    # turnAroundTime

    time= finalProcessList[shortestProcessIndex][3]
    completedProcessIndices.append(shortestProcessIndex)
    previousProcessIndex = shortestProcessIndex

    for i in range(numberOfProcess-1):
        shortestProcessIndex = findShortestProcess(readyQueue, time, completedProcessIndices)

        # Appending the waitingTime[2], completionTime[3] and turnAroundTime[4] for the first process to the finalProcessList
        # finalProcessList = [arrivalTime, burstTime, waitingTime, completionTime, turnAroundTime]
        finalProcessList[shortestProcessIndex].append(finalProcessList[previousProcessIndex][3] - finalProcessList[shortestProcessIndex][0])        # waiting time

        finalProcessList[shortestProcessIndex].append(finalProcessList[previousProcessIndex][3] + finalProcessList[shortestProcessIndex][1])        # completionTime

        finalProcessList[shortestProcessIndex].append(finalProcessList[shortestProcessIndex][3] - finalProcessList[shortestProcessIndex][0])        # turnAroundTime

        time+= finalProcessList[shortestProcessIndex][3]
        completedProcessIndices.append(shortestProcessIndex)
        previousProcessIndex = shortestProcessIndex


    waitingTime, turnAroundTime = 0, 0
    print("Process \t Arrival Time \t Burst Time  \t Waiting Time \t Completion Time \t Turn Around Time")
    for i in range(numberOfProcess):
        print(i+1, "\t\t", finalProcessList[i][0], "\t\t", finalProcessList[i][1], "\t\t", finalProcessList[i][2], "\t\t", finalProcessList[i][3], "\t\t\t", finalProcessList[i][4])

        waitingTime+= finalProcessList[i][2]
        turnAroundTime += finalProcessList[i][4]

    averageWaitingTime = waitingTime/ numberOfProcess
    averageTurnAroundTime = turnAroundTime/ numberOfProcess

    print("Average Waiting Time : ", averageWaitingTime)
    print("Average Turn Around Time : ", averageTurnAroundTime)


numberOfProcess = 4            # int(input("Enter the number of processes : "))
arrivalTime, burstTime  = [], []
# finalProcessList = [arrivalTime, burstTime, waitingTime, completionTime, turnAroundTime]
finalProcessList=[]
# arrivalTime=[0,1,2,3,6]
# burstTime=[2,6,4,9,12]
arrivalTime=[0,2,4,5]
burstTime=[7,4,1,5]

readyQueue = []
for i in range(numberOfProcess):
    readyQueue.append([arrivalTime[i], burstTime[i]])

finalProcessList = readyQueue
print(finalProcessList)
SJF()