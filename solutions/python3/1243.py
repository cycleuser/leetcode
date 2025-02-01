
class Solution:
    # 定义一个解决方案类

    def transformArray(self, arr: List[int], change: bool = True) -> List[int]:
        # 传入数组和是否进行变换的标志，默认为True
        
        while change:
            # 当change为True时，继续执行变换
            new = (
                arr[:1]  # 复制数组的第一个元素作为新的数组开头
                + [
                    b + (a > b < c) - (a < b > c)
                    for a, b, c in zip(arr, arr[1:], arr[2:])
                ]  # 对中间部分应用变换规则生成新值
                + arr[-1:]  # 复制数组的最后一个元素作为新的数组结尾
            )
            # 更新arr和change标志
            arr, change = new, arr != new
        return arr  # 返回最终变换后的数组
