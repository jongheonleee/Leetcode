class Solution:
    def countAndSay(self, n: int) -> str:
        '''    
        i didnt study this code 
        so that i will update after company
        '''
        
        '''
        idea1: https://leetcode.com/problems/count-and-say/discuss/16044/Simple-Python-Solution
        '''
        s = '1'
        
        for _ in range(n-1):
            let, temp, cnt = s[0], '', 0
            
            for l in s:
                if let == l:
                    cnt += 1
                    
                else:
                    temp += str(cnt) + let
                    let = l
                    cnt = 1
                    
            temp += str(cnt) + let
            s = temp
            
        return s
    
    '''
    this is using a regular expression
    '''
    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
            
        return s
    
        
        'other way to solve this by using a regular expression!!'
        # s = '1'
        # for _ in range(n - 1):
        #     s = ''.join(str(len(group)) + digit
        #                 for group, digit in re.findall(r'((.)\2*)', s))
        # return s