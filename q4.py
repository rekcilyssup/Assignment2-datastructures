"""Module for doubly linked list operations."""
# # Use this class
# class DoublyLinkedListNode:
#     """A node in a doubly linked list."""
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next



# Implement insert, delete and print in doubly linkedlist
def insert():
    """
    Insert
    """
    return

def delete():
    """
    Delete
    """
    return

def print_dll(head):
    """
    print
    """
    current = head
    while current:
        print(current.data)
        current = current.next


def find_node_in_dll(head, data):
    """
    find whether a given number is there or not.
    # input: 1<->2<->3<->4, x=4
    # output: "YES"
    """
    current = head
    while current:
        if current.data == data:
            return "YES"
        current = current.next
    return "NO"


if __name__ == "__main__":
    insert()
    delete()
    print_dll(None)
    find_node_in_dll(None, 1)
