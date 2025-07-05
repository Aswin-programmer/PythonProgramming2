from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def BottomViewOfBinaryTree(root):
    queue = []
    queue.append((root, 0))

    verticalOrderTraversalStructure = defaultdict()

    while(len(queue) != 0):
        node, vertical = queue.pop(0)

        verticalOrderTraversalStructure[vertical] = node.value

        if node.left != None:
            queue.append((node.left, vertical-1))
        if node.right != None:
            queue.append((node.right, vertical+1))

    ans = []
    for verticalKey, nodeValue in sorted(verticalOrderTraversalStructure.items()):
        ans.append(nodeValue)

    return ans


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

    print(BottomViewOfBinaryTree(root))

main()