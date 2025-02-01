
from functools import lru_cache

class Solution:
    # 定义一个求解音乐播放列表数量的函数
    def numMusicPlaylists(self, N, L, K):
        # 使用lru_cache缓存中间结果，提高性能
        @lru_cache(None)
        def dp(i, j):
            # 当i为0且j不为0时返回0
            return 1 if not i else (dp(i-1, j-1) * (N-j+1) + dp(i-1, j) * max(j-K, 0)) % (10**9+7)
        # 调用dp函数计算最终结果
        return dp(L, N)
