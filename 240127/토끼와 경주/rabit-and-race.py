import sys
import heapq
input = sys.stdin.readline
def race(K, S):
    runners = set()
    for _ in range(K):
        j, _, r, c, p, i = heapq.heappop(pq)
        runners.add(i)
        t_max = (0, 0,0)
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr = r + dists[p] * dr
            nc = c  + dists[p] * dc
            if nr < 1:
                t = 1 - nr 
                if (t // (N-1)) % 2:
                    nr =  N - t % (N-1)
                else:
                    nr = 1 + t % (N-1)
            elif nr > N:
                t = nr - N 
                if (t // (N-1)) % 2:
                    nr = 1 + t % (N-1)
                else:
                    nr =  N - t % (N-1)
            if nc < 1:
                t = 1 - nc
                if (t // (M-1)) % 2:
                    nc =  M - t % (M-1)
                else:
                    nc = 1 + t % (M-1)
            elif nc > M:
                t = nc - M  
                if (t // (M-1)) % 2:
                    nc = 1 + t % (M-1)
                else:
                    nc =  M - t % (M-1)
            t_max = max(t_max, (nr+nc, nr, nc))
        _, nr, nc = t_max
        heapq.heappush(pq, (j+1, nr+nc, nr, nc, p, i))
        for k in range(P):
            if k == i: continue
            scores[k] += nr+nc
    t_max = [0,0,0,0,0]
    for k, *info in pq:
        if not info[4] in runners: continue
        t_max = max(t_max, info)
    scores[t_max[4]] += S
Q = int(input())
_, N, M, P, *infos = list(map(int,input().split()))
pids = [infos[2*i] for i in range(P)]
dists = {infos[2*i]: infos[2*i+1] for i in range(P)}
pq = [(0, 2, 1, 1, pid, i) for i, pid in enumerate(pids)]
heapq.heapify(pq)
scores = [0]*P
positions = [(1,1) for _ in range(P)]
for _ in range(Q-2):
    command, a, b = map(int, input().split())
    if(command == 200): race(a, b)
    else: dists[a] *= b
input()
print(max(scores))