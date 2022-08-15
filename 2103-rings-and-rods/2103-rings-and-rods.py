class Solution:
    def countPoints(self, rings: str) -> int:
        ten_roads = collections.defaultdict(list)
        res = 0
            
        for i in range(0, len(rings), 2):
            ring, road = rings[i], rings[i+1]
            ten_roads[road].append(ring)

        
        for colors in ten_roads.values():
            if 'R' in colors and 'G' in colors and 'B' in colors:
                res += 1
                        
        return res
            
        
        
        