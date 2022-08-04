class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sorted()한 결과 idx 값이 해당 값보다 작은 값들의 개수가 됨
        # 이때, 중복되는 경우를 고려해야함 -> if tmp[i] not in mapping을 사용함
        tmp = sorted(nums)
        mapping = collections.defaultdict()
        res = []
        
        for i in range(len(tmp)):
            if tmp[i] not in mapping:
                mapping[tmp[i]] = i
                
        for i in range(len(nums)):
            res.append(mapping[nums[i]])
            
        return res
                    
        
        

                
        
                
        