
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        :param flowerbed: 一个整数列表，表示花坛的状态。1 表示位置已有花朵，0 表示可以种植花朵。
        :param n: 需要尝试在花坛中种植的花朵数量
        :return: 如果可以成功种植指定数量的花朵返回 True, 否则返回 False.
        """
        # 剩余需要种植的花朵数
        num = n
        
        # 检查花坛长度小于等于1的情况
        if len(flowerbed) <= 1:
            if (num == 1 and flowerbed == [0]) or (num == 0):
                return True
            else:
                return False
        
        # 处理边界情况：在起始位置种植花朵
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            num -= 1
        
        # 处理边界情况：在末尾位置种植花朵
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            num -= 1
        
        # 遍历花坛中间部分，尝试种植花朵
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] != 1 and flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                flowerbed[i] = 1
                num -= 1
        
        # 检查是否成功种植了所有需要的花朵
        return num <= 0
