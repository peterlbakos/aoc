import itertools
import sys
inp=sys.stdin.read().strip()
pins=[[],[]]
for x in inp.split('\n\n'):
    schematics=x.split('\n')
    pins[schematics[0][0]=='#'].append([sum([schematics[j][i]=='#' for j in range(7)]) for i in range(5)])
ans=sum([all([x[i]+y[i]<=7 for i in range(5)]) for x,y in itertools.product(pins[0],pins[1])])
print(ans)

