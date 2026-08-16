import gymnasium as gym, numpy as np, tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
env=gym.make('CartPole-v1'); x=keras.Input((4,)); h=layers.Dense(32,activation='relu')(x); out=keras.Model(x,[layers.Dense(2,activation='softmax')(h),layers.Dense(1)(h)]); opt=keras.optimizers.Adam(.001)
for ep in range(10):
 s,_=env.reset(); S=[]; A=[]; R=[]; done=False
 while not done and len(R)<300:
  p,v=out(np.array([s])); a=np.random.choice(2,p=p.numpy()[0]); ns,r,t,tr,_=env.step(a); S.append(s);A.append(a);R.append(r);s=ns;done=t or tr
 G=[];g=0
 for r in R[::-1]:g=r+.99*g;G.insert(0,g)
 G=np.array(G,dtype=np.float32)
 with tf.GradientTape() as tape:
  p,v=out(np.array(S)); idx=tf.stack([tf.range(len(A)),A],1); lp=tf.math.log(tf.gather_nd(p,idx)+1e-8); adv=G-tf.squeeze(v,1); loss=-tf.reduce_mean(lp*tf.stop_gradient(adv))+tf.reduce_mean(adv**2)
 opt.apply_gradients(zip(tape.gradient(loss,out.trainable_variables),out.trainable_variables)); print(ep+1,sum(R))
env.close()
