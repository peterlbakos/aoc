import sys
inp=sys.stdin.read().strip()
lines=inp.split('\n')
R,C=len(lines)*3,len(lines[0])*3
grid=[[lines[i//3][j//3] for j in range(C)] for i in range(R)]
vis=[[False]*C for i in range(R)]
ans1,ans2=0,0
for i in range(R):
    for j in range(C):
        if vis[i][j]:
            continue
        region=set()
        st=[(j,i)]
        while len(st):
            x,y=st.pop()
            if not (0<=x<C and 0<=y<R) or grid[y][x]!=grid[i][j] or (x,y) in region:
                continue
            region.add((x,y))
            vis[y][x]=True
            dx,dy=1,0
            for k in range(4):
                st.append((x+dx,y+dy))
                dx,dy=dy,-dx
        t=0
        borders=set()
        for x,y in region:
            v1,v2=1,1
            for k in range(8):
                nx,ny=x+(v1>0)-(v1<0),y+(v2>0)-(v2<0)
                if (nx,ny) not in region:
                    t+=k&1
                    borders.add((nx,ny))
                v1,v2=v1-v2,v1+v2
        ans1+=t*len(region)//27
        corners=0
        for x,y in borders:
            dx,dy=1,1
            ok=False
            for k in range(4):
                ok|=(x+dx,y) in borders and (x,y+dy) in borders
                dx,dy=dy,-dx
            corners+=ok
        ans2+=corners*len(region)//9
print(ans1,ans2)

