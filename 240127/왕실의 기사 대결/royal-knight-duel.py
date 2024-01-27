import sys
input = sys.stdin.readline
L,N,Q = map(int,input().split())
MAP = [[2]*(L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2]*(L+2)]
L += 2
knightMAP = [[MAP[j][i] - 3 for i in range(L)] for j in range(L)]
knights = [list(map(int,input().split())) for _ in range(N)]
firstHp = [k[-1] for k in knights]
dir = [(-1,0),(0,1),(1,0),(0,-1)]

def mkKnightMap():
    for i in range(L):
        for j in range(L):
            if knightMAP[i][j] == -1: pass
            else: knightMAP[i][j] = -3
    for i in range(N):
        r,c,h,w,k = knights[i]
        if k <= 0: continue
        for j in range(w):
            for k in range(h):
                knightMAP[r+k][c+j] = i
def move(i, d):
    r,c,h,w,k = knights[i]
    if k <= 0: return
    stack = [(r+b, c+j) for b in range(h) for j in range(w)]
    dr, dc = dir[d]
    moved = set()
    t = []
    while stack:
        x, y = stack.pop()
        v = knightMAP[x+dr][y+dc]
        if v == -1: return
        if v >= 0 and not v in moved and i != v:
            moved.add(v)
            for m in range(knights[v][2]):
                for j in range(knights[v][3]):
                    t.append((knights[v][0]+m,knights[v][1]+j))
        if not stack:
            stack = t
            t = []
    knights[i] = [r+dr,c+dc,h,w,k]
    for m in moved:
        if m == i: continue
        r,c,h,w,k = knights[m]
        for j in range(w):
            for o in range(h):
                if MAP[r+dr+o][c+dc+j] == 1:
                    k -= 1
        knights[m] = [r+dr,c+dc,h,w,k]
    mkKnightMap()
mkKnightMap()
#왕의 명령
for _ in range(Q):
    i,d = map(int,input().split())
    move(i-1,d)
answer=  0
for i in range(N):
    if knights[i][-1] <= 0: continue
    answer += firstHp[i] - knights[i][-1]
print(answer)