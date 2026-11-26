class graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        # for i in range(size):
        #     for j in range(size):
G1, G3 = None, None
G1 = graph(4)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print("G1 무방향 그래프")
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end="")
    print()


current = 0
next = None
stack = []
visitedAry = []
for vertex in range(4):
    if G1.graph[current][vertex] == 1:
        next = vertex
        break
current = next
stack.append(current)
visitedAry.append(current)

next = None
for vertex in range(4):
    if G1.graph[current][vertex] == 1:
        if vertex in visitedAry:
            pass
        else :
            next = vertex
            break
current = next
stack.append(current)
visitedAry.append(current)

stack.append(0)
data = stack.pop
visitedAry = []
visitedAry.append(0)
visitedAry.append(1)