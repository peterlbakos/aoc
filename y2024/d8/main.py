import sys
inp=sys.stdin.read().strip()
grid=[list(x) for x in inp.split('\n')]
R,C=len(grid),len(grid[0])
anti1=[[False]*C for i in range(R)]
anti2=[[False]*C for i in range(R)]
ans1,ans2=0,0
for i in range((R*C)**3):
    t=i
    a=[]
    for j in range(3):
        a+=[t%C,(t//C)%R]
        t//=R*C
    if grid[a[3]][a[2]]=='.' or grid[a[3]][a[2]]!=grid[a[5]][a[4]] or (a[2],a[3])==(a[4],a[5]):
        continue
    dx,dy,dx2,dy2=a[0]-a[2],a[1]-a[3],a[0]-a[4],a[1]-a[5]
    if (dx*2==dx2 and dy*2==dy2) or (dx==dx2*2 and dy==dy2*2):
        ans1+=not anti1[a[1]][a[0]]
        anti1[a[1]][a[0]]=True
    if dx*dy2==dy*dx2:
        ans2+=not anti2[a[1]][a[0]]
        anti2[a[1]][a[0]]=True
print(ans1,ans2)

