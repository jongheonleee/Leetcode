# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         def check(l1: int, l2:int) -> bool:
#             pass
        
        
        length, crnt_node = 0, head
        while crnt_node:
            length += 1
            crnt_node = crnt_node.next
          
        if length == 1:
            return True
        
        elif length%2 == 0:
            # length is an even
            mid, mid_node = length//2, head
            
            while mid-1 != 0:
                mid -= 1
                mid_node = mid_node.next
                
            head2, mid_node.next = mid_node.next, None
            prev, crnt = None, head2
            
            while crnt:
                next = crnt.next
                crnt.next, crnt, prev = prev, next, crnt
                
            l1, l2 = head, prev
            
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                
                l1, l2 = l1.next, l2.next
            return True
        
        else:
            # length is an odd
            mid, mid_node = (length//2)+1, head
            prev = None
            
            while mid-1 != 0:
                mid -= 1
                prev, mid_node = mid_node, mid_node.next
                
            head2, prev.next = mid_node.next, None
            prev, crnt = None, head2
            
            while crnt:
                next = crnt.next
                crnt.next, crnt, prev = prev, next, crnt
                
            l1, l2 = head, prev
            
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                
                l1, l2 = l1.next, l2.next
            return True
        
            
                
            
            
        
                
            
                
                
            
                
                
                


                
            
                
            
                
            
            
            
            
        
#         else:
#             # length is an odd
#             pass
        
        
    
            
            
            
            
                
            


            

    
        
        