
class Solution:
    # 定义一个生成杨辉三角的方法
    def generate(self, numRows: int) -> List[List[int]]:
        # 初始结果列表，如果numRows为正，则包含首行[1]，否则为空
        res = numRows and [[1]] or []
        
        # 从第二行开始遍历至第numRows-1行
        for _ in range(numRows - 1):
            # 每一行的第一个和最后一个元素固定为1
            row = [1] + \
                # 计算当前行的中间元素，通过前一行相邻元素之和得到
                [a + b for a, b in zip(res[-1], res[-1][1:])] + \
                [1]
            # 将计算出的新行添加到结果列表中
            res.append(row)
        
        return res
