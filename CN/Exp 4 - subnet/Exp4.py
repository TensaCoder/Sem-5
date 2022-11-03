# Ask user for number of subnets and number of addresses in each subnet.
# Check for error : if user put in more address for subnet network than possible
# Also return the number of left over IP addresses back to the user.

# first ip : 17.12.40.0 /26         172.17.14.0
# subnetMask : 255.255.255.192 - 64 available           255.255.254.0 - 512 available
# last ip : 17.12.40.63             172.14.15.255
# 32, 16, 16                        256, 128, 128
# localSubnetStarting = [17.12.40.0, 17.12.40.32, 17.12.40.48]
# localSubnetEnding = [17.12.40.31, 17.12.40.47, 17.12.40.63]

import math

# Returns the nearest 2's power integer
def blockSize(subnetNetLen):
    return (2**(math.ceil(math.log2(subnetNetLen))))


def hostRange(startingIP, subnetMask, blockSize, remainingIP):
    endingIP =[0,0,0,0]

    for i in range(len(subnetMask)):
        if subnetMask[3-i] != 255 and endingIP[3-i]<255:
            # print("subnet and endingIP", subnetMask[3-i], endingIP)
            if remainingIP - blockSize >= 0:
                endingIP[3-i] = startingIP[3-i] + blockSize - 1
                if endingIP[3-i] > 255:
                    endingIP[3-i] = 255
                    overflow = startingIP[3-i] + blockSize - 256
                    print("Overflow : ", overflow)
                    break
            else:
                endingIP[3-i] = startingIP[3-i] + remainingIP - 1
                # print("Overflow : ", blockSize - remainingIP)

            remainingIP -= blockSize
        else:
            # print("subnet and endingIP if octet is 255 : ", subnetMask[3-i], endingIP)
            # print("EndingIP : ", endingIP)
            endingIP[3-i] = startingIP[3-i]
            # print("EndingIP : ", endingIP)

        
        # print("subnet and endingIP after for loop : ", subnetMask[3-i], endingIP)
        # print()
    
    return remainingIP, endingIP

# Main code execution starts

ipAddress =  "17.12.40.0"                        # input("Enter the IP Address : ")
subnetMask = "255.255.255.192"                   # input("Enter the Subnet number : ")

ipAddress = list(map(int, ipAddress.split(".")))
subnetMask = list(map(int, subnetMask.split(".")))

maxHostNetwork = (255 - int(subnetMask[3])) + 1
print("Maximum number of host network available : ",maxHostNetwork)

numOfSubnet = 3                         # input("Enter the number of subnets : ")
subnetNetworkLength = [32, 16, 16]      # To store the number of host network in a subnet 
roundedSubnetNetLen = [blockSize(i) for i in subnetNetworkLength]
print(roundedSubnetNetLen)

subnetNetworkStart =[]     # To store the starting and ending host address of each subnet network
subnetNetworkEnd =[]
remainingHostNetwork = maxHostNetwork

for i in range(numOfSubnet):
    if i==0:
        remainingHostNetwork, endingIP = hostRange(ipAddress, subnetMask, roundedSubnetNetLen[i], remainingHostNetwork)
        subnetNetworkStart.append(ipAddress)
        subnetNetworkEnd.append(endingIP)
    else:
        nextSubnetStart = [subnetNetworkEnd[i-1][0], subnetNetworkEnd[i-1][1], subnetNetworkEnd[i-1][2], subnetNetworkEnd[i-1][3]+1]
        subnetNetworkStart.append(nextSubnetStart)
        remainingHostNetwork, endingIP = hostRange(subnetNetworkStart[i], subnetMask, roundedSubnetNetLen[i], remainingHostNetwork)
        subnetNetworkEnd.append(endingIP)


    # print("Remaining Host Network : ", remainingHostNetwork)

    # if the remainingHostNetwork is negative that is the user has entered more host network than possible
    if remainingHostNetwork < 0:
        print("Error : Not enough host network available")
        print("Overflow of network : ", -remainingHostNetwork)
        break



summation=0         # To check if the summation of all the host network is equal to the maximum host network
for i in range(numOfSubnet):
    summation += subnetNetworkLength[i]
    if summation > maxHostNetwork:
        overflow = subnetNetworkLength[i] - ( roundedSubnetNetLen[i] + remainingHostNetwork)
        print("Number of host network that couldn't be added out of {} given : {} \n".format(subnetNetworkLength[i], overflow))
    else:
        summation = remainingHostNetwork
        print("The remaining host networks that are still available : ", summation)

# 64-48 = 16  given - (rounded - remainingIP) = overflow
# 33 - 16 = 17 -> overflow

print(subnetNetworkStart)
print(subnetNetworkEnd)