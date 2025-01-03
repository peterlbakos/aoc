import itertools
import sys
from collections import defaultdict
inp=sys.stdin.read().strip()
AL=defaultdict(set)
for x in inp.split('\n'):
    u,v=x.split('-')
    AL[u].add(v)
    AL[v].add(u)
ans1=sum([u in AL[v] and u in AL[w] and v in AL[w] and any(map(lambda x:x[0]=='t',[u,v,w])) for u,v,w in itertools.product(AL,repeat=3)])//6
best=[]
for u in AL:
    for i in range(1<<len(AL[u])):
        if i.bit_count()<len(best):
            continue
        subs=set(map(lambda x:x[1],filter(lambda x:(i>>x[0])&1,enumerate(AL[u]))))
        if all([v==w or v in AL[w] for v,w in itertools.product(subs,repeat=2)]):
            best=list(subs)+[u]
ans2=','.join(sorted(best))
print(ans1,ans2)

