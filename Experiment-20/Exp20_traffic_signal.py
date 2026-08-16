import random
Q={(s,a):0. for s in ['Low','High'] for a in ['Short','Long']}; alpha=.1;gamma=.9
for _ in range(300):
 s=random.choice(['Low','High'])
 for _ in range(20):
  a=random.choice(['Short','Long']) if random.random()<.2 else max(['Short','Long'],key=lambda x:Q[(s,x)])
  r=5 if s=='High' and a=='Long' else (-3 if s=='High' else (3 if a=='Short' else 1)); ns=random.choice(['Low','High']); Q[(s,a)]+=alpha*(r+gamma*max(Q[(ns,x)] for x in ['Short','Long'])-Q[(s,a)]); s=ns
for s in ['Low','High']: print(s,max(['Short','Long'],key=lambda a:Q[(s,a)]),Q[(s,'Short')],Q[(s,'Long')])
