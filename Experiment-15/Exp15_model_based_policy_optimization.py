import numpy as np
policy=np.array([.5,.5]); predicted=np.array([4.,8.])
for i in range(10):
 z=predicted-predicted.max(); p=np.exp(z); p/=p.sum(); policy=.7*policy+.3*p; print(i+1,np.round(policy,3))
