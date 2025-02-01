
class Solution:
    # Python 解决方案类

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])  # 获取矩阵的行数和列数
        
        # 对每一行进行前缀和优化
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
                
        res = 0  # 结果初始化为0
        # 遍历所有可能的子矩阵列范围
        for left in range(n):  # 左边界
            for right in range(left, n):  # 右边界，从左边界开始向右扩展
                c = {0:1}  # 哈希表记录前缀和出现的次数
                cur = 0  # 当前子矩阵的累计和
        
                # 遍历所有行
                for row in matrix:
                    cur += row[right] - (row[left-1] if left else 0)  # 计算当前子矩形单行的和
                    
                    # 利用哈希表快速查找是否存在满足条件的前缀和
                    if cur - target in c:
                        res += c[cur-target]
                    
                    c[cur] = c.get(cur, 0) + 1  # 更新哈希表
        
        return res  # 返回结果
