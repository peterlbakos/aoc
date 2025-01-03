from bisect import bisect_left
import sys
inp=sys.stdin.read().strip()
grid=[list(x) for x in inp.split('\n')]
R,C=len(grid),len(grid[0])
rr=[[] for x in range(R+1)]
rc=[[] for x in range(C+1)]
ir=[[] for x in range(R)]
ic=[[] for x in range(C)]
cntr=0
px,py=0,0
for i in range(R):
    for j in range(C):
        match grid[i][j]:
            case '^':
                px,py=j,i
            case '#':
                rr[i].append(j)
                rc[j].append(i)
                ir[i].append(cntr)
                ic[j].append(cntr)
                cntr+=1
def comp_wiring(x,y):
    return [(-1 if not len(rr[y+1]) or rr[y+1][-1]<=x else ir[y+1][bisect_left(rr[y+1],x+1)]*4+1),
            (-1 if not len(rc[x-1]) or rc[x-1][-1]<=y else ic[x-1][bisect_left(rc[x-1],y+1)]*4+2),
            (-1 if not len(rr[y-1]) or rr[y-1][0]>=x else ir[y-1][bisect_left(rr[y-1],x)-1]*4+3),
            (-1 if not len(rc[x+1]) or rc[x+1][0]>=y else ic[x+1][bisect_left(rc[x+1],y)-1]*4)]
digraph=[]
for i in range(R):
    for j in range(C):
        if grid[i][j]=='#':
            digraph+=comp_wiring(j,i)
vis=[[False]*C for i in range(R)]
dx,dy=0,-1
ans2=0
while True:
    vis[py][px]=True
    nx,ny=px+dx,py+dy
    if not (0<=nx<C and 0<=ny<R):
        break
    if grid[ny][nx]=='#':
        dx,dy=-dy,dx
    else:
        px,py=nx,ny
        if vis[ny][nx]:
            continue
        wiring=comp_wiring(nx,ny)
        v=wiring[[(0,-1),(1,0),(0,1),(-1,0)].index((dx,dy))]
        if v==1277:
            print(dx,dy)
        if v==-1:
            continue
        mods=[]
        if nx:
            t=bisect_left(rc[nx],ny+1)
            l,r=bisect_left(rc[nx-1],ny+1),len(rc[nx-1]) if t>=len(rc[nx]) else bisect_left(rc[nx-1],rc[nx][t])
            for i in range(l,r):
                t=ic[nx-1][i]*4+3
                mods.append((t,digraph[t],wiring[0]))
        if ny:
            t=bisect_left(rr[ny],nx)-1
            l,r=0 if t==-1 else bisect_left(rr[ny-1],rr[ny][t]+1),bisect_left(rr[ny-1],nx)
            for i in range(l,r):
                t=ir[ny-1][i]*4
                mods.append((t,digraph[t],wiring[1]))
        if nx<C-1:
            t=bisect_left(rc[nx],ny)-1
            l,r=0 if t==-1 else bisect_left(rc[nx+1],rc[nx][t]+1),bisect_left(rc[nx+1],ny)
            for i in range(l,r):
                t=ic[nx+1][i]*4+1
                mods.append((t,digraph[t],wiring[2]))
        if ny<R-1:
            t=bisect_left(rr[ny],nx+1)
            l,r=bisect_left(rr[ny+1],nx+1),len(rr[ny+1]) if t>=len(rr[ny]) else bisect_left(rr[ny+1],rr[ny][t])
            for i in range(l,r):
                t=ir[ny+1][i]*4+2
                mods.append((t,digraph[t],wiring[3]))
        for x in mods:
            digraph[x[0]]=x[2]
        vis2=[False]*R*C*4
        while v>-1 and not vis2[v]:
            vis2[v]=True
            v=digraph[v]
        ans2+=v>-1
        for x in mods:
            digraph[x[0]]=x[1]
ans1=sum([sum(x) for x in vis])
print(ans1,ans2)

