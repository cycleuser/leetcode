
class Solution:
    # 将整数n转换为对应的Excel表格中的列标题
    def convertToTitle(self, n: int) -> str:
        result = ""
        # 当n大于0时，持续进行转换
        while n > 0:
            if n % 26 == 0:
                # 如果n模26等于0，则当前位为'Z'
                result += "Z"
                n = (n // 26) - 1
            else:
                # 否则，计算当前字符并添加到结果中
                result += chr((n % 26) + ord("@"))
                n = n // 26
        return result[::-1]  # 反转字符串以获得正确的列标题
