import numpy as np
import time

def bipolarSigmoid(x,steepness):
  expValue= steepness * x
  return (1 - np.exp(-expValue))/(1+ np.exp(-expValue))


def deltaLearning(x, w, d, alpha, steepness):
    tolerance = 0.1
    totalSquaredError = tolerance + 1
    epoch, numberOfTimesWeightsChanged = 0, 0
    oi=[0, 0, 0]
    squareError = [0, 0, 0]
    # print("For first epoch : ")
    while totalSquaredError > tolerance:
        for i in range(len(x)):
            net = np.multiply(w ,x[i])
            # print("Printing before sum() : ",net)
            net = sum(net)
            # print("Printing after sum() : ",net)
            o=bipolarSigmoid(net, steepness)
            oDerivative = 0.5*(1- o**2)
            intermediateValue = alpha * (d[i]-o) * oDerivative
            # print(intermediateValue)
            wDelta= [ intermediateValue * j for j in x[i]]
            w = np.add(wDelta, w)
            oi[i] = o
            squareError[i] = (d[i]-o)**2
            # if epoch == 0:
                # print("\nw: ",w)
                # print("oi: ",o)
                # print("Square Error: ",squareError[i])
            numberOfTimesWeightsChanged += 1
        totalSquaredError = sum(squareError)
        epoch+=1

    print("Number of epoch : ", epoch)
    print("Number of times weights changed : ", numberOfTimesWeightsChanged)


    print("Final Total Squared Error : ", totalSquaredError)
    return w, oi


x= [[1, -2, 0, -1], [0, 1.5, -0.5, -1], [-1, 1, 0.5, -1]]
w=[1, -1, 0, 0.5]
alpha = 0.1
steepness = 1
d=[-1, -1, 1]
# t1 = time.time()
# finalWeights, oiList = deltaLearning(x, w, d, alpha, steepness)
# t2 = time.time()
# print("\n\nFinal weights : ", finalWeights)
# print("Final output after training : ", oiList)
# print("Time taken : ", t2-t1)

def Q2(alpha):
    for i in range(10):
        print("Learning Rate : ", alpha)
        finalWeights, oiList = deltaLearning(x, w, d, alpha, steepness)
        alpha+=0.1
        print()


Q2(alpha)
