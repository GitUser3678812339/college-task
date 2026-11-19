## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = "")
    while current.link != None:
        current= current.link
        print(current.data, end = " ")
    print()

memory = []
head, current, pre = None, None, None
dataArray = ["person1", "person2", "person3", "person4", "person5"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]: 
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)