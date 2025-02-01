
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 初始化队列，包含空字符串
        bfs = [""]

        # 过滤掉不包含重复字符的字符串
        for b in filter(lambda x: len(x) == len(set(x)), arr):
            # 构造新字符串，并加入队列中
            bfs += [a + b for a in bfs if not set(a) & set(b)]

        # 返回最长字符串的长度
        return max(map(len, bfs))
