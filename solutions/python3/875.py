
class Solution:
    # 定义一个类来解决求解最低吃香蕉速度的问题

    def minEatingSpeed(self, piles, H):
        # 对香蕉堆进行排序，便于后续二分查找
        piles.sort()

        # 初始化左右指针
        l, r = 1, max(piles)

        # 使用二分查找来确定最小的吃香蕉速度
        while l <= r:
            mid = (l + r) // 2

            # 计算当前速度下吃完所有香蕉需要的时间
            h = sum(math.ceil(p / mid) for p in piles)

            # 如果所需时间超过H，则降低速度（增大左边界）
            if h > H:
                l = mid + 1

            # 如果所需时间少于H，则提高速度（减小右边界）
            elif h < H:
                r = mid - 1

            # 找到恰好等于H的速度，直接返回
            else:
                return mid

        # 最终结果为l
        return l
