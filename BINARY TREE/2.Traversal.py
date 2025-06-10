from selectors import SelectSelector
from typing import no_type_check_decorator


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

def inorder_traversal_iterative(root):
    node = root
    ans = []
    st = []

    while 1:
        if node != None:
            st.append(node)
            node = node.left
        else:
            if len(st) == 0:
                break
            node = st.pop()
            ans.append(node.value)
            node = node.right
    return ans

def postorder_traversal_recursive(root):
    if root is None:
        return
    postorder_traversal_recursive(root.left)
    postorder_traversal_recursive(root.right)
    print(root.value)

def postorder_traversal_iterative_two_stack(root):
    st1 = []
    st2 = []
    ans = []

    st1.append(root)

    while len(st1) != 0:
        node = st1.pop()
        st2.append(node)

        if node.left != None:
            st1.append(node.left)
        if node.right != None:
            st1.append(node.right)

    while len(st2) != 0:
        node = st2.pop()
        ans.append(node.value)
    return ans

# def postorder_traversal_iterative_single_stack(root): #Doubt
#     curr = root
#     st = []
#     ans = []
#
#     while(curr != None or len(st) != 0):
#         if curr != None:
#             st.append(curr)
#             curr = curr.left
#         else:
#             temp = st.pop()
#             ans.append(temp.value)
#             while (len(st) != 0 and temp == (st[len[st]-1].right):



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

def preorder_traversal_iterative(root):
    ans = []
    st = [] # stack
    st.append(root)

    while len(st) != 0:
        node = st.pop()
        ans.append(node.value)

        if node.right != None:
            st.append(node.right)
        if node.left != None:
            st.append(node.left)
    return ans

def PreInPostTraversal(root):
    pre_order = []
    in_order = []
    post_order = []

    st = []
    st.append((root, 1))

    if root == None:
        return

    while len(st) != 0:
        (node, num) = st.pop()

        if num==1:
            pre_order.append(node.value)
            st.append((node, 2))
            if node.left != None:
                st.append((node.left, 1))

        elif num==2:
            in_order.append(node.value)
            st.append((node, 3))
            if node.right != None:
                st.append((node.right, 1))

        else:
            post_order.append(node.value)
    return (pre_order,in_order,post_order)


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

    print("Preorder Traversal Recursive:")
    preorder_traversal_recursive(root)

    print("Preorder Traversal Iterative:")
    print(preorder_traversal_iterative(root))

    print("Inorder Traversal Recursive:")
    inorder_traversal_recursive(root)

    print("Inorder Traversal Iterative:")
    print(inorder_traversal_iterative(root))

    print("Postorder Traversal Recursive:")
    postorder_traversal_recursive(root)

    print("Postorder Traversal Iterative Using Two Stack:")
    print(postorder_traversal_iterative_two_stack(root))

    # print("Postorder Traversal Iterative Using Single Stack:")
    # print(postorder_traversal_iterative_single_stack(root))

    print("Preorder, Inorder and Postorder All In A Single Traversal:")
    (pre_order, in_order, post_order) = PreInPostTraversal(root)
    print(pre_order, in_order, post_order)

    print("Levelorder Traversal:")
    print(levelorder_traversal(root))

main()
