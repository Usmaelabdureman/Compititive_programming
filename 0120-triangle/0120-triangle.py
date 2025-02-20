class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # inplace modif
        N = len(triangle)
        
        for i in range(N - 2, -1, -1):
            for j in range(i + 1):
                
                triangle[i][j] = (min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j])
                
        return triangle[0][0]
        