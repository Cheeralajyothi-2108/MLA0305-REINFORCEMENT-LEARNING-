import gymnasium as gym
for worker in range(4):
 env=gym.make('CartPole-v1'); scores=[]
 for ep in range(3):
  s,_=env.reset(seed=worker*10+ep); total=0; done=False
  while not done:
   s,r,t,tr,_=env.step(env.action_space.sample()); total+=r; done=t or tr
  scores.append(total)
 env.close(); print('Worker',worker,'scores',scores)
print('A3C concept: independent workers collect experience and asynchronously update shared parameters.')
