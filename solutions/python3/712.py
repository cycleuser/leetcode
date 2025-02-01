
class Solution:
    # 定义一个解决方案类

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # 计算字符串s1和s2的长度，分别加1方便处理边界情况
        l1, l2 = len(s1) + 1, len(s2) + 1
        
        # 初始化动态规划表d，大小为(l1, l2)，初始值为0
        d = [[0] * l2 for _ in range(l1)]
        
        # 遍历动态规划表填充值
        for i in range(1, l1):
            for j in range(1, l2):
                c1, c2 = ord(s1[i - 1]), ord(s2[j - 1])
                
                # 如果i或j为0，初始化当前dp值
                if not (i and j): 
                    d[i][j] = d[i - 1][j] + c1 if i else d[i][j - 1] + c2 if j else 0
                
                # 当字符匹配时，继承左上角的dp值
                elif s1[i - 1] == s2[j - 1]: 
                    d[i][j] = d[i - 1][j - 1]
                
                # 字符不匹配时，取三种删除方式中的最小值
                else: 
                    d[i][j] = min(d[i - 1][j] + c1, d[i][j - 1] + c2, d[i - 1][j - 1] + c1 + c2)
        
        # 返回右下角的dp值，即最小删除代价
        return d[-1][-1]
