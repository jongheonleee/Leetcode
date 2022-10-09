import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price: int = sys.maxsize
        profit: int = 0
            
        for p in prices:
            min_price = min(p, min_price)
            profit = max(profit, p-min_price)
            
        return profit
        


                    
        

            
                
   



        
                

        
        
                
                
            
            
            