
class Solution:
    # 定义一个类来解决分配问题

    def findContentChildren(self, g, s):
        # 对满足条件的儿童和饼干大小进行降序排序
        g.sort(reverse=True); s.sort(reverse=True)
        res = 0  # 记录能够满足需求的儿童数量
        
        # 当有剩余的饼干和需要分配的儿童时，继续循环
        while s and g:
            if g[-1] <= s[-1]:  # 检查当前最大需求是否能被当前最大饼干满足
                res += 1  # 如果可以满足，则计数器加一，并移除一个饼干和需求
                g.pop(); s.pop()
            else:  # 否则，说明当前最大饼干不能满足当前最大需求，移除一个饼干尝试下一个小一点的饼干
                s.pop()
        return res  # 返回能够被满足的需求数量
