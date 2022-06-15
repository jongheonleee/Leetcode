class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        
        # it's not satisfied with O(n) in time 
        
        '''
        #main idea : 
        -make res for empty list > total_cnt, ascending_order_list(l1),         
        descending_order_list(l2) > append an element for l1 & l2 : odd_idx > l1.min, even_idx >
        l2.min, gradually increase num(ascending order) > total_cnt == size of a given list:
        return res
        '''
        
        # optimize above idea in space
        # sort - divide into A and B by half(idx) - push each elements in odd_idx, even_idx 