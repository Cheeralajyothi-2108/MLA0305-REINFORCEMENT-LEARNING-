import numpy as np
rng=np.random.default_rng(4); means={'A':5,'B':9,'C':7}; scores={a:rng.normal(m,2,200).mean() for a,m in means.items()}
print(scores); print('Best action:',max(scores,key=scores.get))
