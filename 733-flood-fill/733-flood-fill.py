class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(y, x):
            if y < 0 or y > len(image)-1 or x < 0 or x > len(image[0])-1 or mark != image[y][x]:
                return
            
            if (y, x) in vis:
                return 
            
            image[y][x] = color
            vis.add((y, x))
            
            for dy, dx in dir_:
                dfs(y+dy, x+dx)
            
            
        vis = set()
        mark = copy.deepcopy(image[sr][sc])
        dir_ = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dfs(sr, sc)
        
        return image
        