class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # step 1
        flip_row_image = [row[::-1] for row in image]
        
        # step 2
        for r in range(len(flip_row_image)):
            for c in range(len(flip_row_image[0])):
                if flip_row_image[r][c] == 1:
                    flip_row_image[r][c] = 0
                    
                else:
                    flip_row_image[r][c] = 1
                    
        return flip_row_image
        