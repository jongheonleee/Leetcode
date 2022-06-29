class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        
        cnt = Counter(nums1) & Counter(nums2)
        print(cnt)
        
        return cnt.elements()