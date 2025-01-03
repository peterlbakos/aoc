import sys
from collections import deque
inp=sys.stdin.read().strip()
moves=list(inp.split('\n\n')[1].replace('\n',''))
grid1=list(map(list,inp.split('\n\n')[0].split('\n')))
grid2=[]
for x in grid1:
    grid2.append([])
    for y in x:
        match y:
            case '.':
                grid2[-1].append('.')
                grid2[-1].append('.')
            case '#':
                grid2[-1].append('#')
                grid2[-1].append('#')
            case 'O':
                grid2[-1].append('[')
                grid2[-1].append(']')
            case '@':
                grid2[-1].append('@')
                grid2[-1].append('.')
def solve(grid):
    R,C=len(grid),len(grid[0])
    rx,ry=0,0
    for i in range(R):
        for j in range(C):
            if grid[i][j]=='@':
                rx,ry=j,i
    m=[['.']*C for i in range(R)]
    for x in moves:
        d='>v<^'.find(x)
        dx,dy=1,0
        for i in range(d):
            dx,dy=-dy,dx
        st=deque()
        st.append((rx,ry))
        boxes=set()
        while len(st):
            bx,by=st.pop()
            if grid[by][bx] not in '@O[]' or (bx,by) in boxes:
                continue
            boxes.add((bx,by))
            if dx==1 or grid[by][bx]=='[':
                st.append((bx+1,by))
            if dx==-1 or grid[by][bx]==']':
                st.append((bx-1,by))
            if dy:
                st.append((bx,by+dy))
        ok=True
        for bx,by in boxes:
            if grid[by+dy][bx+dx]=='#':
                ok=False
                break
        if not ok:
            continue
        for bx,by in boxes:
            m[by][bx]=grid[by][bx]
            grid[by][bx]='.'
        for bx,by in boxes:
            grid[by+dy][bx+dx]=m[by][bx]
        rx+=dx
        ry+=dy
    res=0
    for i in range(R):
        for j in range(C):
            if grid[i][j] in 'O[':
                res+=100*i+j
    return res
ans1,ans2=solve(grid1),solve(grid2)
print(ans1,ans2)

