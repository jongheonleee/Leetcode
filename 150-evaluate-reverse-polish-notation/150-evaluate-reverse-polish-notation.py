class Solution:
    def evalRPN(self, tokens):
        st = []
        
        def calculate(a, b, o):
            if o == '+':
                return a+b
            
            if o == '-':
                return b-a
            
            if o == '*':
                return a*b
            
            if o == '/':
                return int(b/a)
            
        for t in tokens:
            if t in '*/+-':
                st.append(calculate(st.pop(), st.pop(), t))

            else:
                st.append(int(t))
                
        return st[-1]
    
    