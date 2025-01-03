import sys
inp=sys.stdin.read().strip()
reg=list(map(lambda x:int(x.split()[2]),inp.split('\n\n')[0].split('\n')))
inst=list(map(int,inp.split('\n\n')[1][9:].split(',')))
p=0
outp=[]
while p+1<len(inst):
    op=inst[p]
    lit=inst[p+1]
    assert(0<=lit<7)
    combo=lit if lit<4 else reg[lit-4]
    match op:
        case 0:
            reg[0]>>=combo
        case 1:
            reg[1]^=lit
        case 2:
            reg[1]=combo&7
        case 3:
            if reg[0]:
                p=lit-2
        case 4:
            reg[1]^=reg[2]
        case 5:
            outp.append(combo&7)
        case 6:
            reg[1]=reg[0]>>combo
        case 7:
            reg[2]=reg[0]>>combo
    p+=2
ans1=','.join(map(str,outp))
assert(inst==[2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0])
def solve(a,d):
    if d<0:
        return a
    a<<=3
    for i in range(8):
        if not ((inst[d]^i^((a|i)>>(i^3))^6)&7):
            res=solve(a|i,d-1)
            if res:
                return res
    return 0
ans2=solve(0,15)
print(ans1,ans2)

