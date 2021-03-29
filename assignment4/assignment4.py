import numpy as np

no_favour = 0
no_expts = 100000
for i in range (no_expts):
    setA = [2,3,4,5]
    setB = [11,12,13,14,15]
    x = np.random.choice(setA)
    y = np.random.choice(setB)
    if x+y==16 :
        no_favour= no_favour + 1

prob = no_favour/no_expts
print("Stimulated probability is : ",prob)
print("Calculated probability is : ",1/5)
