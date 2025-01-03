import math
import sys
from heapq import heappush, heappop
from collections import deque
inp=sys.stdin.read().strip()
grid=[list(x) for x in inp.split('\n')]
R,C=len(grid),len(grid[0])
ex,ey=0,0
q=[]
for i in range(R):
    for j in range(C):
        if grid[i][j] in '.#':
            continue
        if grid[i][j]=='S':
            q.append((0,j,i,0))
        else:
            ex,ey=j,i
        grid[i][j]='.'
dist=[[[math.inf]*4 for j in range(C)] for i in range(R)]
while len(q):
    s,x,y,d=heappop(q)
    if grid[y][x]=='#':
        continue
    dx,dy=1,0
    for i in range(d):
        dx,dy=-dy,dx
    if dist[y][x][d]<=s:
        continue
    dist[y][x][d]=s
    heappush(q,(s+1,x+dx,y+dy,d))
    heappush(q,(s+1000,x,y,(d+1)%4))
    heappush(q,(s+1000,x,y,(d-1)%4))
ans1=min(dist[ey][ex])
st=deque()
for i in range(4):
    if dist[ey][ex][i]==ans1:
        st.append((ans1,ex,ey,i))
vis=[[[False]*4 for j in range(C)] for i in range(R)]
while len(st):
    s,x,y,d=st.pop()
    if s!=dist[y][x][d] or vis[y][x][d]:
        continue
    vis[y][x][d]=True
    dx,dy=1,0
    for i in range(d):
        dx,dy=-dy,dx
    st.append((s-1,x-dx,y-dy,d))
    st.append((s-1000,x,y,(d+1)%4))
    st.append((s-1000,x,y,(d-1)%4))
ans2=sum([sum([any(y) for y in x]) for x in vis])
print(ans1,ans2)

