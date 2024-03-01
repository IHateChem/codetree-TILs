import sys
import heapq
input = sys.stdin.readline
N,M,K = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
canons = [(i,j) for i in range(N) for j in range(M) if MAP[i][j]]
attackTime = [[0]*M for _ in range(N)]
directions = ((0,1), (1,0), (0,-1), (-1,0))
attackRelatedNodes = set()

def getAttackerAndDefender():
    minAttackPoint = (50000, 0, 0, 0, (0, 0)) # 공격력, 마지막 공격시간, 행열 합, 열, (행, 열)
    maxAttackPoint = (-1, 0, 0, 0, (0, 0)) # 공격력, 마지막 공격시간, 행열 합, 열
    for i, j in canons:
        t = (MAP[i][j], -1 * attackTime[i][j], -i-j, -j, (i, j))
        minAttackPoint = min(minAttackPoint, t)
        maxAttackPoint = max(maxAttackPoint, t)
    return minAttackPoint[-1], maxAttackPoint[-1] #공격자, 방어자

def getVisitedNodeesfromPath(pos, path):
    visited = [pos]
    for d in path[::-1]:
        x, y = pos
        dx, dy = directions[d]
        nx = (x - dx) % N
        ny = (y - dy) % M
        visited.append((nx, ny))
        pos = (nx, ny)
    return visited

def findLaserRoot(start, end):
    q = [([], start)]
    t =  []
    while q:
        path, pos = heapq.heappop(q)
        x,y = pos
        visited = getVisitedNodeesfromPath(pos, path)
        if pos == end: break
        for d, (dx,dy) in enumerate(directions):
            nx = (x + dx) % N
            ny = (y + dy) % M
            if not MAP[nx][ny] or (nx, ny) in visited: continue
            heapq.heappush(t, ([i for i in path] + [d], (nx, ny)))
        if not q:
            q = t
            t = []
    else: return []
    return path

def laserAttack(path, start, end):
    attackRelatedNodes.add(start)
    attackRelatedNodes.add(end)
    end_x, end_y = end
    start_x, start_y = start
    ap = MAP[start_x][start_y]
    MAP[end_x][end_y] -= ap
    path = getVisitedNodeesfromPath(end, path)
    for x,y in path[1:-1]:
        MAP[x][y] -= ap//2
        attackRelatedNodes.add((x,y))

def artillery(start, end):
    attackRelatedNodes.add(start)
    attackRelatedNodes.add(end)
    start_x, start_y = start
    ap = MAP[start_x][start_y]
    x, y = end
    MAP[x][y] -= ap
    for dx, dy in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,-1), (1,1)):
        nx = (x + dx) % N
        ny = (y + dy) % M
        if (nx, ny) == start: continue
        attackRelatedNodes.add((nx, ny))
        MAP[nx][ny] -= ap // 2

def attack(path, start, end):
    if path: 
        laserAttack(path, start, end)
    else:
        artillery(start, end)

def maintainCanon():
    t = []
    for i in range(N):
        for j in range(M):
            if MAP[i][j] <= 0:
                MAP[i][j] = 0
                continue
            t.append((i,j))
            if not (i,j) in attackRelatedNodes:
                MAP[i][j] += 1
    attackRelatedNodes.clear()
    return t



for k in range(K):
    start, end = getAttackerAndDefender()
    if start == end: break 
    attackTime[start[0]][start[1]] = k + 1
    MAP[start[0]][start[1]] += N + M
    path = findLaserRoot(start, end)
    attack(path, start, end)
    canons = maintainCanon()


t = 0
for i in range(N):
    for j in range(M):
        t = max(t, MAP[i][j])
print(t)