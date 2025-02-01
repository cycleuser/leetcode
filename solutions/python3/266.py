
class Solution:
    # 判断给定字符串s是否可以通过重新排列形成回文串
    def canPermutePalindrome(self, s: str) -> bool:
        # 使用collections.Counter统计每个字符出现的次数
        cnt = collections.Counter(s)
        
        # 检查有多少个字符的计数是奇数，返回这个数量小于等于1
        # 中文注释：检查有多少个字符出现了奇数次，如果不超过一个，则可以通过重新排列形成回文串
        return len([c for c in cnt if cnt[c] % 2]) <= 1
