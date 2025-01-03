import sys
inp=sys.stdin.read().strip()
towels=set(inp.split('\n\n')[0].split(', '))
designs=inp.split('\n\n')[1].split('\n')
dp=dict()
def solve(d):
    if not len(d):
        return 1
    if d not in dp:
        dp[d]=0
        for x in towels:
            if d.endswith(x):
                dp[d]+=solve(d[:len(d)-len(x)])
    return dp[d]
ans1,ans2=len(designs),0
for x in designs:
    ans1-=not solve(x)
    ans2+=solve(x)
print(ans1,ans2)

