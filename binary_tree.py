"""Binary tree representation and common methods."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    @staticmethod
    def preorder_traverse(root, process):
        """Traverse the tree in preorder and apply `process` function."""
        if root:
            process(root)
            self.preorder_traverse(root.left, process)
            self.preorder_traverse(root.right, process)

    @staticmethod
    def inorder_traverse(root, process):
        """Traverse the tree in inorder and apply `process` function."""
        if root:
            self.inorder_traverse(root.left, process)
            process(root)
            self.inorder_traverse(root.right, process)
    
    @staticmethod
    def postorder_traverse(root, process):
        """Traverse the tree in postorder and apply `process` function."""
        if root:
            self.postorder_traverse(root.left, process)
            self.postorder_traverse(root.right, process)
            process(root)


    @staticmethod
    def bfs(root, process):
        queue = collections.deque([root]):
        while queue:
            node = queue.popleft()
            if node:
                process(node)
                if node.left:
                    self.bfs(root.left, process)
                if node.right:
                    self.bfs(root.right, process)