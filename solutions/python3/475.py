
class Solution:
    # 定义一个解决类，用于找到供暖器的最大半径

    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # 对供暖器的位置进行排序
        heaters.sort()
        
        # 初始化最大半径为0
        r = 0
        
        # 遍历每个房屋位置
        for h in houses:
            # 使用二分查找确定当前房屋最近的供暖器位置
            ind = bisect.bisect_left(heaters, h)
            
            # 如果房屋在所有供暖器之后
            if ind == len(heaters):
                r = max(r, h - heaters[-1])  # 更新最大半径
            
            # 如果房屋在第一个供暖器之前
            elif ind == 0:
                r = max(r, heaters[0] - h)  # 更新最大半径
                
            else:
                # 计算当前房屋到前后两个供暖器的距离，取较小者更新最大半径
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        
        return r
