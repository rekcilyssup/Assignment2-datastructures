"""Module for binary tree traversal operations."""
# Node format
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


def inorder_traversal(root):
    """
    Implement inorder traversal: Left -> Root -> Right
    Input: 1->2, 1->3, 2->4, 2->5
    Output: [4,2,5,1,3]
    """
    result = []

    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.value)
        result.extend(inorder_traversal(root.right))

    return result


def preorder_traversal(root):
    """
    Implement preorder traversal: Root -> Left -> Right
    Input: 1->2, 1->3, 2->4, 2->5
    Output: [1,2,4,5,3]
    """
    result = []

    if root:
        result.append(root.value)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))

    return result


def postorder_traversal(root):
    """
    Implement postorder traversal: Left -> Right -> Root
    Input: 1->2, 1->3, 2->4, 2->5
    Output: [4,5,2,3,1]
    """
    result = []

    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.value)

    return result
