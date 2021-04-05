import numpy as np
import matplotlib.pyplot as plt

case_1, case_2, case_3, case_4, case_5, case_6, case_7,case_8,case_9,case_10 = 0,0,0,0,0,0,0,0,0,0
no_expts = 100000
for i in range (no_expts):
    setA = [2,3,4,5]
    setB = [11,12,13,14,15]
    x = np.random.choice(setA)
    y = np.random.choice(setB)
    if x+y < 13:
        case_1 = case_1 + 1
    elif x+y == 13:
        case_2 = case_2 + 1
    elif x+y == 14:
        case_3 = case_3 + 1
    elif x+y == 15:
        case_4 = case_4 + 1
    elif x+y == 16:
        case_5 = case_5 + 1
    elif x+y == 17:
        case_6 = case_6 + 1
    elif x+y == 18:
        case_7 = case_7 + 1
    elif x+y == 19:
        case_8 = case_8 + 1
    elif x+y == 20:
        case_9 = case_9 + 1
    elif x+y > 20:
        case_10 = case_10 + 1
prob = case_5/no_expts
print("Stimulated probability is : ",prob)
print("Calculated probability is : ",1/5)

x = [12,13,14,15,16,17,18,19,20,21]
stimulated_prob = [case_1 / no_expts, case_2 / no_expts, case_3 / no_expts, case_4 / no_expts, case_5 / no_expts, case_6 / no_expts, case_7 / no_expts, case_8 / no_expts, case_9 / no_expts, case_10 / no_expts]
calculated_prob = [0,1/20,1/10,3/20,1/5,1/5,3/20,2/20,1/20,0]
plt.stem(x,stimulated_prob,label='stimulated') 
plt.scatter(x,calculated_prob,color='r',label='calculated') 
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Stimulated vs Theoretical ')
plt.legend()
plt.show()
