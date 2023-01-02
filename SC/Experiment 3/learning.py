def sgn (x):
    if x>=0:
        return 1
    else:
        return -1

def learning(w, x, d, alpha):
    iteration = 0
    oiList=[]
    while oiList != d :
        oiList=[]
        for i in range(len(x)):
            net = w[0]*x[i][0] + w[1]*x[i][1] + w[2]*x[i][2]
            oi= sgn(net)
            
            if d[i] != oi:
                r=d[i]-oi
                wDeltaVal = alpha * r
                wDelta =[
                    wDeltaVal*x[i][0],
                    wDeltaVal*x[i][1],
                    wDeltaVal*x[i][2]
                ]
                w = [
                    w[0] + wDelta[0],
                    w[1] + wDelta[1],
                    w[2] + wDelta[2]
                ]
                iteration+=1
                print("Changing value of weights : ", w)
            oiList.append(oi)
        
    print("\nNumber of iteration : ", iteration)
    return w, oiList

alpha = 0.6
w=[0, 1, 0]
# Input pattern [bias, x1, x2]
x=[[1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
d=[1, 1, 1, -1]

print("NAND Logic")
print("Alpha : ",alpha)
print("Starting weights : ", w)
wFinal, oiList = learning(w, x, d, alpha)
print("Weights : ", wFinal)

def checkingWeights(w, x0, x1, x2):
    finalOutput= w[0]*x0 + w[1]*x1 + w[2]*x2
    return sgn(finalOutput)

print()

print("Calculating Output for all Inputs using Final Weights")
# TO CHECK IF THE WEIGHTS ARE ACTUALLY CORRECT OR NOT
for subarr in x:
    x0=subarr[0]
    x1=subarr[1] 
    x2=subarr[2]
    finalOutput = checkingWeights(wFinal, x0, x1, x2)
    print("Output for {} and {} : {} ".format(x1, x2, finalOutput))
