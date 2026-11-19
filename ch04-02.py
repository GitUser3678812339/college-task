class Node():
    def __init__(self):
        self.data = None
        self.link = None
# 첫번째 노드 생성 - 링크 필요 없음
node1 = Node()
node1.data = "person1"
# 두번쨰 노드 생성 - 첫번째 노드와 연결
node2 = Node()
node2.data = "person2"
node1.link = node2
#
node3 = Node()
node3.data = "person3"
node2.link = node3

node4 = Node()
node4.data = "person4"
node3.link = node4

node5 = Node()
node5.data = "person5"
node4.link = node5

current = node1
print(current.data, end = ' ')
while current.link != None:
    current = current.link
    print(current.data, end = ' ')
