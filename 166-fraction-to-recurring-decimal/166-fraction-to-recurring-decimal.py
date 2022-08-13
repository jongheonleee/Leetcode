class Solution:
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        
        return ''.join(result).replace('(0)', '').rstrip('.')
    
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator//denominator)
        
        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res = sign + str(numerator//denominator) + '.'
        numerator %= denominator
        i, part = 0, ''
        m = {numerator:i}
        
        while numerator % denominator:
            numerator *= 10
            i += 1
            rem = numerator % denominator
            part += str(numerator // denominator)
            if rem in m:
                part = part[:m[rem]]+'('+part[m[rem]:]+')'
                return res + part
            m[rem] = i
            numerator = rem
            
        return res + part


                    
                
            
            
            
        
        
        