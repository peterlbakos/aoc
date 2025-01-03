import math
from copy import deepcopy
import sys
inp=sys.stdin.read().strip()
digs=[ord(x)-ord('0') for x in inp]
s=0
a=[[],[]]
for i in range(len(digs)):
    a[i&1].append([s,s+digs[i]-1])
    s+=digs[i]
b=deepcopy(a)
ans1=0
while a[1][0][0]<a[0][-1][0]:
    if a[1][0][1]-a[1][0][0]<a[0][-1][1]-a[0][-1][0]:
        ans1+=(len(a[0])-1)*(a[1][0][0]+a[1][0][1])*(a[1][0][1]-a[1][0][0]+1)//2
        a[0][-1][1]-=a[1][0][1]-a[1][0][0]+1
        a[1].pop(0)
    else:
        ans1+=(len(a[0])-1)*(2*a[1][0][0]+a[0][-1][1]-a[0][-1][0])*(a[0][-1][1]-a[0][-1][0]+1)//2
        a[1][0][0]+=a[0][-1][1]-a[0][-1][0]+1
        a[0].pop()
while len(a[0]):
    ans1+=(len(a[0])-1)*(a[0][-1][0]+a[0][-1][1])*(a[0][-1][1]-a[0][-1][0]+1)//2
    a[0].pop()
class SegTree:
    def __init__(self,l,r):
        self.l=l
        self.r=r
        self.cache=0
        if l!=r:
            mid=(l+r)//2
            self.kids=(SegTree(l,mid),SegTree(mid+1,r))
    def point_update(self,target,delta):
        if self.r<target or target<self.l:
            return
        if self.l==self.r:
            self.cache+=delta
        else:
            self.kids[0].point_update(target,delta)
            self.kids[1].point_update(target,delta)
            self.cache=max(self.kids[0].cache,self.kids[1].cache)
    def range_query(self,l,r):
        if r<l or r<self.l or self.r<l:
            return -math.inf
        if l<=self.l and self.r<=r:
            return self.cache
        else:
            return max(self.kids[0].range_query(l,r),self.kids[1].range_query(l,r))
seg=SegTree(0,len(b[1])-1)
for i in range(len(b[1])):
    seg.point_update(i,b[1][i][1]-b[1][i][0]+1)
ans2=0
for i in range(len(b[0])-1,-1,-1):
    ans2+=i*(b[0][i][0]+b[0][i][1])*(b[0][i][1]-b[0][i][0]+1)//2
    lo=-1
    hi=len(b[1])
    while lo+1<hi:
        mid=(lo+hi)//2
        if b[0][i][1]-b[0][i][0]+1<=seg.range_query(0,mid-1):
            hi=mid
        else:
            lo=mid
    if lo==-1 or b[0][i][0]<b[1][lo][0]:
        continue
    ans2-=i*(b[0][i][1]-b[0][i][0]+1)*(b[0][i][0]-b[1][lo][0])
    b[1][lo][0]+=b[0][i][1]-b[0][i][0]+1
    seg.point_update(lo,b[0][i][0]-b[0][i][1]-1)
print(ans1,ans2)

