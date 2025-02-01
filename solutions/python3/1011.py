
class Solution:
    # 定义一个检查函数，判断最大载重mx是否可行
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(mx):
            """
            :param mx: 最大允许的重量
            :return: 使用不超过D天能否将所有货物运送完
            """
            days, cur = 1, 0
            for w in weights:
                if cur + w <= mx:
                    cur += w  # 当前船的载重加上当前货物重量仍小于等于mx，可以继续装载
                else:
                    days += 1  # 需要额外一天来运送
                    cur = w    # 更新当前船只载重为w
            return days

        # 定义左右边界，即最大和最小可能的每船最大承重
        l, r = max(weights), sum(weights)
        
        # 二分查找确定最小的最大载重量
        while l < r:
            mid = (l + r) // 2
            days = check(mid)
            
            if days <= D:  # 如果天数不超过D，则说明mid可能是一个可行解，尝试更小的值
                r = mid
            else:
                l = mid + 1  # 天数超过D，需要更大的最大载重量来减少天数
            
        return r
