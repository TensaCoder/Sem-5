import hashlib
from datetime import datetime
from ecdsa import SigningKey

# # generate private key
# sk = SigningKey.generate() # uses NIST192p
# # generate public key
# vk = sk.verifying_key
# print("Private key: ", sk.to_string().hex())
# print("Public key: ", vk.to_string().hex())

# signature = sk.sign(b"message")
# print("Signature : ", type(signature))
# print("Signature : ", signature)
# print( vk.verify(signature, b"message"))

def createPublicPrivateKeys(numOfUsers):
    keyPairs=[]
    for i in range(numOfUsers):
        sk = SigningKey.generate() # uses NIST192p
        # generate public key
        vk = sk.verifying_key
        # the keys are stored in the form of object, so when we need the string we need to convert it using ".to_string().hex()"
        keyPairs.append([sk, vk])
    return keyPairs

def listOfTransactionToString(listOfTransaction):
    # convert the list of transaction into a string
    string = ""
    for i in range(len(listOfTransaction)):
        string += str(listOfTransaction[i])
    return string

def findHash(blockNumber, blockData, previousHash):
    nonce = int(0)
    hashValue = ""
    while hashValue[:4] != "0000":
        nonce += 1
        hashValue = hashlib.sha256(str(blockNumber).encode() + str(nonce).encode() + str(blockData).encode() + str(previousHash).encode()).hexdigest()

    return hashValue, nonce


def createBlock(previousBlockNumber, previousHash, blockData, transactionFee):

    block =[]
    blockNumber = previousBlockNumber + 1
    hashValue, nonce = findHash(blockNumber, blockData, previousHash)
    timeStamp = datetime.now()

    # subtract the transaction fees from the sender
    transactionAmount = transactionFee * blockData[0]
    blockData[0] -= transactionAmount

    # adding all details into the block
    block.append(blockNumber)
    block.append(nonce)
    block.append(timeStamp)
    block.append(blockData)
    block.append(transactionAmount)
    block.append(previousHash)
    block.append(hashValue)

    # when the block is returned the blockData field will need to be updated to list of lists of transactions
    return block

def addBlock(blockChain, blockData, keyPairs, transactionFee):

    # verify the signature of the transaction
    # blockData -> TransactionLedger
    if individualTransactionVerification(blockData, keyPairs, blockData[1]) != True:
        print("Transaction not verified!!!")
        return False, blockChain

    # if the blockChain is empty then the previousBlockNumber and previousHash will be 0
    if len(blockChain) == 0:
        block = createBlock(-1, "0000", blockData, transactionFee)
        blockChain.append(block)
        print("New Block added to the chain!!! : Block Number : ", block[0])
        return True, blockChain

    # if the blockChain is not empty then the previousBlockNumber and previousHash will be the last block in the blockChain
    lastIndexOfBlockChain = len(blockChain) - 1
    previousBlockNumber = blockChain[lastIndexOfBlockChain][0]
    previousHash = blockChain[lastIndexOfBlockChain][6]

    block = createBlock(previousBlockNumber, previousHash, blockData, transactionFee)
    blockChain.append(block)

    print("New Block added to the chain!!! : Block Number : ", block[0])
    return True, blockChain

# Signs the transaction using the private key of the sender
def signTransaction(TransactionLedger, keyPairs):

    # add sender signature of the transaction to the TransactionLedger
    for i in range(len(TransactionLedger)):

        # find the index of the sender in the keyPairs
        j=0
        if TransactionLedger[i][1] == "A":
            j=0
        elif TransactionLedger[i][1] == "B":
            j=1
        elif TransactionLedger[i][1] == "C":
            j=2
        else:
            print("Error in finding the sender in the keyPairs")

        senderSignature = keyPairs[j][0].sign(listOfTransactionToString(TransactionLedger[i]).encode())
        # print("Sender Signature : ", senderSignature.hex())

        # # this store the signature in the form of string
        # TransactionLedger[0].append(senderSignature.hex())
    
        # this stores the password in the form of hex code
        TransactionLedger[i].append(senderSignature) 

        # value stored : b'\xa0\xc4\xb9n\x1d\x10K(\xaaf\xdb\xb0\x1b\xe7\xc5,\xae\xa6\x91\x11\x8d\x9fkl9\xbb\xb6;}\xd6\xfe*\xbf\x01[\xbcU \xe3\xedP\x8c\xd3\xc4\xc8A\xce\xfb'

        # use this type of value to verify the signature
        # to display the signature in the form of string use : senderSignature.hex()

    return TransactionLedger

def verifyTransaction(TransactionLedger, keyPairs):
    # verify the signature of the transaction using the public key of the sender
    for i in range(len(TransactionLedger)):
        # find the index of the sender in the keyPairs
        j=0
        if TransactionLedger[i][1] == "A":
            j=0
        elif TransactionLedger[i][1] == "B":
            j=1
        elif TransactionLedger[i][1] == "C":
            j=2
        else:
            print("Error in finding the sender in the keyPairs")

        # # verify the signature of the transaction

        # print("\nTransaction : ", TransactionLedger[i])
        # print("\nSignature : ", TransactionLedger[i][3])

        # print("\nVerification : ", keyPairs[j][1].verify(TransactionLedger[i][3], listOfTransactionToString(TransactionLedger[i][:3]).encode()))
        # print("\nList of Transaction : ", listOfTransactionToString(TransactionLedger[i][:3]))

        if keyPairs[j][1].verify(TransactionLedger[i][3], listOfTransactionToString(TransactionLedger[i][:3]).encode()):
            print(f"Transaction {TransactionLedger[i][:3]} verified!!!")
        else:
            print("Transaction not verified!!!")


def individualTransactionVerification(TransactionLedger, keyPairs, sender):
    # verify the signature of individual transaction and return true or false
    # find the index of the sender in the keypairs
    j=0
    if sender == "A":
        j=0
    elif sender == "B":
        j=1
    elif sender == "C":
        j=2
    else:
        print("Error in finding the sender in the keyPairs")
    
    # verify the signature of the transaction
    if keyPairs[j][1].verify(TransactionLedger[3], listOfTransactionToString(TransactionLedger[:3]).encode()):
        return True
    else:
        return False


def printBlockChain(blockChain):
    print("\n\nBlock Chain : ")
    for i in range(len(blockChain)):
        print("\nBlock Number : ", blockChain[i][0])
        print("Nonce : ", blockChain[i][1])
        print("Time Stamp : ", blockChain[i][2])
        print("Transaction Details : ", blockChain[i][3])
        print("Transaction Fee : ", blockChain[i][4])
        print("Previous Hash : ", blockChain[i][5])
        print("Hash Value : ", blockChain[i][6])

# Block Structure of blockchain
# block = [ Block number, time stamp, nonce, transaction_Details, sender public key, PreviousHash, hash value ]

# other values : UTXO ledger, Mining fees for the miner, transaction fee for sender


# give user option to enter the following options
# 1. transaction history
# 2. UTXO
# 3. Display the blockchain
# 4. Transaction fees
# 5. Add a new block

def main():
    keyPairs = []
    blockChain = []
    TransactionLedger = ["$1000 A -> B", "$78 B -> C" , "$50 C -> A", "$20 B -> A"]
    # TransactionLedger = [[Amount, Sender, Receiver, senderSignature]]
    TransactionLedger = [[1000, "A", "B"], [78, "B", "C"], [50, "C", "A"], [20, "B", "A"]]
    UTXO = TransactionLedger[:]

    transactionFee = 0.01
    miningFee = 0.01

    keyPairs = createPublicPrivateKeys(3)

    TransactionLedger = signTransaction(TransactionLedger, keyPairs)
    
    # verifying the transaction
    verifyTransaction(TransactionLedger, keyPairs)
    
    # adding block to the blockchain
    for i in range(len(TransactionLedger)):
        status, blockChain = addBlock(blockChain, TransactionLedger[i], keyPairs, transactionFee)
        if status == False:
            print("\nBlock not added to the blockchain!!!")
    
    # take input from the user to select the option
    while True:
        print("\n\nSelect the option : ")
        print("1. Transaction History")
        print("2. UTXO")
        print("3. Display the blockchain")
        print("4. Transaction fees")
        print("-1. Exit")

        option = int(input())

        if option == 1:
            print("\nTransaction History : ")
            for i in range(len(TransactionLedger)):
                print(f"\nTransaction {i+1} : {TransactionLedger[i]}")
        elif option == 2:
            print("\nUTXO : ")
            for i in range(len(TransactionLedger)):
                print(f"{TransactionLedger[i][0]}ETH : {TransactionLedger[i][1]} -> {TransactionLedger[i][2]}")
        elif option == 3:
            printBlockChain(blockChain)
        elif option == 4:
            print(f"\nTransaction fees : {transactionFee} * transaction amount")
            print(f"Mining fees : {miningFee} * transaction amount")
        elif option == -1:
            break
        else:
            print("\nInvalid option!!!")

    
if __name__ == "__main__":
    main()