import math as m


def readip(ip):
    count = 0
    ipstr = ''
    ip_array = [0]*4
    invalid = False
    for x in ip+'.':
        if isnumber(x):
            ipstr = ipstr + x
        elif x == '.' and count < 4 and inrange(ipstr):
            ip_array[count] = int(ipstr)
            count += 1
            ipstr = ''
        else:
            invalid = True
    else:
        if invalid:
            print('Invalid IP address')
            ip_array = []
    return ip_array


def ceil2(x):
    return 2**(m.ceil(m.log(x, 2)))


def arrtostr(x):
    return str(x).replace('[', '').replace(']', '').replace(',', '.').replace(' ', '')


def isnumber(x):
    flag = False
    for i in x:
        if i not in [str(j) for j in range(10)]:
            flag = True
    return not flag


def inrange(x):
    if x != '' and isnumber(x):
        return True if 0 <= int(x) < 256 else False
    return False


def createmask(n):
    count = 0
    mask = [0, 0, 0, 0]
    while n-8 > 0 and n <= 32:
        mask[count] = 255
        n -= 8
        count += 1
    for x in range(n):
        mask[count] += 2**(7-x)
    return mask


def firlast(ip, n):
    f = [0, 0, 0, 0]
    l = [0, 0, 0, 0]
    mask = createmask(n)
    for x in range(4):
        f[x] = ip[x] & mask[x]
    for x in range(4):
        l[x] = ip[x] | (255-mask[x])
    print(arrtostr(f))
    print(arrtostr(l))


def subnets(n):
    x = [0]*n
    for i in range(n):
        x[i] = ceil2((int(input(f'Enter size of subnet {i}: '))))
    print(x)
    return x


def addhosts(ip, n, size):
    size_arr = base256(size)
    res = base256add(ip, size_arr)
    m = createmask(32-n)

    if base256cmp([res[i] | (255-m[i]) for i in range(4)], [ip[i] | (255-m[i]) for i in range(4)]):
        print(([res[i] | (255-m[i]) for i in range(4)],
              [ip[i] | (255-m[i]) for i in range(4)]))
        print("Not enough addresses!")
        return None
    return res


def base256(n):
    n_arr = [0]*4
    for x in range(3, -1, -1):
        if n >= 256**(x):
            n_arr[3-x] = n//256**(x)
            n = n % (256**(x))
    return n_arr


def base256add(x, y):
    z = [0]*4
    carry = 0
    for i in range(3, -1, -1):
        z[i] = (x[i]+y[i]+carry) % 256
        carry = (x[i]+y[i]+carry)//256
    return z


def base256cmp(x, y):
    for i in range(3):
        if x[i] > y[i]:
            return True
    return False


# ip = readip(input("Enter IP: "))
ip = readip("172.17.15.3")
print("Given IP address : ", ip)
# maskn = int(input("Enter mask: "))
maskn = 23
mask = createmask(maskn)
availableHosts = 2**(32-maskn)

ip = [ip[x] & mask[x] for x in range(4)]
print("Starting IP : ",arrtostr(ip))
# sn = subnets(int(input("Enter number of subnets: ")))
sn = [64, 128, 256, 32]
totalNeededHosts = sum(sn)
i = 0

availableHosts -= totalNeededHosts

if sum(sn) <= 2**(32-maskn):
    for x in sn:
        print(f"\nSubnet {i}:")
        print(f"Mask is {arrtostr(createmask(int(32 - m.log(x,2))))}")
        print(f"First address in subnet {i} is: "+arrtostr(ip))
        ip = addhosts(ip, int(32 - m.log(x, 2)), x-1)
        print(f"Last address in subnet {i} is: "+arrtostr(ip))
        ip = base256add(ip, [0, 0, 0, 1])
        i += 1
else:
    while sum(sn) <= 2**(32-maskn):
        print("Not enough addresses!")
        sn = sn[1:]
    for x in sn:
        print(f"\nSubnet {i}:")
        print(f"Mask is {arrtostr(createmask(int(32 - m.log(x,2))))}")
        print(f"First address in subnet {i} is: "+arrtostr(ip))
        ip = addhosts(ip, int(32 - m.log(x, 2)), x-1)
        print(f"Last address in subnet {i} is: "+arrtostr(ip))
        ip = base256add(ip, [0, 0, 0, 1])
        i += 1

print("\nUnused hosts: "+str(availableHosts))
