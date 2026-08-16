import random
score=[0,0]
for ep in range(10):
 a=[random.choice([0,1]),random.choice([0,1])]; r=int(a[0]==a[1]); score[0]+=r;score[1]+=r;print(ep+1,a,r)
print('Shared rewards:',score)
