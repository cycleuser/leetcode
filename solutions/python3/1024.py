
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 按起始时间降序排序，如果起始时间相同，则按结束时间升序排序
        clips.sort(key=lambda x: (-x[0], x[1]))
        
        x = cnt = mx = 0
        # 当存在clips且当前时间小于目标时间和当前最远播放时间为终止条件
        while clips and clips[-1][0] <= x < T:
            # 遍历所有满足当前时间的剪辑，更新最大结束时间
            while clips and clips[-1][0] <= x:
                mx = max(mx, clips.pop()[1])
            
            if mx > x:
                # 更新当前位置为最远播放位置
                x = mx
                cnt += 1
        
        return cnt if x >= T else -1
