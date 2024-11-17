# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNodeExtension(ListNode):
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = ListNodeExtension.__lt__
        min_heap = []

        for root in lists:
            if root is not None:
                heappush(min_heap, root)
        
        head = tail = ListNode(0)
        while min_heap:
            tail.next = heappop(min_heap)
            tail = tail.next
            if tail.next:
                heappush(min_heap, tail.next)
        return head.next