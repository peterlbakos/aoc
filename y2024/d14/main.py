import math
import re
import sys
sign=lambda x:(x>0)-(x<0)
def stdev(a):
    avg=sum(a)/len(a)
    return math.sqrt(sum([(x-avg)**2 for x in a])/len(a))
inp=sys.stdin.read().strip()
R,C=103,101
grid=[['.' for j in range(C)] for i in range(R)]
robots=[list(map(int,re.findall(r'-?\d+',x))) for x in inp.split('\n')]
ans2=(sum([min([(stdev([(x[i]+x[i+2]*j)%[C,R][i] for x in robots]),j) for j in range([C,R][i])])[1]*[R,C][i] for i in range(2)])*51)%(R*C)
quad=[0]*9
for x in robots:
    quad[sign((x[0]+x[2]*100)%C-C//2)+sign((x[1]+x[3]*100)%R-R//2)*3]+=1
    grid[(x[1]+x[3]*ans2)%R][(x[0]+x[2]*ans2)%C]='#'
ans1=math.prod([quad[x] for x in [2,4,5,7]])
print('\n'.join([''.join(x) for x in grid]))
print(ans1,ans2)

