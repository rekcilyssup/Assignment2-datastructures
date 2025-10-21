"""To check whether a list is palindromic or not"""

def is_linkedlist_palindrome(head):
    """
    Check if a linked list is palindrome or not. [Singly LL] 
    # Input: 1->2->3->2->1
    # Output: "YES" string
    """
    if not head or not head.next:
        return "YES"
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    current = slow.next
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    first_half = head
    second_half = prev
    while second_half:
        if first_half.data != second_half.data:
            return "NO"
        first_half = first_half.next
        second_half = second_half.next
    return "YES"


if __name__ == "__main__":
    is_linkedlist_palindrome(None)
