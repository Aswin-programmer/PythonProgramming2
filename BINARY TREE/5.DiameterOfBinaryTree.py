class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_path_sum_in_binary_tree(root, maxi):
    if root is None:
        return 0

    left_sum = max_path_sum_in_binary_tree(root.left, maxi)
    right_sum = max_path_sum_in_binary_tree(root.right, maxi)

    # Update the maximum path sum (including the current node)
    maxi[0] = max(maxi[0], left_sum + right_sum + root.value)

    # Return the maximum path sum starting from this node (either left or right + current node)
    return root.value + max(left_sum, right_sum)

def main():
    # Constructing the following binary tree (with numerical values):
    #         10
    #        /  \
    #       2    10
    #      / \     \
    #    20   1    -25
    #             /  \
    #            3    4

    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    maxi = [0]  # Using a list to simulate pass-by-reference
    max_path_sum_in_binary_tree(root, maxi)
    print("Maximum path sum:", maxi[0])  # Output should be 42 (20 + 2 + 10 + 10)

main()