
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        # 初始化队列，包含空字符串和初始的计算状态 (表达式串, 当前目标值, 当前数值, 乘数)
        q = {("", 0, 0, 1)}
        
        # 遍历数字中的每个字符
        for i, c in enumerate(num):
            new = set()  # 存储当前状态
            
            # 对于每一个当前状态，生成新的状态并加入队列
            for s, val, cur, coeff in q:
                if i:  # 如果不是第一个字符
                    new.add((s + "+" + c, val + int(c), int(c), 1))
                    new.add((s + "-" + c, val - int(c), int(c), -1))
                    new.add((s + "*" + c, val + cur * coeff * (int(c) - 1), int(c), cur * coeff))
                
                # 处理前导零的情况
                if s and s[-1] == "0" and cur == 0: 
                    continue
                
                pre = cur  # 保存当前数值
                cur = cur * 10 + int(c)  # 构建新的数值
                new.add((s + c, val + coeff * (cur - pre), cur, coeff))
            
            q = new  # 更新队列

        # 返回满足目标值的表达式串
        return [s for s, val, cur, coeff in q if val == target]
