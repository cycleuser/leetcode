
class Solution:
    # 检查两个字符串S和T是否表示相同的有理数，最多保留前20位有效数字
    def isRationalEqual(self, S: str, T: str) -> bool:
        def parse(s):
            # 找到括号开始位置
            i = s.find('(')
            if i >= 0:
                # 替换循环节，只保留20次循环后的结果以简化比较
                s = s[:i] + s[i + 1:-1] * 20
            return float(s[:20])
        
        # 比较两个字符串解析后的浮点数是否相等
        return parse(S) == parse(T)
