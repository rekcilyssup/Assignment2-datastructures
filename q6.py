"""Module for stack data structure operations."""


class Stack:
    """Stack implementation"""
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0


def reverse_string_using_stack(input_str):
    """
    Reverse a string using stack. Implement your own stack. [-Stack]
    # input: string = "reverse me"
    # output: "em esrever"
    """
    stack = Stack()

    # Push all characters onto the stack
    for char in input_str:
        stack.push(char)

    # Pop all characters to build reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


if __name__ == "__main__":
    reverse_string_using_stack("reverse me")
