"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(
        self, head: "Optional[Node]"
    ) -> "Optional[Node]":
        if not head:
            return None

        # Pre-seed None in the hash map to return None for null pointers automatically
        oldToCopy = {None: None}

        # First pass: create all copy nodes
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        # Return the head node of the new list, not the map
        return oldToCopy[head]