"""Binary tree representation and common methods."""
import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traverse(root, process):
    """Traverse the tree in preorder and apply `process` function."""
    if root:
        process(root)
        preorder_traverse(root.left, process)
        preorder_traverse(root.right, process)

def inorder_traverse(root, process):
    """Traverse the tree in inorder and apply `process` function."""
    if root:
        inorder_traverse(root.left, process)
        process(root)
        inorder_traverse(root.right, process)

def postorder_traverse(root, process):
    """Traverse the tree in postorder and apply `process` function."""
    if root:
        postorder_traverse(root.left, process)
        postorder_traverse(root.right, process)
        process(root)


def bfs(root, process):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            process(node)
            if node.left:
                bfs(root.left, process)
            if node.right:
                bfs(root.right, process)