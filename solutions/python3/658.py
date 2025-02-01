
class Solution:
    # 定义一个类，用于解决寻找最接近目标值的k个元素问题

    def findClosestElements(self, arr, k, x):
        """
        :param arr: 列表，存储待查找的整数序列
        :type arr: List[int]
        :param k: 需要返回的元素数量
        :type k: int
        :param x: 目标值，寻找与该值最接近的k个元素
        :type x: int
        :return: 返回包含最接近目标值x的k个整数的列表
        """
        ind, n = bisect.bisect_left(arr, x), len(arr)  # 找到x在有序数组中的插入位置，同时获取数组长度
        
        # 根据左右两侧与x的距离调整ind的位置
        if ind > 0 and x - arr[ind - 1] < arr[ind] - x:
            ind -= 1

        l, r = ind, ind + 1  # 初始化左右指针

        # 寻找最接近目标值的k个元素
        for _ in range(k - 1):
            if r >= n or (l > 0 and x - arr[l - 1] <= arr[r] - x): 
                l -= 1  # 左指针左移
            else:
                r += 1  # 右指针右移

        return arr[l:r]  # 返回结果，包含最接近x的k个元素
