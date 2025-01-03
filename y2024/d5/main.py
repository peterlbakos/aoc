from functools import cmp_to_key
import sys
inp=sys.stdin.read().strip()
rules=set()
for x in inp.split('\n\n')[0].split('\n'):
    rules.add(tuple(map(int,x.split('|'))))
ans=[0,0]
for x in inp.split('\n\n')[1].split('\n'):
    A=list(map(int,x.split(',')))
    B=sorted(A,key=cmp_to_key(lambda a,b:-1 if (a,b) in rules else 1))
    ans[A!=B]+=B[len(A)//2]
print(ans[0],ans[1])

