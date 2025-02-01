
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # 初始化队列q和计数器cnt，低位low和高位high的整数值，以及字符串长度ln
        q, cnt, low, high, ln = ["", "0", "1", "8"], 0, int(low), int(high), len(high)
        
        # 使用广度优先搜索遍历所有可能的回文数字
        while q:
            s = q.pop()
            if s and s[0] != "0" and low <= int(s) <= high: 
                cnt += 1
            # 根据规则添加新的候选字符串到队列中
            q += [l + s + r for l, r in (("8", "8"), ("6", "9"), ("9", "6"), ("1", "1"), ("0", "0")) if len(s) <= ln - 2] 

        # 返回计数结果，如果low为0则额外加1
        return cnt if low != 0 else cnt + 1
