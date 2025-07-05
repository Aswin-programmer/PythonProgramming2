from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def TopViewOfTree(root):
    queue = []
    queue.append((root, 0))

    treeStructure = defaultdict()

    while(len(queue) != 0):
        node, verticalIndex = queue.pop(0)
        if verticalIndex not in treeStructure.keys():
            treeStructure[verticalIndex] = node.value

        if node.left != None:
            queue.append((node.left, verticalIndex - 1))
        if node.right != None:
            queue.append((node.right, verticalIndex + 1))

    ans = []
    for keys, value in sorted(treeStructure.items()):
        ans.append(value)

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

    print(TopViewOfTree(root))

main()
