import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
participants = [list(map(int,input().split())) for _ in range(M)]
scores = [0]*M
dist = lambda x, y, r, c: abs(x-r) + abs(y-c)
outX, outY = map(int,input().split())
outX -= 1
outY -= 1
for i in range(M): participants[i] = [participants[i][0]-1, participants[i][1]-1]
for a, b in participants:
    MAP[a][b] = -1
outBound = lambda x, y: x<0 or x >= N or x < 0 or y >= N
def move(_):
    nextPos = []
    for n, (x, y) in enumerate(participants):
        if x < 0:
            nextPos.append([x,y])
            continue
        m = 10000
        for dx, dy in ((1,0), (-1,0),(0,1), (0, -1)):
            nx, ny = x + dx, y + dy
            if outBound(nx, ny): continue
            if m < dist(nx, ny, outX, outY): continue
            if m == dist(nx, ny, outX, outY) and MAP[pos[0]][pos[1]] < 1: continue
            m = dist(nx, ny, outX, outY)
            pos = [nx, ny]
        if MAP[pos[0]][pos[1]] < 1:
            scores[n] += 1
        else: pos = [x,y]
        nextPos.append(pos)
    for x, y in participants:
        if x < 0: continue
        MAP[x][y] = 0
    for n, (x, y) in enumerate(nextPos):
        participants[n] = [x, y]
        if x < 0: continue
        if x == outX and y == outY:
            participants[n] = [-1, -1]
            continue
        MAP[x][y] = -1
def findRect():
    for n in range(2, N+1):
        for i in range(N-n+1):
            for j in range(N-n+1):
                flag = 0
                for di in range(n):
                    for dj in range(n):
                        if MAP[i+di][j+dj] < 0: flag |= 1
                        if i+di == outX and j+dj == outY: flag |= 2
                if flag == 3: return (i,j, n)
    return (0,0,0)
def rotate():
    x, y, n = findRect()
    t = [[0]*n for _ in range(n)]
    X, Y = outX, outY
    for i in range(n):
        for j in range(n):
            if MAP[x+i][y+j] > 0:
                MAP[x+i][y+j] -=1
            elif MAP[x+i][y+j] < 0:
                for k in range(M):
                    if participants[k] == [x+i,y+j]: participants[k] = [x+j, y+n-1-i]
            elif x+i == outX and y+j == outY: X, Y = x+j, y+n-1-i
            t[j][n-1-i] = MAP[x+i][y+j]
    for i in range(n):
        for j in range(n):
            MAP[x+i][y+j] = t[i][j]
    return X, Y
for k in range(K):
    move(k)
    outX, outY = rotate()
print(sum(scores))
print(outX+1, outY+1)