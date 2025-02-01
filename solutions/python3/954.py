
class Solution:
    # 定义一个类来解决重排问题

    def canReorderDoubled(self, A):
        from collections import Counter
        # 导入Counter工具，用于统计元素出现次数
        
        cnt = Counter(A)
        # 使用Counter统计输入列表A中每个数字的出现频率
        
        for a in sorted(A, key=abs):  # 按绝对值排序后遍历列表
            if cnt[a] and cnt[a * 2]:  # 如果当前元素a及其两倍数存在且次数大于0
                cnt[a] -= 1  # 将计数减一，表示匹配成功一个目标数
                cnt[a * 2] -= 1  
            elif cnt[a] and a % 2 == 0 and cnt[a // 2]:  # 如果当前元素a是偶数且其一半存在且次数大于0
                cnt[a] -= 1  # 将计数减一，表示匹配成功一个目标数
                cnt[a // 2] -= 1  
        # 遍历结束后检查所有元素是否都被匹配
        return all(cnt[a] == 0 for a in A)  # 如果A中每个元素都恰好被匹配了一次，则返回True
