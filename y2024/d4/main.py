import sys
inp=sys.stdin.read().strip()
lines=inp.split('\n')
def check(x,y,dx,dy):
    s=''
    for i in range(4):
        if 0<=y+i*dy<len(lines) and 0<=x+i*dx<len(lines[0]):
            s+=lines[y+i*dy][x+i*dx]
    return s=='XMAS'
ans1=0
ans2=0
for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        for dx in range(-1,2):
            for dy in range(-1,2):
                ans1+=check(j,i,dx,dy)
        try:
            ans2+=((lines[i][j]=='M' and lines[i][j+2]=='S' and lines[i+1][j+1]=='A' and lines[i+2][j]=='M' and lines[i+2][j+2]=='S') or
                   (lines[i][j]=='M' and lines[i][j+2]=='M' and lines[i+1][j+1]=='A' and lines[i+2][j]=='S' and lines[i+2][j+2]=='S') or
                   (lines[i][j]=='S' and lines[i][j+2]=='S' and lines[i+1][j+1]=='A' and lines[i+2][j]=='M' and lines[i+2][j+2]=='M') or
                   (lines[i][j]=='S' and lines[i][j+2]=='M' and lines[i+1][j+1]=='A' and lines[i+2][j]=='S' and lines[i+2][j+2]=='M'))
        except:
            pass
print(ans1,ans2)

