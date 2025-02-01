
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Initialize result and current square size
        res, count = 0, 0
        
        # Iterate through the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # Convert cell value to integer
                matrix[i][j] = int(matrix[i][j])
                
                # Check if current cell can be part of a square
                if matrix[i][j] != 0:
                    count = 1
                    
                    # Update the square size from left neighbor
                    if j > 0 and int(matrix[i][j - 1]) != 0: 
                        matrix[i][j] += int(matrix[i][j - 1])
                        
                    # Update the square size considering upper diagonal cells
                    if i - 1 >= 0 and int(matrix[i - 1][j]) != 0:
                        k, curr = i - 1, []
                        
                        while k >= 0 and k >= i - matrix[i][j] + 1 and int(matrix[k][j]) != 0:
                            if matrix[k][j] >= count + 1:
                                curr.append(matrix[k][j])
                                
                                # Update current square size
                                if min(curr) >= count + 1: 
                                    count += 1
                            else: 
                                break
                            
                            k -= 1
                    
                    # Update the maximum square size found
                    res = max(res, count ** 2)
        
        return res
