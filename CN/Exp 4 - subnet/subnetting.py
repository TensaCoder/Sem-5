import math
import copy
import ipAddress as ip
# import "./ipAddress.py"

# # string='0b1100'
# # string = string[:2] + '0000' + string[2:]
# # print("Value of string after modification : "string)
def binaryModify(binaryList):
    binaryLen = 10
    for i in range(len(binaryList)):
        itemLen = binaryLen - len(binaryList[i])
        binaryList[i] = '0'*itemLen + binaryList[i][2:]    
    return binaryList

# use this function to convert decimal to 8 bit binary
def decimalToBin(decimalInput):
    # binaryList=[0*len(decimalInput)]
    binaryList = []
    for i in range(len(decimalInput)):
        binaryList.append( bin(decimalInput[i]))
    finalBinaryList = binaryModify(binaryList)

    return finalBinaryList

def correctionOfSubnetMask(subnetMask):
    foundFirst1 = False
    for j in range(3, -1, -1):
        if subnetMask[j] == '11111111':
            continue
        else:
            newOctet= ''
            for i in range(7, -1, -1):
                if subnetMask[j][i]=='0' and foundFirst1==True:
                    newOctet += '1'
                elif subnetMask[j][i]=='1' and foundFirst1==False:
                    foundFirst1 = True
                    newOctet += '1'
                else:
                    newOctet += subnetMask[j][i]

                # print(newOctet)
            # print("Value of j : {} and newOctet : {}".format(j, newOctet))
            newOctet = newOctet[::-1]
            subnetMask[j] = newOctet

    return subnetMask


def compliment(subnetMask):
    complimentList = []
    for i in range(len(subnetMask)):
        string=''
        for j in range(len(subnetMask[i])):
            if subnetMask[i][j]=='1':
                string += '0'
            elif subnetMask[i][j]=='0':
                string +='1'

        complimentList.append(string)
    return complimentList

def orOperation (startingIP, subnetMask):
    orList=[]
    for i in range(4):
        string=''
        for j in range(8):
            if startingIP[i][j]=='0' and subnetMask[i][j]=='0':
                    string += '0'
            else:
                string+='1'
        orList.append(string)
    return orList

def andOperation(ipValue, subnetValue):
    address =[]
    for i in range(len(ipValue)):
        andValue = ipValue[i] & subnetValue[i]
        address.append(andValue)

    return address

def binToDecimal(binaryValue):
    lastAddress = []
    for subarr in binaryValue:
        subarr = "0b" + subarr
        intSubarr = int(subarr, 2)
        lastAddress.append(intSubarr)
    return lastAddress


def blockSize(subnetNetLen):
    return (2**(math.ceil(math.log2(subnetNetLen))))

# calculates the number of maximum available IP addresses in the subnet mask
def maxHosts(subnetMask):
    maxHostsPower = 0
    for i in range(len(subnetMask)):
        if subnetMask[3-i] != 255:
            temp = 256 - subnetMask[3-i]
            maxHostsPower += math.log2(temp)
            
    return int((2**maxHostsPower)), int (maxHostsPower)

def over255(subnetMask, subnetNetLen, bitsAvailable):
    remainingIP = subnetNetLen
    while subnetMask[3] + remainingIP > 256:
        # Check if any more allocation is possible or not
        if bitsAvailable == 0:
            print("No more hosts can be added to the subnet")
            break
        remainingIP = remainingIP - (255 - subnetMask[3])
        # print("Value of remainingIP : {} and (256 - subnetMask[3]) : {}".format(remainingIP, (256 - subnetMask[3])))
        subnetMask[3] = 0
        bitsAvailable-=1
        # print("Inside while : subnetMask[3] : {} and remainingIP : {}".format(subnetMask[3], remainingIP))
    else:
        subnetMask[3] += remainingIP 
        # print("Inside else : subnetMask[3] : {} and remainingIP : {}".format(subnetMask[3], remainingIP))
    # print("Value of subnetMask : {}".format(subnetMask))
    return subnetMask







# Main code execution starts

# own Testing case
# ipAddress =  "172.17.14.0"                        # input("Enter the IP Address : ")
# subnetMask = "255.255.254.0"                   # input("Enter the Subnet number : ")

# Testing Case by sir
ipAddress =  "172.17.15.4"
subnetMask = "255.255.254.0"

ipAddress = list(map(int, ipAddress.split('.')))
subnetMask = list(map(int, subnetMask.split(".")))

ipAddress = andOperation(ipAddress, subnetMask)
print("Starting IP Address : {}".format(ipAddress))

maxHostNetwork, bitsAvailable = maxHosts(subnetMask)
print("Maximum number of host network available : ",maxHostNetwork)
bitsAvailable -= 8

# numOfSubnet = 4                        # input("Enter the number of subnets : ")               # set line 97 condition >256:
# subnetNetworkLength = [256, 128, 128, 64]      # To store the number of host network in a subnet 
# numOfSubnet = 1                           # for testing purpose set line 97 condition >255:
# subnetNetworkLength = [510]
numOfSubnet = 4                           # for testing purpose set line 97 condition >255:
# subnetNetworkLength = [250, 100, 60, 30]
subnetNetworkLength = [61, 121, 251, 31]
print("Total number of Hosts in all subnets : ", sum(subnetNetworkLength))

roundedSubnetNetLen = [blockSize(i) for i in subnetNetworkLength]
print(roundedSubnetNetLen)

subnetNetworkStart =[]     # To store the starting and ending host address of each subnet network
subnetNetworkEnd =[]

remainingHostNetwork = maxHostNetwork

# order to be used
# 1. decimalToBin for both ip and subnet mask
# 1.5. correctionOfSubnetMask
# 2. compliment for subnet mask
# 3. orOperation for ip and subnet mask
# 4. binToDecimal for last address

if remainingHostNetwork < 0:
    print("Error : {} is greater than the maximum number of host network available".format(roundedSubnetNetLen[0]))
    exit()

subnetNetworkStart.append(ipAddress)
ipAddress = decimalToBin(ipAddress)


# getting subnetMask for the first subnet network
if remainingHostNetwork < roundedSubnetNetLen[0]:
    print("Cannot allocate {} host network to the subnet".format(roundedSubnetNetLen[0]))
else:
    localSubnetMask = copy.copy(subnetMask)
    localSubnetMask = over255(localSubnetMask, roundedSubnetNetLen[0], bitsAvailable)
    # print("Line 152 : ", localSubnetMask)
    if localSubnetMask[3] == 256:
        localSubnetMask[3] = 0
        localSubnetMask[2] += 1
    localSubnetMask = decimalToBin(localSubnetMask)
    # print("Line 140 : Value of localSubnetMask : ", localSubnetMask)
    localSubnetMask = correctionOfSubnetMask(localSubnetMask)
    print("Line 142 : Value of localSubnetMask : ", localSubnetMask)
    localSubnetMask = compliment(localSubnetMask)
    # print("Line 144 : Local subnet mask : {}".format(localSubnetMask))

    endingIP = orOperation(ipAddress, localSubnetMask)
    endingIP = binToDecimal(endingIP)
    subnetNetworkEnd.append(endingIP)

    remainingHostNetwork -= roundedSubnetNetLen[0]


for i in range(1, numOfSubnet):
    if remainingHostNetwork < 0 or remainingHostNetwork < roundedSubnetNetLen[i]:
        print("Error : {} is greater than the maximum number of host network available".format(roundedSubnetNetLen[i]))
        break
    nextStartingIP = copy.copy(subnetNetworkEnd[i-1])
    nextStartingIP[3]+=1
    if nextStartingIP[3] >= 255:
        nextStartingIP[3] = 0
        nextStartingIP[2]+=1
        if nextStartingIP[2] >= 255:
            nextStartingIP[2] = 0
            nextStartingIP[1]+=1
            if nextStartingIP[1] >= 255:
                nextStartingIP[1] = 0
                nextStartingIP[0]+=1
                if nextStartingIP[0] >= 255:
                    print("Error : IP address is not valid")
                    exit()
    subnetNetworkStart.append(nextStartingIP)
    nextStartingIP = decimalToBin(nextStartingIP)

    localSubnetMask = copy.copy(subnetMask)
    localSubnetMask[3]+=roundedSubnetNetLen[i]
    localSubnetMask = decimalToBin(localSubnetMask)
    localSubnetMask = correctionOfSubnetMask(localSubnetMask)
    print(localSubnetMask)
    localSubnetMask = compliment(localSubnetMask)

    endingIP = orOperation(nextStartingIP, localSubnetMask)
    endingIP = binToDecimal(endingIP)
    subnetNetworkEnd.append(endingIP)
    remainingHostNetwork -= roundedSubnetNetLen[i]
    print("Remaining host network : ", remainingHostNetwork)


print("\nSubnet Network Start : {}".format(subnetNetworkStart))
print("Subnet Network End : {}".format(subnetNetworkEnd))



