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

# calculates the number of maximum available IP addresses in the subnet mask
def maxHosts(subnetMask):
    maxHostsPower = 0
    for i in range(len(subnetMask)):
        if subnetMask[3-i] != 255:
            temp = 256 - subnetMask[3-i]
            maxHostsPower += math.log2(temp)
            
    return int((2**maxHostsPower)), int(maxHostsPower)

def continuousHost(startingIP, endingIP, i):
    for j in range(i):
        if endingIP[j]!=0:
            endingIP[j] += startingIP[j]
        else:
            endingIP[j] = startingIP[j]
        # endingIP[j] = startingIP[j]
        print("line 32 : endingIP[3-i] : ", endingIP)

def hostRange(startingIP, subnetMask, blockSize, remainingIP):
    endingIP = [0,0,0,0]                             # startingIP
    for i in range(len(subnetMask)):
        if subnetMask[3-i] != 255 and endingIP[3-i]<255:
            print("line 37 : subnet and endingIP {} : {}, {} ".format(3-i, subnetMask[3-i], endingIP))
            if remainingIP - blockSize >= 0:                            # when there are ip to allot
                checkPoint = startingIP[3-i] + blockSize                # 0 + 512 => target ip value to reach 
                print("Line 40 : checkPoint : ",checkPoint)
                #Test case 1 : 0 + 512 = 512
                #Test case 2 : 128 + 512 = 640 try this later
                # if the checkpoint is greater than 255, then we need to add 1 to the previous octet and reset the current octet to 0 and add the remainingVal to the current octet
                if checkPoint + endingIP[3-i] > 255:                    # 512 + 0 > 255     to check if the endingIp is more than 255
                    print("line 45 : {}, {} ".format(checkPoint, endingIP[3-i]))
                    remainingVal = checkPoint - (256 - endingIP[3-i])       # 512 - 256 + 0 = 256
                    endingIP[3-i -1]+=1                             # 172.17.15.0
                    print("line 47 : remaining Value", remainingVal)
                    while remainingVal > (255 - endingIP[3-i]):
                        endingIP[3-i -1]+=1                             # 172.17.15.0
                        remainingVal = checkPoint - (256 - endingIP[3-i])       # 512 - 256 + 0 = 256
                        print("line 51 : remaining Value", remainingVal)
                    print("line 52 : remaining Value", remainingVal)
                    endingIP[3-i] = remainingVal
                    print("line 54 : endingIP[3-i] : ", endingIP)
# working here                    continuousHost(startingIP)
                else:                                                           # if the checkpoint + endingIP is below 255 
                    endingIP[3-i] = checkPoint
                    continuousHost(startingIP, endingIP, 3-i)
                    # for j in range(3-i):
                    #     endingIP[j] = startingIP[j]
                    # print("line 58 : endingIP[3-i] : ", endingIP)
                    break

            else:                                                               # incase user wants more ip than we can allocate
                endingIP[3-i] = startingIP[3-i] + remainingIP - 1
                print("line 63 : Overflow  when subnet mask != 255 : ", blockSize - remainingIP)
            print("line 64 : For when subnet mask != 255 : ",endingIP[3-i])
            # continuousHost(startingIP, endingIP, 3-i)
            remainingIP -= blockSize
        else:
            # subnet mask is 255, so endingIP octet is the same as startingIP octet
            if endingIP[3-i]!=0:
                endingIP[3-i] += startingIP[3-i]
            else:
                endingIP[3-i] = startingIP[3-i]
            print("line &2 : For when subnet mask = 255 : ",endingIP[3-i])

    return remainingIP, endingIP



# Main code execution starts

ipAddress =  "172.17.14.0"                        # input("Enter the IP Address : ")
subnetMask = "255.255.254.0"                   # input("Enter the Subnet number : ")

ipAddress = list(map(int, ipAddress.split(".")))
subnetMask = list(map(int, subnetMask.split(".")))

maxHostNetwork, bitsAvailable = maxHosts(subnetMask)
print("Maximum number of host network available : ",maxHostNetwork)

numOfSubnet = 3                         # input("Enter the number of subnets : ")
subnetNetworkLength = [64, 128, 128]      # To store the number of host network in a subnet 
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

# 64-48 = 16  given - (rounded - remainingIP) = overflow
# 33 - 16 = 17 -> overflow

print(subnetNetworkStart)
print(subnetNetworkEnd)



# try coding it without using a for loop, bcoz ip need to be given from the last octet only if the octet crosses 255 then +1 to the previous octet,if that too is above 255 then 