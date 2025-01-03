from copy import deepcopy
import sys
def check(a):
    inc=0
    dec=0
    ok=True
    for i in range(1,len(a)):
        inc+=a[i-1]<a[i]
        dec+=a[i-1]>a[i]
        if not (1<=abs(a[i-1]-a[i])<=3):
            ok=False
            break
    return ok and ((not inc) or (not dec))
def getcands(a):
    if len(a)==3:
        return [0,1,2]
    incs=[]
    decs=[]
    sames=[]
    for i in range(1,len(a)):
        if a[i-1]<a[i]:
            incs.append(i)
        elif a[i-1]>a[i]:
            decs.append(i)
        else:
            sames.append(i)
    if len(sames):
        if len(sames)>1:
            return []
        else:
            return [sames[0]-1,sames[0]]
    elif len(incs)==1:
        return [incs[0]-1,incs[0]]
    elif len(decs)==1:
        return [decs[0]-1,decs[0]]
    elif len(incs)>1 and len(decs)>1:
        return []
    for i in range(1,len(a)):
        if not (1<=abs(a[i-1]-a[i])<=3):
            return [i-1,i]
    assert(False)
inp=sys.stdin.read().strip()
ans1=0
ans2=0
for x in inp.split('\n'):
    a=list(map(int,x.split()))
    if len(a)<3 or check(a):
        ans1+=1
        ans2+=1
        continue
    cands=getcands(a)
    for x in cands:
        a2=deepcopy(a)
        del a2[x]
        if check(a2):
            ans2+=1
            break
print(ans1,ans2)

