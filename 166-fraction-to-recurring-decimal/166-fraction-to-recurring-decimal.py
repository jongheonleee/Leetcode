class Solution:
    def fractionToDecimal(self, numerator, denominator):
        
        n, reminder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n), '.']
        stack = []
        
        while reminder not in stack:
            stack.append(reminder)
            n, reminder = divmod(reminder * 10, abs(denominator))
            result.append(str(n))

            
        idx = stack.index(reminder)
        result.insert(idx + 2, '(')
        result.append(')')
        
        return ''.join(result).replace('(0)', '').rstrip('.')


                    
                
            
            
            
        
        
        