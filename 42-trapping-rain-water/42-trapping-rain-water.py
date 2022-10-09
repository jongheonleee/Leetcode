class Solution:
    def trap(self, height: List[int]) -> int:
        # those variable pointed a highest wall which i passed
        # max_l => left side
        # max_r => right side        
        max_l: int = 0
        max_r: int = 0
            
        left, right = 0, len(height)-1
        
        # store how much water can i trap
        water: int = 0
        
        # using two pointers
        while left < right:
            if height[left] <= height[right]:
                # compare which one is bigger between a highest wall that i passed and a wall that i stand
                max_l = max(max_l, height[left])
                # trap a amount of water are subtract between a highest wall that i passed and a wall that i stand
                water += max_l - height[left]
                
                left += 1
                
            else:
                # compare which one is bigger between a highest wall that i passed and a wall that i stand
                max_r = max(max_r, height[right])
                # trap a amount of water are subtract between a highest wall that i passed and a wall that i stand
                water += max_r - height[right]
                
                right -= 1
                
        return water
                    

