# Node클래스로 모든 노드를 연결한후
# bfs
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.nextN = [None]* 4
        self.visited = False
        self.fin = False
    def __repr__(self):
        return f"val: {self.value}, visited: {self.visited} next: {[n.value if n else None for n in self.nextN]}"

def join(NodeMap, i, j):
    # 남북 연결
    if i > 0:
        s = NodeMap[i][j]
        n = NodeMap[i-1][j]
        s.nextN[3] = n
        n.nextN[2] = s
    #동서 연결
    if j> 0:
        w = NodeMap[i][j-1]
        e = NodeMap[i][j]
        w.nextN[0] = e
        e.nextN[1] = w
# 동 0 서 1 남 2 북 3
N,M,F = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
NodeMap = [[Node(i) for i in x] for x in Map]
l,r = N, N
for i in range(N):
    for j in range(N):
        if Map[i][j] == 4:
            NodeMap[i][j].fin = True
        if Map[i][j] == 3:
            l = min(l, i)
            r = min(r, j)
        join(NodeMap, i, j)

Map = [list(map(int,input().split())) for _ in range(M)]
eastNodeMap = [[Node(i) for i in x] for x in Map]
Map = [list(map(int,input().split())) for _ in range(M)]
westNodeMap = [[Node(i) for i in x] for x in Map]
Map = [list(map(int,input().split())) for _ in range(M)]
southNodeMap = [[Node(i) for i in x] for x in Map]
Map = [list(map(int,input().split())) for _ in range(M)]
northNodeMap = [[Node(i) for i in x] for x in Map]
Map = [list(map(int,input().split())) for _ in range(M)]
upNodeMap = [[Node(i) for i in x] for x in Map]


nodes = []

for i in range(M):
    for j in range(M):
        if upNodeMap[i][j].value == 2:
            nodes.append(upNodeMap[i][j])
            nodes[-1].visited = True
        join(upNodeMap, i, j)
        #동서 연결
        if i > 0:
            e = eastNodeMap[i][j]
            w = eastNodeMap[i-1][j]
            w.nextN[0] = e
            e.nextN[1] = w
        # 남북 연결
        if j> 0:
            s = eastNodeMap[i][j-1]
            n = eastNodeMap[i][j]
            s.nextN[3] = n
            n.nextN[2] = s
        
        join(southNodeMap, i, j)

        #동서 연결
        if i > 0:
            e = westNodeMap[i][j]
            w = westNodeMap[i-1][j]
            w.nextN[0] = e
            e.nextN[1] = w
        # 남북 연결
        if j> 0:
            n = westNodeMap[i][j-1]
            s = westNodeMap[i][j]
            s.nextN[3] = n
            n.nextN[2] = s


        if i > 0:
            n = northNodeMap[i][j]
            s = northNodeMap[i-1][j]
            s.nextN[3] = n
            n.nextN[2] = s
        #동서 연결
        if j> 0:
            e = northNodeMap[i][j-1]
            w = northNodeMap[i][j]
            w.nextN[0] = e
            e.nextN[1] = w

        

# 동 0 서 1 남 2 북 3
#동쪽면
# 윗면과 연결
for i in range(M):
    upNodeMap[-1-i][-1].nextN[0] = eastNodeMap[0][i]
    eastNodeMap[0][i].nextN[1] = upNodeMap[-1-i][-1]
#바닥과 연결
for i in range(M):
    NodeMap[l+i][r+M].nextN[1] = eastNodeMap[-1][-1-i]
    eastNodeMap[-1][-1-i].nextN[0] = NodeMap[l+i][r+M]

#서쪽면 
# 윗면과 연결
for i in range(M):
    upNodeMap[i][0].nextN[1] = westNodeMap[0][i]
    westNodeMap[0][i].nextN[0] = upNodeMap[i][0]
# 바닥과 연결
for i in range(M):
    NodeMap[l+i][r-1].nextN[0] = westNodeMap[-1][i]
    westNodeMap[-1][i].nextN[1] = NodeMap[l+i][r-1]


#남쪽면  2
# 윗면과 연결
for i in range(M):
    upNodeMap[-1][i].nextN[2] = southNodeMap[0][i]
    southNodeMap[0][i].nextN[3] = upNodeMap[-1][i]
# 바닥과 연결
for i in range(M):
    NodeMap[l+M][r+i].nextN[3] = southNodeMap[-1][i]
    southNodeMap[-1][i].nextN[2] = NodeMap[l+M][r+i]
# 동쪽 면과 연결
for i in range(M):
    eastNodeMap[i][0].nextN[2] = southNodeMap[i][-1]
    southNodeMap[i][-1].nextN[0] = eastNodeMap[i][0]
# 서쪽 면과 연결
for i in range(M):
    westNodeMap[i][-1].nextN[2] = southNodeMap[i][0]
    southNodeMap[i][0].nextN[1] = westNodeMap[i][-1]

#북 3
# 윗면과 연결
for i in range(M):
    upNodeMap[0][i].nextN[3] = northNodeMap[0][-1-i]
    northNodeMap[0][-1-i].nextN[2] = upNodeMap[0][i]
# 바닥과 연결
for i in range(M):
    NodeMap[l-1][r+i].nextN[2] = northNodeMap[-1][-1-i]
    northNodeMap[-1][-1-i].nextN[3] = NodeMap[l-1][r+i]
# 동쪽 면과 연결
for i in range(M):
    eastNodeMap[i][-1].nextN[3] = northNodeMap[i][0]
    northNodeMap[i][0].nextN[0] = eastNodeMap[i][-1]
# 서쪽 면과 연결
for i in range(M):
    westNodeMap[i][0].nextN[3] = northNodeMap[i][-1]
    northNodeMap[i][-1].nextN[1] = westNodeMap[i][0]

weirdPositions = [list(map(int, input().split())) for _ in range(F)]
weirdNodes = []
ds = [n[-2] for n in weirdPositions]
vs = [n[-1] for n in weirdPositions]
for i in range(F):
    x,y,d,v = weirdPositions[i]
    NodeMap[x][y].value = 1
    weirdNodes.append(NodeMap[x][y])
T = 0

def diffusion(t):
    for i in range(F):
        n = weirdNodes[i]
        v = vs[i]
        d = ds[i]
        if t % v != 0: continue
        nextNode = n.nextN[d]
        if nextNode and nextNode.value != 1 and nextNode.value != 4:
            nextNode.value = 3
            weirdNodes[i] = nextNode
while nodes:
    T += 1
    diffusion(T)
    t = []
    while nodes:
        node = nodes.pop()
        for i in range(4):
            nextNode = node.nextN[i]
            if nextNode and nextNode.value == 0 and nextNode.visited == False:
                t.append(nextNode)
                nextNode.value = 5
            if nextNode and nextNode.fin:
                print(T)
                exit(0)
    nodes = t
print(-1)