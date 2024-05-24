import sys
input = sys.stdin.readline
directions = [(-1,0), (0,1), (1,0), (0,-1)]
R,C,K = map(int,input().split())
MAP = [[0]*C for _ in range(R+2)]
exits = set()
ScoreMap = [[0]*C for _ in range(R+2)]
def clear():
    exits.clear()
    for i in range(R+2):
        for j in range(C):
            MAP[i][j] = 0
            ScoreMap[i][j] = 0
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
visited = set()
def dfs(r,c, M):
    color = MAP[r][c]
    visited.add((r, c))
    for dr, dc in ((1,0),(-1,0), (0,1), (0,-1)):
        if not inbound(r+dr, c+dc) or (r+dr, c+dc) in visited: continue
        nextColor = MAP[r+dr][c+dc]
        if nextColor and (color == nextColor or (r,c) in exits) : 
            M = max(dfs(r+dr, c+dc, M), M)
    return max(M, ScoreMap[r][c])
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
            exits.add((r+dr, c+dc))
            visited = set()
            M = dfs(r+dr, c+dc, r)
            for dr, dc in ((1,0),(-1,0), (0,1), (0,-1),(0,0)):
                MAP[r+dr][c+dc] = _+1
                ScoreMap[r+dr][c+dc] = M
            answer += M
            break
print(answer)