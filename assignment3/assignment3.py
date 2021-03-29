from scipy.stats import bernoulli
import matplotlib.pyplot as plt

no_expts = 10000
no_favour_1 = 0
no_favour_2 = 0
outcomes_1 = bernoulli.rvs(size = no_expts, p = 10/25)
outcomes_2_0 = bernoulli.rvs(size = no_expts, p=10/24)
outcomes_2_1 = bernoulli.rvs(size = no_expts, p = 9/24)
for i in range (no_expts):
    if outcomes_1[i] == 0 and outcomes_2_0[i]==1: 
        no_favour_1= no_favour_1 + 1
    elif outcomes_1[i] ==1 and outcomes_2_1[i]==0:
        no_favour_2 = no_favour_2 + 1
prob = (no_favour_1 + no_favour_2) / no_expts
print("stimulated value is : ",prob)
print("calculated value is : ",1/2)
