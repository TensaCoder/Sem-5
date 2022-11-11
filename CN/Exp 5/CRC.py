
def EXOR(dividend, divisor):
    quotient=""
    remainder = ""
    if dividend[0] != divisor[0]:
        quotient+="0"
        remainder = dividend
        return quotient, remainder

    for i in range(len(divisor)):
        if dividend[i] == divisor[i]:
            remainder+="0"
        else:
            remainder+="1"
    quotient+="1"
    return quotient, remainder

def bitwiseShift(remainder):
    temp = ""
    for i in range(len(remainder)-1):
        temp+=remainder[i+1]
    remainder = temp
    return remainder

def CRC(augmentedData, divisor):
    finalQuotient =""
    remainder = ""
    quotient, remainder = EXOR(augmentedData[0:len(divisor)], divisor)
    finalQuotient+=quotient
    for i in range(1, len(divisor)):
        remainder = bitwiseShift(remainder)
        remainder+= augmentedData[i+len(divisor)-1]
        quotient, remainder = EXOR(remainder, divisor)
        finalQuotient+=quotient

    return finalQuotient, remainder[1:]





data = "1001"                     # Data to be transmitted
divisor = "1011"                  # Divisor
augmentedData = data + "0" * (len(divisor) - 1)   # Appending 0's to data => 1001000
quotient, remainder = CRC(augmentedData, divisor)

print('Sender side :')
print("Quotient : ", quotient)
print("Remainder : ", remainder)

data +=remainder
print("Final Codeword : ", data)

# receiverData = data
# running CRC at receiver side
# receiverData = "1001001"
receiverData = str(input("Enter the data word : "))
print("\nReceiver Side :")
quotient, remainder = CRC(receiverData, divisor)
print("Quotient : ", quotient)
print("Remainder : ", remainder)
if remainder == "0" * (len(divisor) - 1):
    print("No Error!!! Data Received Successfully!")
else:
    print("Error!!!")






