# Calculates differenceerence of each track number with the head position
def calculateDifference(queue, head, difference):
    for i in range(len(difference)):
        difference[i][0] = abs(queue[i] - head)


# find unaccessed track which is at minimum distance from head
def findMin(difference):

    index = -1
    minimum = 999999999

    for i in range(len(difference)):
        if (not difference[i][1] and
                minimum > difference[i][0]):
            minimum = difference[i][0]
            index = i
    return index

# prints the sequence
def printSequence(seek_sequence):
    for i in range(len(seek_sequence)-1):
        print(str(seek_sequence[i]) + " ->", end=" ")
    print(seek_sequence[len(seek_sequence)-1])


def shortestSeekTimeFirst(request, head):
    if (len(request) == 0):
        return

    size = len(request)
    difference = [0] * size

    # initialize array
    for i in range(size):
        difference[i] = [0, 0]

    # count total number of seek operation
    seek_count = 0

    # stores sequence in which disk
    # access is done
    seek_sequence = [0] * (size + 1)

    for i in range(size):
        seek_sequence[i] = head
        calculateDifference(request, head, difference)
        index = findMin(difference)

        difference[index][1] = True

        # increase the total count
        seek_count += difference[index][0]

        # accessed track is now new head
        head = request[index]

    # for last accessed track
    seek_sequence[len(seek_sequence) - 1] = head

    print("Total number of seek operations =", seek_count)

    print("\nSeek Sequence :")

    # print the sequence
    printSequence(seek_sequence)


# Driver code
if __name__ == "__main__":

    # request array
    proc = [176, 79, 34, 60, 92, 11, 41, 114]
    shortestSeekTimeFirst(proc, 50)
