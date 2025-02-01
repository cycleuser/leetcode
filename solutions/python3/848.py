
class Solution:
    # 定义一个类用于解决字母移动问题

    def shiftingLetters(self, S: str, shifts: list[int]) -> str:
        # 初始化累积偏移量sm和结果字符串res
        sm, res = sum(shift % 26 for shift in shifts) % 26, ""
        
        # 遍历每个字符及其对应的移动值
        for i, s in enumerate(shifts):
            # 计算当前字符的新位置，更新累积偏移量sm，并构建结果字符串res
            move, sm = ord(S[i]) + sm % 26, sm - s
            res += chr(move > 122 and move - 26 or move)
        
        # 返回最终处理后的字符串
        return res
