
class Solution:
    # 定义一个解决方案类，包含求解最大乘积的方法

    def maxProduct(self, words):
        # 初始化字典和最大乘积变量
        sets, mx = {w: set(w) for w in words}, 0
        # 按单词长度降序排序
        words.sort(key=len, reverse=True)
        
        # 双重循环遍历所有可能的单词对组合
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                # 如果当前两词长度乘积小于等于最大乘积，跳出内层循环
                if len(words[i]) * len(words[j]) <= mx:
                    break
                # 判断两个单词是否无交集字符
                elif not sets[words[i]] & sets[words[j]]:
                    # 更新最大乘积
                    mx = len(words[i]) * len(words[j])
        return mx  # 返回最大乘积
