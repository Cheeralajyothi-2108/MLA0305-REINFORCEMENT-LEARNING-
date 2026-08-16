import gymnasium as gym, numpy as np, tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
env=gym.make('CartPole-v1'); model=keras.Sequential([layers.Input((4,)),layers.Dense(32,activation='relu'),layers.Dense(2,activation='softmax')]); opt=keras.optimizers.Adam(.001)
for ep in range(10):
 s,_=env.reset(); S=[]; A=[]; R=[]; done=False
 while not done and len(R)<300:
  p=model(np.array([s]))[0].numpy(); a=np.random.choice(2,p=p); ns,r,t,tr,_=env.step(a); S.append(s); A.append(a); R.append(r); s=ns; done=t or tr
 G=[]; g=0
 for r in R[::-1]: g=r+.99*g; G.insert(0,g)
 G=np.array(G,dtype=np.float32); G=(G-G.mean())/(G.std()+1e-8)
 with tf.GradientTape() as tape:
  p=model(np.array(S)); idx=tf.stack([tf.range(len(A)),A],1); lp=tf.math.log(tf.gather_nd(p,idx)+1e-8); loss=-tf.reduce_mean(lp*G)
 opt.apply_gradients(zip(tape.gradient(loss,model.trainable_variables),model.trainable_variables)); print(ep+1,sum(R))
env.close()
