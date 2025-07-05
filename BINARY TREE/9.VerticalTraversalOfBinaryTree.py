from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def LevelOrderTraversal(root):
    queue = []
    queue.append((root, 0, 0)) #node, vertical, level
    ans = []

    verticalOrderTraversalStructure = defaultdict(lambda: defaultdict(list))

    while(len(queue) != 0):
        size = len(queue)
        for i in range(size):
            node, vertical, level = queue.pop(0)
            verticalOrderTraversalStructure[vertical][level].append(node.value)
            if node.left != None:
                queue.append((node.left, vertical-1, level+1))
            if node.right != None:
                queue.append((node.right, vertical+1, level+1))

    verticalOrderTraversalStructure = dict(sorted(verticalOrderTraversalStructure.items()))

    for vertical_key, vertical_item in verticalOrderTraversalStructure.items():
        vertical_item = dict(sorted(vertical_item.items()))
        temp = []
        for level_key, nodes in vertical_item.items():
            temp.extend(sorted(nodes))
        ans.append(temp)

    return ans

from collections import defaultdict

def LevelOrderTraversalNeatChatgpt(root):
    queue = []
    queue.append((root, 0, 0))  # node, vertical, level
    ans = []

    verticalOrderTraversalStructure = defaultdict(lambda: defaultdict(list))

    while queue:
        node, vertical, level = queue.pop(0)
        verticalOrderTraversalStructure[vertical][level].append(node.value)
        if node.left:
            queue.append((node.left, vertical - 1, level + 1))
        if node.right:
            queue.append((node.right, vertical + 1, level + 1))

    for vertical_key in sorted(verticalOrderTraversalStructure.keys()):
        vertical_item = verticalOrderTraversalStructure[vertical_key]
        temp = []
        for level_key in sorted(vertical_item.keys()):
            temp.extend(sorted(vertical_item[level_key]))  # ✅ FIXED
        ans.append(temp)

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

    print(LevelOrderTraversalNeatChatgpt(root))

main()



