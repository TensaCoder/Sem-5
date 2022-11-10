def conversionToAscii(inputString):
    asciiValue = []
    for i in inputString:
        asciiValue.append(ord(i))
    return asciiValue



def conversionToHex(asciiValue):
    hexValue = []

    for i in asciiValue:
        hexValue.append(str(hex(i)[2:]))

    for i in range(0, len(hexValue)-2):
        hexValue[i:i+2] = [''.join(hexValue[i: i+2])]

    while ("" in hexValue):
        hexValue.remove("")
    
    for i in range(len(hexValue)):
        if len(hexValue[i]) < 4:
            x = len(hexValue[i])
            x = 4-x
            for j in range(x):
                hexValue[i] +="0"

    return hexValue


def sum(hexValue, checksum):
    sum = 0
    for i in range(len(hexValue)):
        sum += int(hexValue[i], 16)
    sum += int(checksum, 16)
    sum = hex(sum)
    fsum = sum[2:]

    while (len(fsum) > 4):
        carry = fsum[0]
        fsum = fsum[1:]
        sum2 = hex(int(carry, 16)+int(fsum, 16))

    finalSum = sum2[2:]

    checksumlist = []
    for i in finalSum:
        checksumlist.append(hex(15-int(i, 16)))
    for i in range(len(checksumlist)):
        f = checksumlist[i]
        checksumlist[i] = f[2:]

    checksum = ''.join(str(x) for x in checksumlist)
    return checksum


print("*"*20+"      Sender End      " + "*"*20)
# inputString = input("Enter the text value :  ")
inputString = "kjsomaiya"
initialchecksum = "0000"
asciiValue = conversionToAscii(inputString)
print("ASCII VALUE : ", asciiValue)
hexValue = conversionToHex(asciiValue)
print("HEX VALUE : ", hexValue)
checksum = sum(hexValue, initialchecksum)


print("Value of checksum to be sent :", checksum)


print("\n")
print("*"*20 + "        Receiver End        " + "*"*20)
# inputString2 = input("Enter the text value :  ")
inputString2 = "kjsomaiya"
asciiValue2 = conversionToAscii(inputString2)
print("ASCII VALUE : ", asciiValue2)
hexValue2 = conversionToHex(asciiValue2)
print("HEX VALUE : ", hexValue2)
checksum2 = sum(hexValue2, checksum)

print("Final Value of CheckSum at receiver end : ", checksum2)

check = int(checksum2, 16)

if (check == 0):
    print("\nError Not Found!!!")
else:
    print("\nError Found in Data!!!")
