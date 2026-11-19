class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "person1"
node1.link = node1

node2 = Node()
node2.data = "person2"
node2.link = node1

node3 = Node()
node3.data = "person3"
node2.link = node3
node3.link = node1

node4 = Node()
node4.data = "person4"
node3.link = node4
node4.link = node1

node5 = Node()
node5.data = "person5"
node4.link = node5
node5.link = node1

newNode = Node()
newNode.data = "personA"
newNode.link = node2.link
node2.link = newNode


current = node1
print(current.data, end = ' ')
while current.link != None:
    current = current.link
    print(current.data, end = ' ')

