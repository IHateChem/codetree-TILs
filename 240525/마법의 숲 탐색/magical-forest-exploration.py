import sys
input = sys.stdin.readline
directions = [(-1,0), (0,1), (1,0), (0,-1)]
R,C,K = map(int,input().split())
MAP = [[0]*C for _ in range(R+2)]
def clear():
    for i in range(R+2):
        for j in range(C):
            MAP[i][j] = 0
inbound = lambda r,c : 0<=r<R+2 and 0<=c<C
def canGoDown(r,c):
    if not inbound(r+2,c): return False
    if not inbound(r+1,c+1) or not inbound(r+1,c-1): return False
    if (MAP[r+2][c] or MAP[r+1][c+1] or MAP[r+1][c-1]): return False
    return True

def canGoDownRotateW(r,c):
    if not inbound(r+2,c-1): return False
    if not inbound(r+1,c-1) or not inbound(r+1,c-2): return False
    if not inbound(r,c-2) or not inbound(r-1,c-1): return False
    if (MAP[r+2][c-1] or MAP[r+1][c-1] or MAP[r+1][c-2]or MAP[r][c-2]or MAP[r-1][c-1]): return False
    return True

def canGoDownRotateE(r,c):
    if not inbound(r+2,c+1): return False
    if not inbound(r+1,c+1) or not inbound(r+1,c+2): return False
    if not inbound(r,c+2) or not inbound(r-1,c+1): return False
    if (MAP[r+2][c+1] or MAP[r+1][c+1] or MAP[r+1][c+2]or MAP[r][c+2]or MAP[r-1][c+1]): return False
    return True
answer = 0
for _ in range(K):
    c,d = map(int,input().split())
    c -= 1
    r = 0
    while 1:
        if(canGoDown(r,c)):
            r+=1
        elif(canGoDownRotateW(r,c)):
            r += 1
            c -= 1
            d = (d-1)%4
        elif(canGoDownRotateE(r,c)):
            r += 1
            c += 1
            d = (d+1)%4
        elif r <= 2:
            clear()
            break
        else:
            dr, dc = directions[d]
            M = r
            for ddr, ddc in ((1,0),(-1,0), (0,1), (0,-1)):
                nr = r+dr+ddr
                nc = c +dc +ddc
                if not inbound(nr, nc): continue
                M = max(MAP[nr][nc],M)
            for dr, dc in ((1,0),(-1,0), (0,1), (0,-1),(0,0)):
                MAP[r+dr][c+dc] = M
            answer += M
            break
print(answer)