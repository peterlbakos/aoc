import math
import sys
inp=sys.stdin.read().strip()
def f(a,g,i,flag):
    if g<0:
        return False
    if i==1:
        return g==a[1]
    if flag:
        p=10**(math.floor(math.log(a[i],10))+1)
        if g%p==a[i] and f(a,g//p,i-1,True):
            return True
    if f(a,g-a[i],i-1,flag):
        return True
    return not g%a[i] and f(a,g/a[i],i-1,flag)
ans=[0,0]
for x in inp.split('\n'):
    a=list(map(int,x.replace(':','').split()))
    for i in range(2):
        ans[i]+=f(a,a[0],len(a)-1,i)*a[0]
print(ans[0],ans[1])

