class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def preorder(root):
    if root is not None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def get_size(root):

    if root is None:
        return 0

    return 1 + get_size(root.left) + get_size(root.right)







if __name__ == "__main__":
    new_node = Node(10)
    new_node.left = Node(3)
    new_node.right = Node(12)
    new_node.left.left = Node(37)
    #inorder(new_node)
    #postorder(new_node)
    #preorder(new_node)
    s = get_size(new_node)
    print(s)