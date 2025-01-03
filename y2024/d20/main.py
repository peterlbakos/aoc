import math
import sys
from collections import deque
inp=sys.stdin.read().strip()
grid=list(map(list,inp.split('\n')))
R,C=len(grid),len(grid[0])
sx,sy=0,0
ex,ey=0,0
for i in range(R):
    for j in range(C):
        match grid[i][j]:
            case 'S':
                sx,sy=j,i
            case 'E':
                ex,ey=j,i
dist=[]
for (cx,cy) in [(sx,sy),(ex,ey)]:
    dist.append([[math.inf]*C for i in range(R)])
    q=deque()
    q.append((0,cx,cy))
    while len(q):
        d,x,y=q.popleft()
        if grid[y][x]=='#' or dist[-1][y][x]<=d:
            continue
        dist[-1][y][x]=d
        dx,dy=1,0
        for i in range(4):
            q.append((d+1,x+dx,y+dy))
            dx,dy=-dy,dx
track=[]
for i in range(R):
    for j in range(C):
        if grid[i][j]!='#':
            track.append((j,i))
def solve(mxd):
    res=0
    for (x1,y1) in track:
        for (x2,y2) in track:
            md=abs(x2-x1)+abs(y2-y1)
            res+=md<=mxd and dist[0][ey][ex]-dist[0][y1][x1]-md-dist[1][y2][x2]>=100
    return res
ans1,ans2=solve(2),solve(20)
print(ans1,ans2)

