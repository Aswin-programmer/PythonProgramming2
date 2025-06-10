# Any of the traversal algorithm is actually suitable for this usecase.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_same_binary_tree(root1, root2):
    if root1 == None or root2 == None:
        return root1 == root2 #Checking whether both of them are actually NULL.

    return ((root1.value == root2.value) and (is_same_binary_tree(root1.left, root2.left)) and (is_same_binary_tree(root1.right, root2.right)))

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

    print(is_same_binary_tree(root, root))

main()