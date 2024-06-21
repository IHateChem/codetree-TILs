import sys
input = sys.stdin.readline
N,M,H,K = map(int,input().split())
MAP = [[set() for _ in range(N)] for _ in range(N)]
TreeMap = [[0]*N for _ in range(N)]
seeker = 0


seeker_map = [[0]*N for _ in range(N)]
seekers_pos = [0] *(2*N*N-2)
inbound = lambda x,y: 0<=x<N and 0<=y<N
x = 0
n = 0
y = 0
d = 2
directions = [(-1,0), (0,1), (1,0), (0,-1)]
while x != N//2 or y != N//2:
    seekers_pos[N*N - 1 -n] = (x,y)
    seeker_map[x][y] = 1
    dx,dy = directions[d]
    if not inbound(x+dx, y+dy) or seeker_map[x+dx][y+dy]:
        d = (d-1)%4
        dx,dy = directions[d]
    x += dx
    y += dy
    n += 1
seekers_pos[0] = (N//2, N//2)
for i in range(N*N-2):
    seekers_pos[N*N + i] = seekers_pos[N*N-2-i]


hiders = []
for i in range(M):
    x,y,d = map(int,input().split())
    hiders.append((x-1,y-1,d))
    MAP[x-1][y-1].add(i)
for _ in range(H):
    x,y  = map(int,input().split())
    TreeMap[x-1][y-1] = 1
def getDistnace(x,y):
    sx, sy = seekers_pos[seeker]
    return abs(x-sx) + abs(y-sy)


def hidersMove():
    newHiders = []
    for n, (x, y, d) in enumerate(hiders):
        if d == -1:
            newHiders.append((-1,-1,-1))
            continue # 잡힘을 의미
        if getDistnace(x,y) <=3:
            MAP[x][y].remove(n)
            dx, dy = directions[d]
            if not inbound(x+dx, y+dy):
                d = (d+2)%4
                dx, dy = directions[d]
            sx, sy = seekers_pos[seeker]
            if sx ==x+dx and sy == y+dy:
                dx = 0
                dy = 0
            x += dx
            y += dy
            MAP[x][y].add(n)
        newHiders.append((x,y,d))
    for i in range(M):
        hiders[i] = newHiders[i]
def getDirection():
    sx, sy = seekers_pos[seeker]
    nx, ny = seekers_pos[(seeker+ 1) % len(seekers_pos)]
    for i in range(4):
        if directions[i] == (nx-sx, ny-sy):
            return i


def seek():
    sx, sy = seekers_pos[seeker]
    d = getDirection()
    dx, dy = directions[d]
    catch = []
    for i in range(3):
        if not inbound(sx, sy): break
        if TreeMap[sx][sy]:
            sx += dx
            sy +=dy
            continue
        while len(MAP[sx][sy]):
            catch.append(MAP[sx][sy].pop())
        sx += dx
        sy += dy
    for c in catch:
        x, y,d = hiders[c]
        hiders[c] = (x,y,-1)
    return catch

answer = 0
for i in range(K):
    hidersMove()
    seeker = (seeker+ 1) % len(seekers_pos)
    caught = seek()
    answer += (i+1)*len(caught)
print(answer)