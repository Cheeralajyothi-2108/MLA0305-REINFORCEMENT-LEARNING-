import numpy as np
old=np.array([.4,.3,.5,.25]); new=np.array([.44,.24,.7,.2]); adv=np.array([1,1,-1,-1]); eps=.2
ratio=new/old; clip=np.clip(ratio,1-eps,1+eps); obj=np.minimum(ratio*adv,clip*adv)
print('Ratio:',ratio); print('Clipped:',clip); print('PPO objective:',obj); print('Mean:',obj.mean())
