# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head, even_head = ListNode(-1), ListNode(-1)
        op, ep = odd_head, even_head
        step = 0
        crnt_node = head
        
        while crnt_node:
            if step % 2:
                ep.next = crnt_node
                ep = ep.next
            
            else:
                op.next = crnt_node
                op = op.next
                
            crnt_node = crnt_node.next
            step += 1
        
        if step % 2:
            ep.next = None
            
        else:
            op.next = None
            
        op.next = even_head.next
        return odd_head.next
                
        