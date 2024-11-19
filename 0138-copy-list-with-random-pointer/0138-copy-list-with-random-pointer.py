"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        if not head:
            return None
        
        new_list = {}

        current = head
        while current:
            new_list[current] = Node(current.val, None, None)
            current = current.next
        
        current = head
        while current:
            new_list[current].next = new_list.get(current.next)
            new_list[current].random = new_list.get(current.random)
            current = current.next
        
        return new_list[head]