import math
import sys
from collections import deque
sign=lambda x:(x>0)-(x<0)
inp=sys.stdin.read().strip()
order=list(map(lambda x:tuple(map(int,x.split(','))),inp.split('\n')))
R,C=71,71
corr=[[math.inf]*C for i in range(R)]
for i,(x,y) in enumerate(order):
    corr[y][x]=i
q=deque()
q.append((0,0,0))
vis=[[False]*C for i in range(R)]
ans1=0
while len(q):
    d,x,y=q.popleft()
    if not (0<=x<C and 0<=y<R) or corr[y][x]<1024 or vis[y][x]:
        continue
    vis[y][x]=True
    if (x,y)==(C-1,R-1):
        ans1=d
        break
    dx,dy=1,0
    for i in range(4):
        q.append((d+1,x+dx,y+dy))
        dx,dy=-dy,dx
class DSU:
    def __init__(self,n):
        self.p=list(range(n))
    def find(self,v):
        if self.p[v]!=v:
            self.p[v]=self.find(self.p[v])
        return self.p[v]
    def unite(self,u,v):
        u=self.find(u)
        v=self.find(v)
        if u!=v:
            self.p[u]=v
dsu=DSU((R+2)*(C+2))
dsu.unite(C,2*(C+2)-1)
dsu.unite(R*(C+2),(R+1)*(C+2)+1)
for i in range(1,R):
    dsu.unite((i+1)*(C+2),i*(C+2))
    dsu.unite((i+2)*(C+2)-1,(i+1)*(C+2)-1)
for i in range(1,C):
    dsu.unite(i+1,i)
    dsu.unite((R+1)*(C+2)+i+1,(R+1)*(C+2)+i)
ans2=''
for i,(x,y) in enumerate(order):
    v1,v2=1,0
    for j in range(8):
        nx,ny=x+sign(v1),y+sign(v2)
        if not (0<=nx<C and 0<=ny<R) or corr[ny][nx]<i:
            dsu.unite((y+1)*(C+2)+x+1,(ny+1)*(C+2)+nx+1)
        v1,v2=v1-v2,v1+v2
    if dsu.find(1)==dsu.find(C+2):
        ans2=f'{x},{y}'
        break
print(ans1,ans2)

