
class Solution:
    # """
    # 这是一个 MountainArray 的 API 接口。
    # 不要实现它，也不要去推测它的实现方式。
    # """
    # class MountainArray:
    #     def get(self, index: int) -> int:
    #     def length(self) -> int:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            md = mountain_arr.get(mid)
            # 中间点的左侧和右侧值，判断是否为峰值点
            if mid and mountain_arr.get(mid - 1) < md > mountain_arr.get(mid + 1):
                pivot = mid
                break
            elif md < mountain_arr.get(mid + 1):  # 右侧递增
                l = mid + 1
            else:  # 左侧递减
                r = mid - 1

        # 在左侧升序部分查找目标值
        l, r = 0, pivot
        while l <= r:
            mid = (l + r) // 2
            md = mountain_arr.get(mid)
            if md == target:  # 找到目标值，返回索引
                return mid
            elif md < target:  # 目标在右侧，更新左边界
                l = mid + 1
            else:  # 目标在左侧，更新右边界
                r = mid - 1

        # 在右侧递减部分查找目标值
        l, r = pivot, mountain_arr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            md = mountain_arr.get(mid)
            if md == target:  # 找到目标值，返回索引
                return mid
            elif md > target:  # 目标在左侧，更新右边界
                r = mid - 1
            else:  # 目标在右侧，更新左边界
                l = mid + 1

        return -1  # 没找到目标值，返回-1
