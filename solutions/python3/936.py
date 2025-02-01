
class Solution:
    def movesToStamp(self, stamp, target):
        """
        判断当前字符串是否可以通过stamp匹配，如果可以返回True，否则False。
        :param s: 当前子串
        :return: 匹配结果
        英文注释：Check if the current substring can be matched by the stamp. Return True if it matches, False otherwise.
        """
        def okay(s):
            ret = False
            for c1, c2 in zip(s, stamp):
                if c1 == "*": continue  # 如果当前字符为'*'，则跳过检查
                elif c1 != c2: return False  # 不匹配直接返回False
                else: ret = True  # 匹配设置ret为True
            return ret

        t, move, mx, arr = "*" * len(target), 0, 10 * len(target), []  # 初始化变量
        """
        t: target的掩码版本，用于比较判断是否完全匹配
        move: 记录当前操作次数
        mx: 最大尝试次数限制
        arr: 存储成功匹配的位置索引
        
        英文注释：t: the masked version of target used for comparison and judgment, 
                  move: record the current number of operations,
                  mx: maximum trial times limit,
                  arr: store successful match position indexes.
        """
        
        while move < mx:
            pre = move  # 记录上一次匹配次数
            for i in range(len(target) - len(stamp) + 1):
                if okay(target[i:i + len(stamp)]):  # 尝试匹配stamp
                    move += 1
                    arr = [i] + arr  # 成功则记录位置并反转添加到结果数组中
                    target = target[:i] + "*" * len(stamp) + target[i + len(stamp):]  # 更新target状态

            if target == t: return arr  # 如果完全匹配，返回结果
            if move == pre: break  # 连续无匹配则跳出循环

        return []  # 返回空列表表示无法完成匹配
