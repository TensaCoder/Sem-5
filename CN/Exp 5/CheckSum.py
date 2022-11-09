
def wrapAddition(wrappingBits, binarySendingSum):
    i = len(wrappingBits)
    j = len(binarySendingSum)
    wrappedSum = ""
    carry=0
    while i > 0:
        if wrappingBits[i-1] == '0' and binarySendingSum[j-1] == '0' and carry == 0:
            wrappedSum += '0'
        elif wrappingBits[i-1] == '0' and binarySendingSum[j-1] == '0' and carry == 1:
            wrappedSum += '1'
            carry = 0
        elif wrappingBits[i-1] == '1' and binarySendingSum[j-1] == '1':
            wrappedSum += '0'
            carry = 1
        else:
            wrappedSum += '1'
        i -= 1
        j -= 1
    # print(wrappedSum)
    while j > 0:
        if binarySendingSum[j-1] == '0' and carry == 0:
            wrappedSum += '0'
        elif binarySendingSum[j-1] == '0' and carry == 1:
            wrappedSum += '1'
            carry = 0
        elif binarySendingSum[j-1] == '1' and carry == 1:
            wrappedSum += '0'
            carry = 1
        else:
            wrappedSum += '1'
        j -= 1
    wrappedSum = wrappedSum[::-1]
    # print("Wrapped sum final : {}".format(wrappedSum))
    return wrappedSum

def wrap(lengthOfDataBit, sendingSum):
    binarySendingSum = bin(sendingSum)
    binarySendingSum = str(binarySendingSum[2:])
    # print("Binary Sending Sum : {}".format(binarySendingSum))
    wrappingLength = len(binarySendingSum) - lengthOfDataBit
    wrappingBits = binarySendingSum[:wrappingLength]
    binarySendingSum = binarySendingSum[wrappingLength:]
    wrappedSum = wrapAddition(wrappingBits, binarySendingSum)
    # print("Wrapped sum : {}".format(wrappedSum))
    return wrappedSum

def compliment(binarySum):
    complimentWrapSum = ""
    for i in range(len(binarySum)):
        if binarySum[i] == '0':
            complimentWrapSum += '1'
        else:
            complimentWrapSum +='0'
    return complimentWrapSum

#sender side
def senderSide(senderPacket, lengthOfDataBit):
    sendingSum = sum(senderPacket)
    wrappedSum = wrap(lengthOfDataBit, sendingSum)
    complimentWrapSum = compliment(wrappedSum)
    print("Sender Binary Check Sum : {}".format(complimentWrapSum))
    checkSum = int(complimentWrapSum, 2)
    print("Check Sum : {}".format(checkSum))
    senderPacket.append(checkSum)
    print("Sender packet : {}".format(senderPacket))

#receiver side
def receiverSide(senderPacket, lengthOfDataBit):
    receivingSum = sum(senderPacket)
    receiverWrapSum = wrap(lengthOfDataBit, receivingSum)
    receiverCheckSum = compliment(receiverWrapSum)

    print("\nReceiver Check Sum : {}".format(receiverCheckSum))
    if receiverCheckSum == '0'*lengthOfDataBit:
        print("No error in the packet!!!")
    else:
        print("Error in the packet!!!")
        


lengthOfDataBit = 4                                      #int(input("Enter the length of data: "))
senderPacket = [7, 11, 12, 0, 6]                         #input("Enter the packet to be sent: ")

senderSide(senderPacket, lengthOfDataBit)
# senderPacket = [7, 11, 12, 1, 6]                         # To check the error condition of CheckSum
receiverSide(senderPacket, lengthOfDataBit)