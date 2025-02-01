
class Solution:
    def splitLoopedString(self, strs):
        # 将每个字符串处理成按原序或反转后较大者，并初始化结果为空字符串
        arr, res = [s if s > s[::-1] else s[::-1] for s in strs], ""
        
        # 遍历每个字符串及其反向字符串，尝试不同分割组合方式
        for i, word in enumerate(strs):
            for w in (word, word[::-1]):
                s, ind = "", 0
                # 寻找当前单词的最佳分割点以构成最大字典序结果
                for j in range(len(w)):
                    if not s or w[j:] + w[:j] > s: 
                        s, ind = w[j:] + w[:j], j   
                
                # 构造最终候选字符串并更新最优解
                cur = w[ind:] + "".join(arr[i + 1:]) + "".join(arr[:i]) + w[:ind]
                if not res or cur > res: 
                    res = cur
        
        return res
