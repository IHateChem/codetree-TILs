import heapq
from collections import  deque, defaultdict as dd
import sys
input = sys.stdin.readline
Q = int(input())
_, N, u = input().strip().split()
N = int(N)
domain = u.split("/")[0]
problem_queue = dd(list)
problem_queue[domain] = [(1, 0, u)]
cnt = 1
used_url_in_queue = set([u])
grader = [0]*(N+1)
grading_domain = set()
grader_heap =list(range(1,N+1))
heapq.heapify(grader_heap)
domain_start = dd(int)
domain_fin = dd(int)
for _ in range(Q-1):
    commands = list(input().strip().split())
    status = commands[0]
    if status == "200":
        _, t, p, u = commands
        if u in used_url_in_queue: continue
        d = u.split("/")[0]
        heapq.heappush(problem_queue[d], (int(p), int(t), u))
        used_url_in_queue.add(u)
    elif status == "300":
        _ , t1 = commands
        request_domain = 0
        request_min = (10000000, 0, 0)
        if not grader_heap: continue
        for domain, h in problem_queue.items():
            if not h: continue
            if domain in grading_domain or (domain_start[domain] and (domain_fin[domain] - domain_start[domain]) * 3 + domain_start[domain] > int(t1)): continue
            if request_min > h[0]:
                request_domain = domain
                request_min = h[0]
        if request_domain:
            p,t, u = heapq.heappop(problem_queue[request_domain])
            used_url_in_queue.remove(u)
            domain, number = u.split("/")
            g = heapq.heappop(grader_heap)
            grader[g] = domain
            grading_domain.add(domain)
            domain_start[domain] = int(t1)
    elif status == "400":
        _, t, j = commands
        t, j = map(int, [t,j])
        domain = grader[j]
        if domain:
            grader[j] = 0
            grading_domain.remove(domain)
            domain_fin[domain] = t
            heapq.heappush(grader_heap, j)
    else:
        t = 0
        for domain, h in problem_queue.items():
            t += len(h)
        print(t)