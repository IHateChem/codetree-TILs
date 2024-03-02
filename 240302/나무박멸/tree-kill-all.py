import sys
input = sys.stdin.readline
from collections import defaultdict as dd

N, M, K, C= map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
herbicide = dd(int)
inbound  = lambda x, y: 0<=x<N and 0<=y<N
def growth(): #모든 나무에서 동시에
    for i in range(N):
        for j in range(N):
            cnt = 0
            if MAP[i][j] > 0:
                for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                    ni, nj = i+di, j+dj
                    if not inbound(ni, nj): continue
                    if MAP[ni][nj] > 0: cnt += 1
            MAP[i][j] += cnt

def breeding(t): #벽, 제초제, 나무 없는 곳으로 주위에 없는 수만큼 나머지 
    added = dd(int)
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > 0:
                cnt = 0
                for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                    ni, nj = i+di, j+dj
                    if not inbound(ni, nj): continue
                    if MAP[ni][nj] == 0 and herbicide[(ni,nj)] < t: cnt += 1
                for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                    ni, nj = i+di, j+dj
                    if not inbound(ni, nj): continue
                    if MAP[ni][nj] == 0 and herbicide[(ni,nj)] < t: added[(ni, nj)] += MAP[i][j] // cnt
    for (x, y), v in added.items():
        MAP[x][y] = v
def calcRemoved(x, y):
    cnt  = MAP[x][y]
    for k in range(1, K+1):
        for dx, dy in ((1,1), (1,-1), (-1, 1), (-1, -1)):
            nx, ny = k*dx + x , k*dy + y
            if not inbound(nx, ny): continue
            if MAP[nx][ny] > 0: cnt += MAP[nx][ny]
    return cnt

def weeding(t): #나무 있는 곳에 뿌리면 K만큼 대각선으로 전파. c년 유지. 원래있었으면 갱신
    pos = (0, 0)
    cnt =  0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] < 1: continue
            t = calcRemoved(i,j)
            if t > cnt: 
                cnt = t
                pos = (i, j)
    x, y = pos
    herbicide[(x,y)] = t + C
    MAP[x][y] = 0
    if MAP[x][y] > 0:
        for k in range(1, K+1):
            for dx, dy in ((1,1), (1,-1), (-1, 1), (-1, -1)):
                nx, ny = k*dx + x , k*dy + y
                if not inbound(nx, ny): continue
                herbicide[(nx,ny)] = t + C
                MAP[nx][ny] = 0
    return cnt
answer = 0
for i in range(M):
    growth()
    breeding(i+1)
    answer += weeding(i+1)

print(answer)