model={(0,0):(0,-1),(0,1):(1,0),(1,0):(0,-1),(1,1):(2,0),(2,0):(1,-1),(2,1):(3,10)}
s=0
for _ in range(3):
 a=max([0,1],key=lambda x:model[(s,x)][1]); s,r=model[(s,a)]; print('Action',a,'Reward',r,'State',s)
