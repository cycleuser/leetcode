
class Solution:
    # 定义一个类来解决问题
    
    def minFallingPathSum(self, A):
        # 计算最小下降路径和
        
        for i in range(1, len(A)):
            # 从第二行开始遍历，每一行的每个元素
            for j in range(len(A)):
                # 遍历当前行的所有列
                
                # 更新当前元素为上一行相邻元素中的最小值加上自身
                A[i][j] += min(A[i - 1][max(0, j - 1):j + 2])
        
        return min(A[-1])  # 返回最后一行的最小值，即最终结果
