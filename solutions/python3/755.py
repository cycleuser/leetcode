
class Solution:
    def pourWater(self, heights: list[int], V: int, K: int) -> list[int]:
        """
        模拟水滴落入高度数组的过程。
        
        English:
        Simulate the process of water droplets falling into an array of heights.
        """
        for drop in range(V):
            l = r = K  # 初始化左右指针为K位置
            # 向左寻找较低的洼地
            for i in range(K - 1, -1, -1):
                if heights[i] > heights[l]:
                    break
                elif heights[i] < heights[l]:
                    l = i
            # 如果左侧存在更低的位置，则将水滴加在左侧；否则向右寻找较低的洼地
            if l < K:
                heights[l] += 1
            else:
                for j in range(K + 1, len(heights)):
                    if heights[j] > heights[r]:
                        break
                    elif heights[j] < heights[r]:
                        r = j
            # 如果左右都未找到更低洼地，则加在原位置K上
            if l == r == K:
                heights[K] += 1
            elif r > K:  # 将水滴加在右侧较低洼地的位置
                heights[r] += 1
        return heights
