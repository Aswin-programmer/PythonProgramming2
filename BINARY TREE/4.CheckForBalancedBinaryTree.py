class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_depth(root):
    if root == None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def check_balanced_binary_tree(root):
    if root == None:
        return 0

    lh = max_depth(root.left)
    rh = max_depth(root.right)

    if lh==-1 or rh==-1:
        return -1

    if abs(lh-rh)>1:
        return -1

    return 1 + max(lh, rh)

def main():
    # Constructing the following binary tree:
    #         A
    #        / \
    #       B   C
    #      / \   \
    #     D   E   F

    root = Node('A')
    root.left = Node('B')
    #root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    #root.right.right = Node('F')

    print(check_balanced_binary_tree(root)) # -1 means unbalanced else it's the height of the binary tree.

main()