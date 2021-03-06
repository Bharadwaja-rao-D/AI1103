from scipy.stats import bernoulli
no_expts = 100000
#*********part 1 ********
print("1")
coin1 = bernoulli.rvs(size = no_expts, p=0.5)
coin2 = bernoulli.rvs(size = no_expts, p=0.5)
no_F = 0 
no_EF = 0
for i in range (no_expts) :
  if coin1[i]==1 or coin2[i]==1: 
    no_F+=1
for i in range (no_expts) :
  if (coin1[i]==1 and coin2[i]==0) or (coin1[i]==0 and coin2[i]==1): 
    no_EF+=1
prob_F = no_F / no_expts
prob_EF = no_EF / no_expts
print("stimulated probability is : ",prob_EF / prob_F)
print("theoretical value of P(E/F) is : ",2/3)
#*********part 2 ********
print(2)
no_F = no_EF = 0
for i in range (no_expts) :
  if coin1[i]==0 and coin2[i]==0: 
    no_F+=1
for i in range (no_expts) :
  if (coin1[i]==1 and coin2[i]==1) and (coin1[i]==0 and coin2[i]==0): 
    no_EF+=1
prob_F = no_F / no_expts
prob_EF = no_EF / no_expts
print("stimulated probability is : ",prob_EF / prob_F)
print("theoretical value of P(E/F) is : ",0)
