from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def RightViewOfBinaryTree(node, level, ans):
    if node == None:
        return

    if len(ans) == level:
        ans.append(node.value)

    if node.right != None:
        RightViewOfBinaryTree(node.right, level+1, ans)
    if node.left != None:
        RightViewOfBinaryTree(node.left, level+1, ans)

def LeftViewOfBinaryTree(node, level, ans):
    if node == None:
        return

    if len(ans) == level:
        ans.append(node.value)

    if node.left != None:
        LeftViewOfBinaryTree(node.left, level+1, ans)
    if node.right != None:
        LeftViewOfBinaryTree(node.right, level+1, ans)



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

    ansRight = []
    RightViewOfBinaryTree(root, 0, ansRight)
    print(ansRight)

    ansLeft = []
    LeftViewOfBinaryTree(root, 0, ansLeft)
    print(ansLeft)

main()