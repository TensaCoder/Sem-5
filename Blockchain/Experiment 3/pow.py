import hashlib
import time
# write a function to calculate the hash of a string using hashlib.sha256‘s hexdigest() method
def hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

# write a function to accept blockNumber, blockData, and previousHash as parameters from the user and return a string with the blockNumber, blockData, and previousHash concatenated together
def blockToString(blockNumber, nonce, blockData, previousHash):
    return str(blockNumber) + " : " + str(nonce) + " : " + blockData + " : " + previousHash

# write a function to accept a list of strings as input and return all elements concatenated together
def concatList(l):
    return ', '.join(l)

# write a function to produce a hash that starts with 0000
def findHash(blockNumber, blockData, previousHash):
    nonce = 0
    completeData = blockToString(blockNumber, nonce, blockData, previousHash)
    hashValue = hash(completeData)
    while hashValue[:4] != "0000":
        nonce += 1
        completeData = blockToString(blockNumber, nonce, blockData, previousHash)
        hashValue = hash(completeData)
    # print("Value of nonce : ",nonce)
    return hashValue, nonce

# write a function to produce a hash that starts with 0000 including difficulty
def findHashWithDifficulty(blockNumber, blockData, previousHash, difficulty):
    nonce = 0
    completeData = blockToString(blockNumber, nonce, blockData, previousHash)
    hashValue = hash(completeData)
    while hashValue[:difficulty] != "0"*difficulty:
        nonce += 1
        completeData = blockToString(blockNumber, nonce, blockData, previousHash)
        hashValue = hash(completeData)
    print("Value of nonce : ",nonce)
    return hashValue



def userInput():
    # read in the blockNumber, blockData, and previousHash from the user
    blockNumber = int(input("Enter the block number: "))

    # accept the block transaction details
    blockData =[]
    print('Enter "X" to exit')
    blockTransactions = input("Enter the block data: ")
    while blockTransactions != "X":
        blockData.append(blockTransactions)
        blockTransactions = input("Enter the block data: ")

    # accept the previous hash
    previousHash = input("Enter the previous hash: ")
    
    blockData = concatList(blockData)
    nonce =0

    hashValue = findHash(blockNumber, nonce, blockData, previousHash)
    print(hashValue)


def main():
    blockNumber = 0
    blockData = ["A transfered 100 to B", "B transfered 50 to C", "C transfered 25 to D", "D transfered 10 to E"]
    
    previousHash = "0000"
    blockData = concatList(blockData)
    # print(blockData)

    startTime = time.time()
    hashValue = findHash(blockNumber, blockData, previousHash)
    endTime = time.time()
    print("Time taken : ", (endTime - startTime))
    print("Final Hash Value",hashValue)
    print("Block Data : ",blockData)

if __name__ == "__main__":
    main()
