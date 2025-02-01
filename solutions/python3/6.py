
class Solution:
    # 定义一个转换函数，将字符串s按照指定行数numRows进行转换
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            # 如果行数为1或大于等于字符串长度，则直接返回原字符串
            return s
        
        row, direction, res = 0, -1, [""] * numRows
        # 初始化行索引row，方向direction和结果列表res
        
        for char in s:
            # 遍历字符串中的每个字符char
            res[row] += char
            # 将当前字符添加到对应行的result列表中
            
            if row == 0 or row == numRows - 1: 
                direction *= -1
            # 当到达第一行或最后一行时，改变方向（向下变向上，向上变向下）
            
            row += direction
            # 更新行索引row
        
        return "".join(res)
        # 将result列表中的所有字符串连接成一个完整的字符串并返回
