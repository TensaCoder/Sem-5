def FCFS(arr, head):
    seek_count = 0
    distance, cur_track = 0, 0
    size = len(arr)

    for i in range(size):
        cur_track = arr[i]

        # calculate the absolute distance between tracks
        distance = abs(cur_track - head)
        # increase the total count
        seek_count += distance
        # accessed track is now new head
        head = cur_track

    print("Total number of seek operations = ", seek_count)
    print("\nSeek Sequence : ")

    for i in range(size-1):
        print(str(arr[i]) + " -> ", end="")
    print(arr[size-1])

# Driver code
if __name__ == "__main__":

    arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
    head = 50

    FCFS(arr, head)