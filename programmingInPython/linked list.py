class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insertbtw(self,prev_node,new_data):
        if prev_node is None:
            print("does not exists")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is  None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    def printlis(self):
        temp = self.head
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
lis = Linkedlist()

lis.append(6)
lis.push(7)
lis.push(1)
lis.append(4)
lis.insertbtw(lis.head.next,8)
print("the list is")
lis.printlis()
