import itertools
import sys
from collections import defaultdict
from functools import reduce
inp=sys.stdin.read().strip()
secrets=list(map(int,inp.split('\n')))
triggers=defaultdict(int)
ans1=0
for x in secrets:
    seq=[x]
    for i in range(2000):
        seq.append(reduce(lambda a,b:(a^int(a*2**b))&((1<<24)-1),[seq[-1],6,-5,11]))
    ans1+=seq[-1]
    prices=list(map(lambda y:y%10,seq))
    deltas=[c-p for p,c in itertools.pairwise(prices)]
    seen=set()
    for y,z in zip(zip(*[deltas[i:] for i in range(4)]),prices[4:]):
        triggers[y]+=z*(y not in seen)
        seen.add(y)
ans2=max(triggers.values())
print(ans1,ans2)

