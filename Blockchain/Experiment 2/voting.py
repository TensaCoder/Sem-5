# write a program to simulate proof of stake using voting method
import random

numberOfNodes = int(input("Enter number of publishing nodes present : "))
numberOfVotes = [0] * numberOfNodes
for i in range(numberOfNodes):
    randomlyVotedNode = random.randint(0, numberOfNodes-1)
    numberOfVotes[randomlyVotedNode] +=1

maximumVotes = max(numberOfVotes)
maximumVotedNode = numberOfVotes.index(maximumVotes)
print("Votes received by every node : ", numberOfVotes)
print("Votes received by winning Node : ", maximumVotes)
print("Node selected for publishing the block : Node", maximumVotedNode+1)