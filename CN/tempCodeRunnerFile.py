import math

def maxHosts(subnetMask):
    maxHostsPower = 0
    for i in range(len(subnetMask)):
        if subnetMask[3-i] != 255:
            temp = 256 - subnetMask[3-i]
            print("Value of temp : ", temp)
            maxHostsPower += math.log2(temp)
        print("Value of maxHostsPower for i {} : {}".format(i, maxHostsPower))  

subnetMask = [255, 255, 254, 0]
maxHosts(subnetMask)