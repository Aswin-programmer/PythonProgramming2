from selectors import SelectSelector


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal_recursive(root):
    if root is None:
        return
    print(root.value)
    preorder_traversal_recursive(root.left)
    preorder_traversal_recursive(root.right)

def inorder_traversal_recursive(root):
    if root is None:
        return
    inorder_traversal_recursive(root.left)
    print(root.value)
    inorder_traversal_recursive(root.right)

def postorder_traversal_recursive(root):
    if root is None:
        return
    postorder_traversal_recursive(root.left)
    postorder_traversal_recursive(root.right)
    print(root.value)

def levelorder_traversal(root):
    ans = []
    if root == None:
        return ans

    queue = []
    queue.append(root)

    while len(queue) != 0:
        size = len(queue)
        level = []
        for i in range(size):
            node = queue.pop(0)
            level.append(node.value)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        ans.append(level)

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

    print("Preorder Traversal:")
    preorder_traversal_recursive(root)

    print("Inorder Traversal:")
    inorder_traversal_recursive(root)

    print("Postorder Traversal:")
    postorder_traversal_recursive(root)

    print("Levelorder Traversal:")
    print(levelorder_traversal(root))

main()
