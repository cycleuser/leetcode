
class Solution:
    # 定义一个移除指定数量数字的方法
    def removeKdigits(self, num: str, k: int) -> str:
        out = []  # 初始化结果列表
        
        for digit in num:
            # 当k大于0且当前数字小于栈顶元素时，弹出栈顶元素
            while k and out and out[-1] > digit:
                out.pop()
                k -= 1
            
            # 将当前数字压入栈中
            out.append(digit)
        
        # 去除最后k个字符或直至结果为空
        res = ''.join(out[:-k or None])
        
        # 移除结果前导零并返回，若结果为空则返回"0"
        return res.lstrip('0') or "0"
