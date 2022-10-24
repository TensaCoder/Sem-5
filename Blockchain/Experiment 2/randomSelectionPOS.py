import random

numberOfNodes = int(input("Enter the number of nodes : "))
randomlySelectedNode = random.randint(1, numberOfNodes)

print("Node selected for publishing the block : Node", randomlySelectedNode)