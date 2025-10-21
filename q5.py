"""Module for circular linked list operations."""
# class ListNode:
#     """A node in a circular linked list."""
#     def __init__(self, data):
#         self.data = data
#         self.next = next

def is_linkedlist_circular(head):
    """
    Find if a LinkedList is circular or not.
    If yes then return the length of the circle.  [Circular LL]
    input: 1->2->3->4->2 (4 is linked back to 2)
    output: 3 (length of circle is 3)
    """
    if not head:
        return -1

    slow = head
    fast = head

    # Detect if there's a cycle using Floyd's algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Found cycle, now calculate length
            cycle_length = 1
            current = slow.next
            while current != slow:
                cycle_length += 1
                current = current.next
            return cycle_length

    return -1


if __name__ == "__main__":
    is_linkedlist_circular(None)
