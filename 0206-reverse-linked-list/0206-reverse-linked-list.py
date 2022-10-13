# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev, crnt = None, head
        while crnt:
            next = crnt.next
            crnt.next, prev = prev, crnt
            crnt = next
            
        return prev


    
        

            

            
            
            
            
            
            