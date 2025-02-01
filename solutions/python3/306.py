
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # 获取起始数对
        def getStarter():
            arr = []
            for i in range(1, len(num) - 1):
                for j in range(i + 1, len(num)):
                    s1, s2 = num[:i], num[i:j]
                    # 跳过以0开头且长度大于1的字符串
                    if (s1[0] == "0" and len(s1) > 1) or (s2[0] == "0" and len(s2) > 1):
                        continue
                    arr.append((int(s1), int(s2), j))
            return arr

        # 深度优先搜索，验证是否为添加型数字序列
        def dfs(pre1, pre2, i):
            if i == len(num):  # 遍历完整个字符串
                return True
            sm = pre1 + pre2  # 计算前两个数的和
            l = len(str(sm))  # 获得该和的长度
            new = int(num[i:i + l])  # 获取新生成的数
            return new == sm and dfs(pre2, new, i + l)  # 检查是否相等并递归

        # 找出所有可能的起始组合，并进行验证
        q = getStarter()
        return any(dfs(p1, p2, i) for p1, p2, i in q)
