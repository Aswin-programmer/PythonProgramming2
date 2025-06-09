class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def main():
    node1 = Node(5)
    node2 = Node(6)
    node3 = Node(7)

    node1.left = node2
    node1.right = node3

    print(node1.right.value)
main()