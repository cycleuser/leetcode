
class Solution:
    # 定义一个求解重复字符串匹配次数的方法，输入为两个字符串A和B
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # 遍历从1到len(B)//len(A)+2的范围（考虑到可能需要额外拼接A以包含B）
        for i in range(1, 2 + len(B) // len(A) + 1):
            # 检查字符串B是否在重复i次后的字符串A中
            if B in A * i:
                return i  # 如果找到返回当前的i值

        # 如果没有找到合适的i，返回-1表示未找到匹配情况
        return -1
