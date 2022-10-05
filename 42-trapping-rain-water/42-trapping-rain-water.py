class Solution:
    def trap(self, height: List[int]) -> int:
        l_max, r_max, l, r = height[0], height[-1], 0, len(height)-1
        water = 0
        
        while l < r:
            if height[l] <= height[r]:
                l += 1
                l_max = max(l_max, height[l])
                water += (l_max - height[l])
                
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water += (r_max - height[r])
                
        return water
