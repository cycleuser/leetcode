
class Solution:
    # 定义一个类来解决问题

    def numDistinct(self, s: str, t: str) -> int:
        # 构造一个集合存储字符串t中的字符，用于快速查找
        chars = set(t)
        
        # 使用defaultdict来存储每个字符在字符串t中出现的所有索引位置
        index = collections.defaultdict(list)
        for i, c in enumerate(t):
            index[c].append(i)

        # 动态规划数组初始化为0，长度等于字符串t的长度
        dp = [0] * len(t)

        # 遍历字符串s中的每个字符
        for c in s:
            if c in chars:
                # 如果当前字符c在集合chars中，则更新dp数组
                for i in index[c]:
                    dp[i] += dp[i - 1] if i > 0 else 1

        # 返回最终结果，即最后一个元素的值
        return dp[-1]
