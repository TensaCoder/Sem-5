import numpy as np
# w = [1, -1, 1]
# x=[[1, -2, 1], [2, 3, 1], [1, -1, 1]]
# print(np.dot(x[0], w))

def bipolarSigmoid(x,steepness):
    expValue= steepness * x
    return (1 - np.exp(-expValue))/(1+ np.exp(-expValue))

def sgn(x):
    if x>=0: 
        return 1
    else: 
        return -1

# needs w, x, alpha
def hebbianBipolarLearning(w, x, alpha):
    epoch =0
    # iteration over all input 3 times
    while (epoch <3):
        for i in range(len(x)):
            # for j in range (len(x[0])):
            #     net = w[j] * x[i][j]
            net = np.dot(w, x[i])
            oiBipolar = sgn(net)

            #modifying the weights
            wDeltaVal = alpha * oiBipolar
            # wDelta =[
            #     wDeltaVal*x[i][0],
            #     wDeltaVal*x[i][1],
            #     wDeltaVal*x[i][2],
            #     wDeltaVal*x[i][3]
            # ]
            wDelta = np.multiply(wDeltaVal, x[i])
            # w = [
            #     w[0] + wDelta[0],
            #     w[1] + wDelta[1],
            #     w[2] + wDelta[2],
            #     w[3] + wDelta[3]
            # ]
            w = np.add(w, wDelta)
            print("Changing Value of Weights : ", w)

        epoch+=1
    
    return w

# needs w, x, steepness, 
def hebbianSigmoidLearning(w, x, alpha, steepness):
    epoch =0
    # iteration over all input 3 times
    while (epoch <3):
        for i in range(len(x)):
            # for j in range (len(x[0])):
            #     net = w[j] * x[i][j]
            net = np.dot(w, x[i])
            # print("Net: ", net)
            oiSigmoid = bipolarSigmoid(net, steepness)
            print("f(net)", oiSigmoid)

            #modifying the weights
            wDeltaVal = alpha * oiSigmoid
            # wDelta =[
            #     wDeltaVal*x[i][0],
            #     wDeltaVal*x[i][1],
            #     wDeltaVal*x[i][2],
            #     wDeltaVal*x[i][3]
            # ]
            wDelta = np.multiply(wDeltaVal, x[i])
            # w = [
            #     w[0] + wDelta[0],
            #     w[1] + wDelta[1],
            #     w[2] + wDelta[2],
            #     w[3] + wDelta[3]
            # ]
            w = np.add(w, wDelta)
            print("Changing Value of Weights : ", w)

        epoch+=1
    
    return w


w = [1, -1, 0, 0.5]
x=[[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]]
steepness = 1
alpha = 1

# w = [1, -1, 1]
# x=[[1, -2, 1], [2, 3, 1], [1, -1, 1]]
# steepness = 1
# alpha = 1


print("For Biploar Activation Hebbian Learning:")
finalWeights = hebbianBipolarLearning(w,x,alpha)
print("\nThe final weights for Bipolar Hebbain Learning : ", finalWeights)


print("\n\nFor Biploar Sigmoid Activation Hebbian Learning:")
finalSigmoidWeights = hebbianSigmoidLearning(w, x, alpha, steepness)
print("\nThe final weights for Bipolar Hebbain Learning : ", finalSigmoidWeights)
