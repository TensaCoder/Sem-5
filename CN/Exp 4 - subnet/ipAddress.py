# ip : 172.17.14.24         196.168.86.42
# subnet : 255.255.254.0    255.255.254.0

def dotToArray(inputDot):
    inputList = inputDot.split(".")
    for i in range (len(inputList)):
        inputList[i] = int(inputList[i])
    return inputList

def decimalToBin(decimalInput):
    # binaryList=[0*len(decimalInput)]
    binaryList = []
    for i in range(len(decimalInput)):
        binaryList.append( bin(decimalInput[i] ))
    complimentList = binaryModify(binaryList)

    return complimentList

# # string='0b1100'
# # string = string[:2] + '0000' + string[2:]
# # print("Value of string after modification : ",string)
def binaryModify(binaryList):
    binaryLen = 10
    for i in range(len(binaryList)):
        itemLen = binaryLen - len(binaryList[i])
        binaryList[i] = '0'*itemLen + binaryList[i][2:]    
    return binaryList


def compliment(binaryList):
    complimentList = []
    for i in range(len(binaryList)):
        string=''
        for j in range(len(binaryList[i])):
            if binaryList[i][j]=='1':
                string += '0'
            elif binaryList[i][j]=='0':
                string +='1'

        complimentList.append(string)
    return complimentList
    

def andOperation(ipValue, subnetValue):
    address =[]
    for i in range(len(ipValue)):
        andValue = ipValue[i] & subnetValue[i]
        address.append(andValue)

    return address

def orOperation (ipValue, subnetValue):
    orList=[]
    for i in range(len(ipValue)):
        string=''
        for j in range(len(ipValue[i])):
            if ipValue[i][j]=='0' and subnetValue[i][j]=='0':
                string += '0'
            else:
                string+='1'
        orList.append(string)
    return orList

def binToDecimal(binaryValue):
    lastAddress = []
    for subarr in binaryValue:
        subarr = "0b" + subarr
        intSubarr = int(subarr, 2)
        lastAddress.append(intSubarr)

    return lastAddress

# string='0b1100'
# string = '0b'+ string
# print("Value of string after modification : ",string)

def main():
    ipAddress = input("Enter the IP Address : ")
    subnetMask = input("Enter the IP Address : ")

    ipValue= dotToArray(ipAddress)
    subnetValue= dotToArray(subnetMask)

    ipBinaryValue= decimalToBin(ipValue)
    # print('Binary of Ip',ipBinaryValue)


    subnetBinaryValue= decimalToBin(subnetValue)
    subnetCompliment = compliment(subnetBinaryValue)
    # print("Compliment of subnet : ",subnetCompliment)

    #  Calculates the first address of the block
    firstAddress = andOperation(ipValue, subnetValue)

    # Calculates the last address of the block
    lastAddressBinary = orOperation(ipBinaryValue, subnetCompliment)

    # print("line 119",lastAddressBinary)
    lastAddress = binToDecimal(lastAddressBinary)

    print("\n")
    if ipValue[0] in range(0,127):
        print("Class A type Network!")
    elif ipValue[0] in range(128,191):
        print("Class B type Network!")
    elif ipValue[0] in range(192, 223):
        print("Class C type Network!")
    elif ipValue[0] in range(224, 239):
        print("Class D type Network!")
    elif ipValue[0] in range(240, 254):
        print("Class E type Network!")
    else:
        print("You have entered wrong IP Address!!!")

    # Print the first and last address
    print("First Address : ",firstAddress)
    print("Last Address : ",lastAddress)


if __name__ == "__main__":
    main()