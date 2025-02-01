
class Solution:
    # 定义一个类，用于解决给定字符串中长度为K的无重复字符子串数量的问题

    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        from collections import Counter  # 引入Counter来统计字符频率
        cnt = Counter(S[:K - 1])  # 统计前K-1个字符的频率
        res = 0  # 初始化结果为0
        
        for i in range(K - 1, len(S)):
            # 更新当前窗口中的字符频率
            cnt[S[i]] += 1
            
            if len(cnt) == K:  # 如果当前窗口中字符种类数等于K，则找到一个满足条件的子串
                res += 1
                
            # 移除窗口最左侧的字符，保持滑动窗口大小为K
            cnt[S[i - K + 1]] -= 1
            if not cnt[S[i - K + 1]]:
                cnt.pop(S[i - K + 1])
                
        return res  # 返回满足条件的子串数量
