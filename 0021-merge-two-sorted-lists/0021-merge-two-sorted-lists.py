# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        crnt_node = dummy_node
        l1, l2 = list1, list2
        
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    crnt_node.next = l1
                    crnt_node = crnt_node.next
                    l1 = l1.next
                
                elif l1.val > l2.val:
                    crnt_node.next = l2
                    crnt_node = crnt_node.next
                    l2 = l2.next
                    
            elif l1:
                crnt_node.next = l1
                break
                    
            else:
                crnt_node.next = l2
                break
                    
        return dummy_node.next
                
        