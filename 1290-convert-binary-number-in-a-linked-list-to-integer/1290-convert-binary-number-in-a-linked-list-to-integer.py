# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        crnt_node = head
        b2_str = ''
        
        while crnt_node:
            b2_str += str(crnt_node.val)
            crnt_node = crnt_node.next
            
        return int(b2_str, 2)
        