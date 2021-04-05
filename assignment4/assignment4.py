import numpy as np
import matplotlib.pyplot as plt

case_1, case_2, case_3, case_4, case_5, case_6, case_7,case_8,case_9,case_10 = 0,0,0,0,0,0,0,0,0,0
no_expts = 100000
setA = [2,3,4,5]
setB = [11,12,13,14,15]
for i in range (no_expts):
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

#*****plot of P(X) and P(Y)*****
f, (ax1,ax2) = plt.subplots(1,2)
no_2,no_3,no_4,no_5 = 0,0,0,0
for i in range (no_expts):
    x = np.random.choice(setA)
    if x == 2:
        no_2 = no_2 + 1
    elif x == 3:
        no_3 = no_3 + 1
    elif x == 4:
        no_4 = no_4 + 1
    elif x == 5:
        no_5 = no_5 + 1
no_11,no_12,no_13,no_14,no_15 = 0,0,0,0,0
for i in range (no_expts):
    x = np.random.choice(setB)
    if x == 11:
        no_11 = no_11 + 1
    elif x == 12:
        no_12 = no_12 + 1
    elif x == 13:
        no_13 = no_13 + 1
    elif x == 14:
        no_14 = no_14 + 1
    elif x == 15:
        no_15 = no_15 + 1
x_1 = [2,3,4,5]
x_2 = [11,12,13,14,15]
stimulated_A = [no_2/no_expts, no_3/no_expts, no_4/no_expts,no_5/no_expts]
stimulated_B = [no_11/no_expts, no_12/no_expts, no_13/no_expts, no_14/no_expts,no_15/no_expts]
ax1.stem(x_1,stimulated_A)
ax1.set(xlabel='x', ylabel='P(X=x)')
ax2.stem(x_2,stimulated_B)
ax2.set(xlabel='y', ylabel='P(Y=y)')
plt.legend()
plt.show()

#******plot of P(Z)*****
x = [12,13,14,15,16,17,18,19,20,21]
stimulated_prob = [case_1 / no_expts, case_2 / no_expts, case_3 / no_expts, case_4 / no_expts, case_5 / no_expts, case_6 / no_expts, case_7 / no_expts, case_8 / no_expts, case_9 / no_expts, case_10 / no_expts]
calculated_prob = [0,1/20,1/10,3/20,1/5,1/5,3/20,2/20,1/20,0]
plt.stem(x,stimulated_prob,label='stimulated') 
plt.scatter(x,calculated_prob,color='r',label='calculated') 
plt.xlabel('n')
plt.ylabel('P(Z=n)')
plt.title('Stimulated vs Theoretical ')
plt.legend()
plt.show()
