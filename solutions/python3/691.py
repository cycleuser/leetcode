
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # 使用Counter统计目标字符串中每个字符的数量
        cnt = collections.Counter(target)
        # 初始化结果为无穷大，用于记录最小贴纸数量；len(target)表示target长度
        res = [float("inf")]
        
        def dfs(dic, used, i):
            """
            dic: 当前已使用的字符统计字典
            used: 已用到的贴纸数量
            i: 目标字符串中当前处理到的位置索引
            """
            if i == len(target):  # 如果目标字符串遍历完成
                res[0] = min(res[0], used)  # 更新最小贴纸数
            elif dic[target[i]] >= cnt[target[i]]:  # 当前字符已经足够覆盖目标中需要的数量，跳过
                dfs(dic, used, i + 1)
            elif used < res[0] - 1:  # 如果当前已用的贴纸数量比最小值还小，则继续尝试
                for sticker in stickers:
                    if target[i] in sticker:  # 当前贴纸能覆盖目标字符串中的某个字符，开始递归处理
                        for s in sticker:
                            dic[s] += 1  # 更新当前已用的字符统计字典
                        dfs(dic, used + 1, i + 1)  # 递归调用
                        for s in sticker:
                            dic[s] -= 1  # 恢复状态，回溯

        dfs(collections.defaultdict(int), 0, 0)
        
        return res[0] < float("inf") and res[0] or -1  # 如果找到有效解返回结果，否则返回-1
