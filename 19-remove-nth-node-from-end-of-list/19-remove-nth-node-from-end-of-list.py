# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1=head
        ptr2=head
        while n-1!=0:
            ptr1=ptr1.next
            n-=1
        if ptr1.next is None:
            return head.next
        while ptr1.next is not None:
            ptr1=ptr1.next
            prev=ptr2
            ptr2=ptr2.next
        if prev is not None:
            prev.next=ptr2.next
        return head