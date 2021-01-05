
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

if __name__ == '__main__':
    
    
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    if isbst(root):
        print("Yes BST")
    else:
        print("No Bst")
