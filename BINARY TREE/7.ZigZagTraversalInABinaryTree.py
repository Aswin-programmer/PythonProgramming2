class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def zig_zag_traversal(root):
    ans = []
    if root == None:
        return ans

    queue = []
    queue.append(root)

    interchange_order = True

    while len(queue) != 0:
        size = len(queue)
        level = []

        interchange_order = not interchange_order

        for i in range(size):
            node = queue.pop(0)
            level.append(node.value)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        ans.append(level[:: -1] if interchange_order == True else level)

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

    print(zig_zag_traversal(root))

main()