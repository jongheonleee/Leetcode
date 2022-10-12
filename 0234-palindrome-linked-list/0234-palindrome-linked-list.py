# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # append all node.val in list
        # then solve this by two pointers
        lst = []
        crnt_node = head
        while crnt_node:
            lst.append(crnt_node.val)
            crnt_node = crnt_node.next
            
        left, right = 0, len(lst)-1
        
        while left <= right:
            if lst[left] != lst[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
    
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         ll_len = 0
#         crnt_node = head
#         while crnt_node:
#             ll_len += 1
#             crnt_node = crnt_node.next
            
#         if ll_len % 2 == 0:
#             mid = head
#             for _ in range((ll_len//2)-1):
#                 mid = mid.next
                
#             head2, mid.next = mid.next, None
            
#             prev, crnt, next = None, head2, head2.next
            
#             while crnt:
#                 crnt.next = prev
#                 prev = crnt
#                 crnt = next
#                 next = crnt.next if crnt else None
                
            
#             l1, l2 = head, head2
#             while l1 and l2:
#                 if l1.val != l2.val:
#                     return False
                
#                 l1, l2 = l1.next, l2.next
                
#             return True
        
#         else:
#             mid = head
#             for _ in range((ll_len//2)+1):
#                 mid = mid.next
                
#             head2, mid.next = mid, None
            
#             prev, crnt, next = None, head2, head2.next
            
#             while crnt:
#                 crnt.next = prev
#                 prev = crnt
#                 crnt = next
#                 next = crnt.next if crnt else None
                
            
#             l1, l2 = head, head2
#             while l1 and l2:
#                 if l1.val != l2.val:
#                     return False
                
#                 l1, l2 = l1.next, l2.next
                
#             return True
            
            
            
            
            
                
            


            

    
        
        