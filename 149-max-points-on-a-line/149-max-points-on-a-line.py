class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # gcd: 최대 공약수 구하기 Greatest Common Divisor
        def gcd(a, b):
            return gcd(b%a, a) if a != 0 else b
        
        points_in_line = defaultdict(set)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                
                # line: ax + by + c = 0
                # 1. eq: x = x1
                if x1 == x2:
                    a, b, c = 1, 0, -x1
                    
                # 2. ax1 + by1 + c = 0, ax2 + by2 + c = 0 -> represente each a, b, c based on x1, x2, y1, y2    
                else:
                    a, b, c = y2-y1, x1-x2, x2*y1 - x1*y2
                    
                    # to make sure the same (a, b, c) are calculated for all same lines
                    
                    # rules
                    # -1. a is positive
                    # -2. reduce fraction of a, b and c
                    
                    if a<0:
                        a, b, c = -a, -b, -c
                        
                    g = reduce(gcd, (a, b, c))
                    
                    a, b, c = a/g, b/g, c/g
                    
                line = (a, b, c)
                points_in_line[line].add(i)
                points_in_line[line].add(j)
        
        # edge case: return 0 for 0 point, 1 for 1 point
        return max(map(len, points_in_line.values())) if points_in_line else len(points)