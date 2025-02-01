
class Solution:
    # 中文: 实现矩阵乘法，给定两个二维数组A和B，返回它们的乘积。
    # 英文: Implement matrix multiplication. Given two 2D arrays A and B, return their product.
    
    def multiply(self, A, B):
        # 中文: 使用列表推导式遍历矩阵A的每一行
        # 英文: Use list comprehension to iterate over each row of matrix A
        return [[sum(a * b for a, b in zip(A[i], [B[k][j] for k in range(len(B))])) for j in range(len(B[0]))] 
                for i in range(len(A))]
