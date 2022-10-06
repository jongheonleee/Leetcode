class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 차이가 얼마 안나는 요소들로 묶어주기
        nums.sort()
        lst = []
        
        for i in range(0, len(nums)-1, 2):
            lst.append(min(nums[i], nums[i+1]))
            
        return sum(lst)
        
        

            
                
        
            
        