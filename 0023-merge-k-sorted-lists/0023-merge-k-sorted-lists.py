# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr, heap = None, []
        
        for l1 in lists:
            curr = l1
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
                
        dummy = ListNode(-1)
        crnt = dummy
        
        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            crnt.next = node
            crnt = crnt.next
            
        return dummy.next
            
        