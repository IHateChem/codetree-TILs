# 플로이드 워샬 통해 모든 점 사이의 거리를 저장해두기. => 2000^3 = 80억..?
# 시작지 변경마다 다익스트라 2만 *15 -> 30만 이거다. 

import sys
import heapq
input = sys.stdin.readline
INF = 100000000000
Q =  int(input())
_, n,m ,*info = map(int, input().split())
graph = [[] for _ in range(n)]
heap = []
commodities = {}

def dijk(s):
    dist = [INF] * (n)
    dist[s] = 0
    visited = set()
    q = [(0,s)]
    while q:
        w, u = heapq.heappop(q)
        if u in visited: continue
        dist[u] = w
        visited.add(u)
        for v, dw in graph[u]:
            if w + dw < dist[v]:
                heapq.heappush(q, (w+dw, v))
    return dist

def addCommodity(id, revenue, dest):
    commodities[id] = (revenue, dest) # rev, dist
    if(revenue >= dist[dest]):
        heapq.heappush(heap, (-1*(revenue-dist[dest]), id))
def delCommodity(id):
    if id in commodities:
        del commodities[id]
def sellAppropriate():
    sell = -1
    while heap:
        cost, id = heapq.heappop(heap)
        if id in commodities:
            sell = id
            delCommodity(id)
            break
    return sell

for i in range(m):
    v,u, w = info[3*i:3*i+3]
    if v == u: continue
    graph[v].append((u,w))
    graph[u].append((v,w))
dist = dijk(0)
for _ in range(Q-1):
    num, *info = map(int,input().split())
    if(num == 200):
        addCommodity(*info)
    if(num==300):
        delCommodity(*info)
    if(num==400):
        print(sellAppropriate())
    if(num==500):
        dist = dijk(info[0])
        heap = []
        for id in commodities.keys():
            r, d = commodities[id]
            c = dist[d]
            if(r >= dist[d]):
                heapq.heappush(heap, ((-1*(r-c), id)))