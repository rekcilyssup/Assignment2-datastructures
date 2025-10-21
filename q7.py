"""Module for queue and binary tree traversal operations."""
# Node Format
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


class Queue:
    """A simple queue implementation."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0


def level_order_traversal(root):
    """
    Given a binary tree, return level order traversal using queue.
    Implement your own queue. [Queue]
    input: 1->left 2, 1->right 3, 2->left 4, 2->right 5, 3->left 6, 3->right 7
    output:  [1, 2, 3, 4, 5, 6, 7]
    """
    if not root:
        return []

    queue = Queue()
    queue.enqueue(root)
    result = []

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return result


if __name__ == "__main__":
    level_order_traversal(None)
