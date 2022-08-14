class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        cnt = collections.defaultdict(int)
        
        for n in range(lowLimit, highLimit+1):
            num = 0
            
            for m in str(n):
                num += int(m)
                
            cnt[num] += 1
            
        print(cnt)
            
        max_key = max(cnt, key=cnt.get)
        return cnt[max_key]
            
        
        