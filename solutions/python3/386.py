
class Solution:
    # 定义一个Solution类

    def lexicalOrder(self, n):
        # 方法: lexicalOrder，输入参数n，返回1到n之间的数字按照字典序排序的结果
        
        return sorted(range(1, n + 1), key=str)  # 使用sorted函数和key=str将范围内的数字按字符串形式排序
