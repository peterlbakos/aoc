import re
import sys
inp=sys.stdin.read().strip()
def solve(a):
    n1,d1=a[3]*a[4]-a[2]*a[5],a[0]*a[3]-a[1]*a[2]
    assert(d1)
    if n1%d1:
        return 0
    t=n1//d1
    n2,d2=a[4]-a[0]*t,a[2]
    assert(d2)
    if n2%d2:
        return 0
    return 3*t+n2//d2
ans=[0,0]
for x in inp.split('\n\n'):
    a=list(map(int,re.findall(r'\d+',x)))
    ans=[ans[i]+solve(a[:4]+[10000000000000*i+a[j] for j in range(4,6)]) for i in range(2)]
print(ans[0],ans[1])

