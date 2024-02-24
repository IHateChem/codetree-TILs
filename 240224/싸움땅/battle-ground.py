import sys
n, m, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
MAP = [[[] for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if t[i][j]: MAP[i][j].append(t[i][j])
players = [list(map(int, input().split())) for _ in range(m)] #x, y, d, s
for i in range(m):
    x, y, d, s = players[i]
    players[i] = (x-1,y-1, d, s)
guns = [0] * m
scores = [0] * m
directions = [(-1, 0), (0,1), (1,0), (0,-1)]
inbound = lambda x, y: 0<=x<n and 0<=y<n
def find(x, y):
    for i in range(m):
        if x == players[i][0] and y == players[i][1]: return i 
def fight(p1, p2):
    diff = players[p1][3] + guns[p1] - players[p2][3] - guns[p2]
    if diff > 0 or (diff==0 and players[p1][3] > players[p2][3]):
        scores[p1] += diff
        lose(p2)
        w = p1
    else:
        scores[p2] -= diff
        lose(p1)
        w = p2
    nx, ny, d, s = players[w]
    if MAP[nx][ny] and max(MAP[nx][ny]) > guns[w]:
        t = guns[w]
        guns[w] = max(MAP[nx][ny])
        MAP[nx][ny].append(t)
        MAP[nx][ny].remove(guns[w])

def lose(p): #2-2-2에플레이어가 무조건 이동한다는 보장이 있나?  
    x, y, d, s = players[p]
    if guns[p]:
        MAP[x][y].append(guns[p])
        guns[p] = 0
    for i in range(4):
        dx, dy = directions[(d+i)%4]
        nx, ny = x+dx, y+dy
        if inbound(nx,ny) and find(nx, ny) == None:
            players[p] = (nx,ny,(d+i)%4,s)
            if MAP[nx][ny] and max(MAP[nx][ny]) > guns[p]:
                t = guns[p]
                guns[p] = max(MAP[nx][ny])
                MAP[nx][ny].append(t)
                MAP[nx][ny].remove(guns[p])
            break

def move(i):
    x, y, d, s = players[i]
    dx, dy = directions[d]
    if not inbound(x+dx, y+dy):
        d = (d+2)%4
        dx, dy = directions[d]
    nx, ny = x+dx, y+dy
    findResult = find(nx, ny)
    players[i] = (nx, ny, d, s)
    if findResult == None:
        if MAP[nx][ny] and max(MAP[nx][ny]) > guns[i]:
            t = guns[i]
            guns[i] = max(MAP[nx][ny])
            MAP[nx][ny].append(t)
            MAP[nx][ny].remove(guns[i])
        return
    fight(i, findResult)
for _ in range(k):
    for i in range(m):
        move(i)
print(*scores)