import numpy
from scipy.stats import bernoulli
import matplotlib.pyplot as plt 
no_expts = 100000
sent_signal = bernoulli.rvs(size = no_expts, p=0.5)
no_sent_1 = numpy.size(numpy.nonzero(sent_signal)) 
no_sent_0 = no_expts - no_sent_1
prob_sent_0 = no_sent_0 / no_expts #probability of the sender sending 0 as signal 
prob_sent_1 = no_sent_1 / no_expts #probability of the sender sending 1 as signal
#*******case 1 the sender has sent 000*********
n, p = 3, .1  # number of signal recieved , probability of recieved signal being 1
recieved = numpy.random.binomial(n, p, no_expts)
#print(s)
no_0, no_1, no_2 , no_3 = 0, 0, 0, 0
for i in range (no_expts):
  if recieved[i] == 0:
    no_0 = no_0 + 1
  elif recieved[i] == 1:
    no_1 = no_1 + 1
  elif recieved[i] == 2:
    no_2 = no_2 + 1
  elif recieved[i] == 3:
    no_3 = no_3 + 1
stimulated_prob_0_0 = no_0 / no_expts   #stimulated_prob_0_0 means stimulated probality when the sender has sent 0 and the number of 1's recieved are 0
stimulated_prob_0_1 = no_1 / no_expts
stimulated_prob_0_2 = no_2 / no_expts
stimulated_prob_0_3 = no_3 / no_expts
prob_1 = ( no_2 + no_3 ) / no_expts
prob_1 = ( no_2 + no_3 ) / no_expts
#*******case 2 the sender has sent 111*********
n, p = 3, .9  # number of signal recieved , probability of recieved signal being 1
recieved = numpy.random.binomial(n, p, no_expts)
no_0 , no_1, no_2, no_3 = 0, 0, 0, 0
for i in range (no_expts):
  if recieved[i] == 0:
    no_0 = no_0 + 1
  elif recieved[i] == 1:
    no_1 = no_1 + 1
  elif recieved[i] == 2:
    no_2 = no_2 + 1 
  elif recieved[i] == 3:
    no_3 = no_3 + 1
stimulated_prob_1_0 = no_0 / no_expts   #stimulated_prob_1_0 means stimulated probality when the sender has sent 1 and the number of 1's recieved are 0
stimulated_prob_1_1 = no_1 / no_expts
stimulated_prob_1_2 = no_2 / no_expts
stimulated_prob_1_3 = no_3 / no_expts
prob_2 = ( no_0 + no_1 ) / no_expts
prob_avg = prob_sent_0 * prob_1 + prob_sent_1 * prob_2
print("Stimulated average probability of error is :  ",prob_avg)
x = [0,1,2,3]
y = [stimulated_prob_0_0, stimulated_prob_0_1, stimulated_prob_0_2, stimulated_prob_0_3]
z = [0.729, 0.243, 0.027, 0.001]
plt.stem(x,y,label='stimulated') 
plt.scatter(x,z,color='r',label='calculated') 
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Stimulated vs Theoretical for Y=0')
plt.legend()
plt.show()
x = [0,1,2,3]
y = [stimulated_prob_1_0, stimulated_prob_1_1, stimulated_prob_1_2, stimulated_prob_1_3]
z = [0.001,0.027,0.243,0.729]
plt.stem(x,y,label='stimulated') 
plt.scatter(x,z,color='r',label='calculated') 
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Stimulated vs Theoretical for Y=1')
plt.legend()
plt.show()
