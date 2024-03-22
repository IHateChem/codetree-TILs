n,m,k = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(n)]
teams = [[(0,0), (0,0), 0, 0] for _ in range(m)] # 머리 좌표, 꼬리 좌표, 길이, 어디가 머리인지
idx = 0
score = 0
inbound = lambda i, j: 0<=i<n and 0<=j<n
def findTail(i,j, idx):
    visited = set([(i,j)])
    n = 1
    while 1:
        n += 1
        flag = False
        for di, dj in ((1,0),(0,1), (-1,0), (0,-1)):
            ni, nj = i+di, j+ dj
            if not inbound(ni, nj) or (ni,nj) in visited or MAP[ni][nj] == 4 or MAP[ni][nj] == 0: continue
            if MAP[ni][nj] == 3:
                flag = True
                i3, j3 = ni, nj
                continue
            flag = False
            MAP[ni][nj] = [idx,n]
            visited.add((ni,nj))
            i,j = ni, nj
            break
        if flag:
            MAP[i3][j3] = [idx,n]
            return (i3, j3), n 

def getPeopleQueue(i,j):
    q = []
    visited = set([(i,j)])
    t = [(i,j)]
    while t:
        i, j = t.pop()
        q.append((i,j))
        for di, dj in ((1,0),(0,1), (-1,0), (0,-1)):
            ni, nj = i+di, j+ dj
            if not inbound(ni, nj) or (ni,nj) in visited or MAP[ni][nj] == 4 or MAP[ni][nj] == 0 or abs(MAP[ni][nj][1]-MAP[i][j][1])!=1: continue
            visited.add((ni,nj))
            t.append((ni, nj))
    return q
            

def move():
    for team in teams:
        flag = False
        i,j = team[team[3]]
        for di, dj in ((1,0),(0,1), (-1,0), (0,-1)):
            ni, nj = i+di, j+ dj
            if not inbound(ni, nj) or MAP[ni][nj] ==0 : continue
            if MAP[ni][nj] == 4:
                flag = False
                break
            if abs(MAP[ni][nj][1] - MAP[i][j][1]) != 1:
                flag = True
                ti, tj = ni, nj
        if flag:
            flag = True
            ni, nj = ti, tj
        team[team[3]] = (ni,nj)
        q = getPeopleQueue(i,j)
        print(q)
        if flag:
            t = MAP[ni][nj]
        else:
            t = 4
        for p in range(team[2]):
            pi, pj = i, j
            i,j = q[p]
            MAP[ni][nj] = MAP[i][j]
            ni, nj = i, j
        i,j = q[0]
        if flag:
            pi, pj = q[0]
            ni, nj = q[-2]
        MAP[ni][nj] = t
        team[(team[3]+1)%2] = (pi,pj) 

def throwBall(i,j, di, dj):
    global score
    while inbound(i, j):
        if not MAP[i][j] in (0, 4):
            t, n = MAP[i][j]
            team = teams[t]
            if team[3]:
                score += (team[2] - n + 1)**2
            else:
                score += (n) ** 2
            team[3] = (team[3] + 1) % 2
            return 
        i, j = i+di, j+ dj


for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1:
            MAP[i][j] = [idx, 1]
            teams[idx][0] = (i,j)
            teams[idx][1], teams[idx][2] = findTail(i,j, idx)
            idx += 1
for Round in range(k):
    move()
    if (Round // n) % 4 == 0:
        i, j =  Round % n ,0
        di,dj = 0, 1
    if (Round // n) % 4 == 1:
        i, j =  n-1 , Round % n
        di,dj = -1, 0
    if (Round // n) % 4 == 2:
        i, j =  n -1 - Round % n, n-1
        di,dj = 0, -1
    if (Round // n) % 4 == 3:
        i, j = 0,  n -1 - Round % n
        di,dj = 1, 0
    throwBall(i,j,di,dj) 
print(score)