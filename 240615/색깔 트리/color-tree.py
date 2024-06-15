# 최대 깊이를 부모와 비교하여 갱신해주기. 
# 매번 색 업데이트 X 꽁쳐두고 있따가 한번에 슉
# 색 업데이트는 recursive하게 하면 될듯. 
import sys
input = sys.stdin.readline
nodes = {-1: [-1,10000000000000000, [], [], 1,-1]} # key : mid, value: (pid, depth, children, colorDIff, color, 생긴날)
def addNode(mid, pid,color, depth, t):
    if(nodes[pid][1] > 0):
        nodes[mid] = [pid, min(depth-1, nodes[pid][1]-1), [], [], color, t]
        nodes[pid][2].append(mid)

def changeColor(mid, color, t):
    nodes[mid][3] = [t,color]
    nodes[mid][4] = color

def getColor(mid):
    node = nodes[mid]
    stack = [node]
    while node[0] != -1:
        node = nodes[node[0]]
        stack.append(node)
    color = []
    while stack:
        node = stack.pop()
        if not color and not node[3]: continue
        if not color:
            color = node[3]
        elif not node[3] and node[5] > color[0]:
            color = []
        elif node[3] < color:
            node[3] = color
            node[4] = color[1]
        elif node[3] > color:
            color = node[3]
    return node[4]
def getScore(mid):
    totScore, colors = 0, set()
    colors.add(nodes[mid][4])
    for child in nodes[mid][2]:
        _tot, _col = getScore(child)
        colors |= _col
        totScore += _tot
    return totScore + len(colors)**2, colors

N = int(input())
for i in range(N):
    command = list(map(int, input().split()))
    if command[0] == 100:
        addNode(*command[1:], i)
    if command[0] == 200:
        changeColor(*command[1:], i)
    if command[0] == 300:
        print(getColor(command[1]))
    if command[0] == 400:
        score = 0
        for child in nodes[-1][2]:
            _tot, _col = getScore(child)
            score += _tot
        print(score)