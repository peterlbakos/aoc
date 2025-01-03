import sys
inp=sys.stdin.read().strip()
do=True
ans1=0
ans2=0
for i in range(len(inp)):
    if inp[:i].endswith('do()'):
        do=True
    elif inp[:i].endswith("don't()"):
        do=False
    if inp[:i].endswith('mul('):
        try:
            a=list(map(int,inp[i:inp.index(')',i)].split(',')))
        except:
            continue
        ans1+=a[0]*a[1]
        ans2+=do*a[0]*a[1]
print(ans1,ans2)

