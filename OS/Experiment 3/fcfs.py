import time

def FCFS():
    waitingTime.append(0)
    completionTime.append(arrivalTime[0] + burstTime[0])
    turnAroundTime.append(completionTime[0] - arrivalTime[0])
    # used to calculate the waitingTime, completionTime and turnAroundTime for each process
    for i in range(1, numberOfProcess):
        processWaitingTime = completionTime[i-1] - arrivalTime[i]
        waitingTime.append(processWaitingTime)
        
        processCompletionTime = completionTime[i-1] + burstTime[i]
        completionTime.append(processCompletionTime)
        
        processTurnAroundTime = completionTime[i] - arrivalTime[i]
        turnAroundTime.append(processTurnAroundTime)
    

    averageWaitingTime = sum(waitingTime) / numberOfProcess
    averageTurnAroundTime = sum(turnAroundTime) / numberOfProcess
    print("Process \t Arrival Time \t Burst Time  \t Waiting Time \t Completion Time \t Turn Around Time")
    for i in range(numberOfProcess):
        print(i+1, "\t\t", arrivalTime[i], "\t\t", burstTime[i], "\t\t", waitingTime[i], "\t\t", completionTime[i], "\t\t\t", turnAroundTime[i])

    print("\nAverage Waiting Time: ", averageWaitingTime)
    print("Average Turn Around Time: ", averageTurnAroundTime)


numberOfProcess = int(input("Enter the number of processes : "))
arrivalTime, burstTime, completionTime, waitingTime, turnAroundTime  = [], [], [], [], []
arrivalTime=[0,1,2,3,6]
burstTime=[2,6,4,9,12]
# for i in range(numberOfProcess):
#     processArrivalTime, processBurstTime = int(input("Enter the arrival time and burst time of process {} : ".format(i+1)))
#     arrivalTime.append(processArrivalTime)
#     burstTime.append(processBurstTime)

t1=time.time()
FCFS()
t2=time.time()
print("Time taken by FCFS execution : ",t2-t1, " sec")
