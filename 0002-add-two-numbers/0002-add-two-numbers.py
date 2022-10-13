# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        crnt_node, tens, units = dummy_node, 0, 0
        
        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + tens
                l1, l2 = l1.next, l2.next
                
            elif l1:
                sum = l1.val + tens
                l1 = l1.next
                
            else:
                sum = l2.val + tens
                l2 = l2.next
                
            tens, units = sum//10, sum%10
            new_node = ListNode(units)
            crnt_node.next = new_node
            crnt_node = crnt_node.next
            
        if tens == 1:
            crnt_node.next = ListNode(1)
            
            
                
        return dummy_node.next
            
                
                
                
                
                
                
                

        
    
        
            
        
            
            
            
            
            
            
            
        