class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # matrix[i][j] -> [j][n - i - 1]
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                last_replacement = matrix[i][j]
                # i = 0, j = 1
                # move bottom left to 
                matrix[i][j] = matrix[n - j - 1][i] #[0][1] = [1][0]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1] #[2][1] = [1][2]  # should be [1][0]
                
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1] # [2][1] = [1][2]
                matrix[j][n - i - 1] = last_replacement #[1][2] = [0][1]
    
        # rotate corners
        # i = 0
        # [i][0] -> [i][j]
        # [0][n - i - 1] -> [j][n - i - 1]
        # [n - i - 1][0] -> [n - i - 1][j]
        # [n - i - 1][n - j - 1]



def test():
    solution = Solution()
    input = [[1,2,3],[4,5,6],[7,8,9]]
    output = [[7,4,1],[8,5,2],[9,6,3]]
    solution.rotate(input)
    assert input == output

    input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    solution.rotate(input)
    assert input == output

if __name__ == '__main__':  
    test()
    print("Everything passed")