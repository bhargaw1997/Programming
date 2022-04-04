# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_start = head
        for i in range(k-1):
            k_start = k_start.next
        end=k_start
        k_end=head
        while end.next:
            k_end = k_end.next
            end = end.next
        temp = k_start.val
        k_start.val = k_end.val
        k_end.val = temp
        
        return head
            