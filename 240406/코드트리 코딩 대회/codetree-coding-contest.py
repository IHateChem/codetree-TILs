import heapq
N,M =map(int,input().split())
problems = list(map(int,input().split()))
if max(problems) > M:
    print(-1)
    exit(0)

heap = [(1, 1, [M-problems[0]])]
visited = set()
while heap:
    n,i, usedBags = heapq.heappop(heap)
    if i == N: break
    problem = problems[i]
    #add  Bag
    v = (n+1, i+1, tuple(sorted([bag for bag in usedBags]+[M-problem])))
    if not v in visited:
        visited.add(v)
        heapq.heappush(heap, v)
    #use Bag
    for j, bag in enumerate(usedBags):
        if bag >= problem:
            v = (n, i+1, tuple(sorted([ubag if k!= j else ubag - problem for k, ubag in enumerate(usedBags)])))
            if not v in visited:
                visited.add(v)
                heapq.heappush(heap, v)
print(n)