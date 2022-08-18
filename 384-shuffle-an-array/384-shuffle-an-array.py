class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums[:]
        self.origin_arr = nums[:]
        

    def reset(self) -> List[int]:
        self.arr = self.origin_arr[:]
        
        return self.arr


    def shuffle(self) -> List[int]:
        for i in range(len(self.arr)):
            random = randint(i, len(self.arr)-1)
            self.arr[i], self.arr[random] = self.arr[random], self.arr[i]
            
        return self.arr
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()