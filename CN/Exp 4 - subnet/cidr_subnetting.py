#  line 94, 99, 149

# address_cidr = input("Enter IP address in CIDR format: ")
address_cidr = "172.17.15.4/23"
a = address_cidr.split('/')
ip_address = a[0]
x = int(a[1])

flag = 0
count = 0
unused = 0

unused = unused+pow(2, 32-x)  # initialized with all hosts from 32-x host bits

ipLower = ""
ipHigher = ""
lower = []
higher = []

# Checking Validity of IP Address Entered
if len(ip_address) > 15:
    flag = 1
    print("Invalid IP address")
    exit()

for i in ip_address:
    if i == ".":
        count = count + 1

if count != 3:
    flag = 1
    print("Invalid IP address")
    exit()

octet = ip_address.split(".", 4)
for i in range(0, len(octet)):
    octet[i] = int(octet[i])
    if octet[i] > 255:
        flag = 1
        print("Invalid IP address")
        exit()


created_mask = []
tmp = []

# If a valid IP Address then proceed
if flag == 0:
    lower = []
    higher = []
    ipLower = ""
    ipHigher = ""

    # IP Address in binary
    print("\nIP address in binary:")
    for i in octet:
        print(format(int(i), '08b'), end="")

    # Creating the mask
    for i in range(0, x):  # x has no. of domain bits
        tmp.append("1")
    for i in range(x, 32):
        tmp.append("0")
    print("\n\nSubnet address in binary:")
    for i in tmp:
        print(i, end="")

    result = []
    for i in range(0, len(tmp), 8):
        result.append("".join(tmp[i:i+8]))
    for i in range(0, len(result)):
        created_mask.append(int(result[i], 2))  # converting to decimal

    print("\n\nComplement of Subnet address in binary:")
    for i in range(0, len(created_mask)):
        print(format(int(255 - created_mask[i]), '08b'), end="")

    # Lower 1St IP Address by anding with mask
    for i in range(0, len(octet)):
        lower.append(str(octet[i] & created_mask[i]))
    # generating string for lower IP address
    ipLower = ipLower + lower[0] + "." + \
        lower[1] + "." + lower[2] + "." + lower[3]
    print("\n\nThe First address: " + ipLower)

    # Higher 2nd IP Address by oring with complement of mask
    for i in range(0, len(octet)):
        # or operation with ip address and complement of subnet
        higher.append(str(octet[i] | (255 - created_mask[i])))
    # generating string for higher IP address
    ipHigher = ipHigher + higher[0] + "." + \
        higher[1] + "." + higher[2] + "." + higher[3]
    print("The Last address: " + ipHigher)

    print()
    # n = int(input("\nEnter number of sub blocks: "))
    n =4
    subnetNetworkLength = [61, 121, 251, 31]

    # for first subnet
    # number = int(input("\nEnter number of IP address required: "))
    number = subnetNetworkLength[0]


    b = 0
    # Checking if ip addresses requried are available
    if(number > unused):
        b = 1
    if(b == 0):
        created_mask.clear()
        result.clear()
        tmp.clear()
        x = 0

        while 2 ** x < number:  # IMP
            x = x + 1
        unused = unused-pow(2, x)  # updated unused ip count of network
        print(f"Mask: /{32-x}")
        for i in range(0, 32-x):
            tmp.append("1")
        for i in range(32-x, 32):
            tmp.append("0")
        for i in range(0, len(tmp), 8):
            result.append("".join(tmp[i:i + 8]))
        for i in range(0, len(result)):
            created_mask.append(int(result[i], 2))
        for i in range(0, len(lower)):
            lower[i] = int(lower[i])
        for i in range(0, len(higher)):
            higher[i] = int(higher[i])
        subblockLower = []
        subblockHigher = []
        ipLower = ""
        ipHigher = ""
        for i in range(0, len(lower)):
            subblockLower.append(lower[i])
        print("For Sub block 1:")
        for j in range(0, len(subblockLower)):
            subblockHigher.append(
                int(subblockLower[j]) | (255 - created_mask[j]))
        ipLower = ipLower + str(subblockLower[0]) + "." + str(
            subblockLower[1]) + "." + str(subblockLower[2]) + "." + str(subblockLower[3])
        ipHigher = ipHigher + str(subblockHigher[0]) + "." + str(
            subblockHigher[1]) + "." + str(subblockHigher[2]) + "." + str(subblockHigher[3])
        print(f"First address: {ipLower}")
        print(f"Last address: {ipHigher}")

        # for remaining subnets
        for k in range(1, n):
            b = 0
            # number = int(input("\nEnter number of IP address required: "))
            number = subnetNetworkLength[k]

            if(number > unused):
                b = 1
            if(b == 0):
                created_mask.clear()
                result.clear()
                tmp.clear()
                x = 0
                while 2 ** x < number:
                    x = x + 1
                unused = unused-pow(2, x)
                print(f"Mask:/{32-x}")
                for i in range(0, 32-x):
                    tmp.append("1")
                for i in range(32-x, 32):
                    tmp.append("0")
                for i in range(0, len(tmp), 8):
                    result.append("".join(tmp[i:i + 8]))
                for i in range(0, len(result)):
                    created_mask.append(int(result[i], 2))
                for i in range(0, len(lower)):
                    lower[i] = int(lower[i])
                for i in range(0, len(higher)):
                    higher[i] = int(higher[i])

                subblockLower[3] = subblockHigher[3] + 1
                if subblockLower[3] > 255:
                    subblockLower[3] = 0
                    subblockLower[2] = subblockLower[2] + 1
                    if subblockLower[2] > 255:
                        subblockLower[2] = 0
                        subblockLower[1] = subblockLower[1] + 1
                        if subblockLower[1] > 255:
                            subblockLower[2] = 0
                            subblockLower[1] = subblockLower[1] + 1
                subblockHigher = []
                ipLower = ""
                ipHigher = ""
                for j in range(0, len(subblockLower)):
                    subblockHigher.append(
                        int(subblockLower[j]) | (255 - created_mask[j]))
                ipLower = ipLower + str(subblockLower[0]) + "." + str(subblockLower[1]) + "." + str(
                    subblockLower[2]) + "." + str(subblockLower[3])
                ipHigher = ipHigher + str(subblockHigher[0]) + "." + str(subblockHigher[1]) + "." + str(
                    subblockHigher[2]) + "." + str(subblockHigher[3])
                print(f"For Sub block: {k+1}")
                print(f"First address: {ipLower}")
                print(f"Last address: {ipHigher}")
            else:
                print("Required no of addresses not available")
    else:
        print("Required no of addresses not available")
    print()
    print(f"Unused addresses: {unused}")
