# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        rev = None
        
        while fast and fast.next:
            fast = fast.next.next
            # (좌측)rev는 slow(링크드 리스트 객체)가 할당되고 rev.next는 slow.next를 의미함
            # (우측)rev는 기존 reverse 객체, 즉 slow가 할당되기 전 참조하고 있던 객체
            # 예를들어, 1->2->3->2->1, rev = None
            # 이때, slow는 head 부분을 참조, 1->2->...
            # (좌측)rev는 1->2->..., rev.next는 1->2(1에서 2를 가르키는 링크), slow는 2
            # (우측)rev는 None을 의미함
            # 따라서, rev = 1->None
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
            
        return not rev
        