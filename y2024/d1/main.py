from collections import defaultdict
import sys
inp=sys.stdin.read().strip()
a=[]
b=[]
for x in inp.split('\n'):
    t=list(map(int,x.split('   ')))
    a.append(t[0])
    b.append(t[1])
a.sort()
b.sort()
m=defaultdict(lambda:[0,0])
ans1=0
for i in range(len(a)):
    ans1+=abs(a[i]-b[i])
    m[a[i]][0]+=1
    m[b[i]][1]+=1
ans2=0
for x in m:
    ans2+=x*m[x][0]*m[x][1]
print(ans1,ans2)

