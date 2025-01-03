import math
from collections import defaultdict
import sys
inp=sys.stdin.read().strip()
a=list(map(int,inp.split()))
dp=defaultdict(int)
for x in a:
    dp[x]+=1
ans1=0
for i in range(75):
    if i==25:
        ans1=sum(dp.values())
    ndp=defaultdict(int)
    ndp[1]=dp[0]
    for x in dp:
        if not x:
            continue
        lg=math.floor(math.log(x,10)+1)
        if lg&1:
            ndp[x*2024]+=dp[x]
        else:
            t=10**(lg//2)
            ndp[x//t]+=dp[x]
            ndp[x%t]+=dp[x]
    dp=ndp
ans2=sum(dp.values())
print(ans1,ans2)

