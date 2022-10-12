# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # split LL into left LL and right LL based on middle of the node
        # first of all, i have to check length of LL
        length, crnt_node = 0, head
        while crnt_node:
            length += 1
            crnt_node = crnt_node.next
          
        # if length of LL is 1, just return True
        if length == 1:
            return True
        
        # if length of LL is an even number
        elif length%2 == 0:
            mid, mid_node = length//2, head
            # access middle of the node in LL
            while mid-1 != 0:
                mid -= 1
                mid_node = mid_node.next
                
            # make head2 for next node which has mid node as previous node
            # cut link that was connected on middle of the node
            head2, mid_node.next = mid_node.next, None
            prev, crnt = None, head2
            
            # reverse right LL
            while crnt:
                next = crnt.next
                crnt.next, crnt, prev = prev, next, crnt
                
            # make two pointers for checking this is palindrom or not
            l1, l2 = head, prev
            
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                
                l1, l2 = l1.next, l2.next
            return True
        
        # if length of LL is an odd number
        else:
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
        
        
    
            
            
            
            
                
            


            

    
        
        