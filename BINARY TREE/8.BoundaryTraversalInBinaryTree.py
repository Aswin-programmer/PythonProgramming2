class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def isLeafNode(self):
        return self.left == None and self.right == None

def FindLeftBoundary(temp, res):
    temp = temp.left
    while temp != None:
        if not temp.isLeafNode():
            res.append(temp.value)
        if temp.left != None:
            temp = temp.left
        else:
            temp = temp.right

def FindRightBoundary(temp, res):
    temp_res = []
    while temp != None:
        if not temp.isLeafNode():
            temp_res.append(temp.value)
        if temp.right != None:
            temp = temp.right
        else:
            temp = temp.left
    res += temp_res[::-1]

def FindLeafNodes(node, res):
    if node == None:
        return
    if node.isLeafNode():
        res.append(node.value)
    FindLeafNodes(node.left, res)
    FindLeafNodes(node.right, res)

def FindBoundary(node):
    ans = []
    if node == None:
        return ans

    FindLeftBoundary(node, ans)
    FindLeafNodes(node, ans)
    FindRightBoundary(node, ans)
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

    print(FindBoundary(root))

main()