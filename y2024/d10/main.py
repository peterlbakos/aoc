import sys
inp=sys.stdin.read().strip()
grid=[list(x) for x in inp.split('\n')]
R,C=len(grid),len(grid[0])
reach=set()
ans2=0
def dfs(x,y):
    global ans2
    if grid[y][x]=='9':
        ans2+=1
        reach.add((x,y))
        return
    dx,dy=1,0
    for i in range(4):
        nx,ny=x+dx,y+dy
        if 0<=nx<C and 0<=ny<R and ord(grid[ny][nx])==ord(grid[y][x])+1:
            dfs(nx,ny)
        dx,dy=dy,-dx
ans1=0
for i in range(R):
    for j in range(C):
        if grid[i][j]=='0':
            reach.clear()
            dfs(j,i)
            ans1+=len(reach)
print(ans1,ans2)

