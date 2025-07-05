class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def IsSymmetricBinaryTree(left, right):
    if left == None or right == None:
        return left == right

    if left.value != right.value:
        return False

    return IsSymmetricBinaryTree(left.left, right.right) and IsSymmetricBinaryTree(left.right, right.left)

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

    print(IsSymmetricBinaryTree(root.left, root.right))

main()