class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_depth(root):
    if root == None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def main():
    # Constructing the following binary tree:
    #         A
    #        / \
    #       B   C
    #      / \   \
    #     D   E   F

    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('F')

    print(max_depth(root))

main()