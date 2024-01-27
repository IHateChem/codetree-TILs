import sys
input = sys.stdin.readline
N,M,P,C,D = map(int,input().split())

def Rmove(r, c, k):
    min_dis = [100000,0,0,0]
    for i in range(P):
        a,x,y = santas[i]
        if not a: continue
        t_dis = [dist(r,c,x,y),-x,-y,a]
        if a and t_dis < min_dis:
            min_dis = t_dis
    dr, dc = r+min_dis[1], c+min_dis[2]
    dr = -int(dr/abs(dr)) if dr else dr
    dc = -int(dc/abs(dc)) if dc else dc
    if dr: r += dr
    if dc: c += dc
    if r==-min_dis[1] and c == -min_dis[2]:
        a,x,y = min_dis[3], r,c
        conditions[a-1] = k+1
        scores[a-1] += C
        MAP[x][y] = 0
        x += C*dr
        y += C*dc
        if 1<=x<=N and 1<=y<=N:
            na = MAP[x][y]
            MAP[x][y] = a
            santas[a-1] = [a, x, y]
            while na:
                x += dr
                y += dc
                if 1<=x<=N and 1<=y<=N:
                    t = MAP[x][y]
                    MAP[x][y] = na
                    santas[na-1] = [na, x, y]
                    na = t
                else:
                    santas[na-1][0] = 0
                    na = 0
        else:
            santas[a-1][0] = 0
            MAP[x-C*dr][y-C*dc] = 0
    return r, c
def Smove(k, x, y):
    for a,r,c in santas:
        if not a or conditions[a-1] >= k: continue
        min_dis = dist(x,y,r,c)
        next_pos = (r,c)
        for dr,dc in ((-1,0), (0,1), (1,0), (0,-1)):
            nr, nc = r+dr, c+dc
            if not (1<=nr<=N and 1<=nc<=N) or MAP[nr][nc]: continue
            t_dis = dist(x,y,nr,nc)
            if min_dis > t_dis:
                min_dis = t_dis
                next_pos = (nr, nc)
        nr, nc = next_pos
        if(MAP[nr][nc]): continue
        MAP[r][c] = 0
        if(nr == x and nc == y):
            dr = nr - r
            dc = nc - c
            nr = nr - dr * D
            nc = nc - dc * D
            scores[a-1] += D
            conditions[a-1] = k+1
            if 1<=nr<=N and 1<=nc<=N:
                na = MAP[nr][nc]
                MAP[nr][nc] = a
                santas[a-1] = [a, nr, nc]
                while na:
                    nr -= dr
                    nc -= dc
                    if 1<=nr<=N and 1<=nc<=N:
                        t = MAP[nr][nc]
                        MAP[nr][nc] = na
                        santas[na-1] = [na, nr, nc]
                        na = t
                    else:
                        santas[na-1][0] = 0
                        na = 0
            else:
                santas[a-1][0] = 0

        else:   
            MAP[nr][nc] = a
            santas[a-1] = [a,nr,nc]
def crash():
    pass
def interaction():
    pass
dist = lambda x,y, r,c: (x-r)**2 + (y-c)**2
r,c = map(int,input().split())
santas = [list(map(int,input().split())) for _ in range(P)]
MAP = [[0]*(N+1) for _ in range(N+1)]
santas.sort()
for a,b,d in santas:
    MAP[b][d] = a
scores = [0]*P
conditions = [-1]*P
for i in range(M):
    r,c = Rmove(r, c, i)
    p = 0
    for a, _, __ in santas:
        if not a: p += 1
    if p == P: break
    Smove(i, r, c)
    p = 0
    for a, _, __ in santas:
        if not a: p += 1
    if p == P: break
    for a, _, __ in santas:
        if a: scores[a-1] += 1
print(*scores)