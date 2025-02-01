
class Solution:
    # 定义一个类来解决问题

    def minDeletionSize(self, A: List[str]) -> int:
        # 初始化结果计数器和当前列的状态
        res = 0
        cur = [""] * len(A)
        
        # 遍历每一列（使用zip(*)对矩阵转置）
        for col in zip(*A):
            # 将当前列状态与新的一行进行比较并排序后对比
            cur2 = list(zip(cur, col))
            if cur2 == sorted(cur2):  # 如果保持顺序，则更新当前状态为排序后的结果，表明这一列不需要删除
                cur = [x[0] for x in sorted(cur2)]
            else:
                res += 1  # 若不是有序的，则说明需要删除该列以满足条件
        
        return res  # 返回最终的结果计数
