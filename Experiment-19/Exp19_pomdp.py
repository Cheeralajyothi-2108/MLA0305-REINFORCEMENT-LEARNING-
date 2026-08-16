belief={'Good':.5,'Bad':.5}; like={'Good':{'Safe':.9,'Danger':.1},'Bad':{'Safe':.2,'Danger':.8}}; obs='Danger'
post={s:belief[s]*like[s][obs] for s in belief}; z=sum(post.values()); post={s:v/z for s,v in post.items()}
print('Prior:',belief);print('Observation:',obs);print('Posterior:',post)
