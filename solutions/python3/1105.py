
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        """
        计算书籍堆叠所需的最小高度。
        
        Parameters:
            books (List[List[int]]): 每本书的宽度和高度组成的列表，格式为 [width, height]。
            shelf_width (int): 书架的最大容量（宽度）。

        Returns:
            int: 堆叠所有书籍所需的最小高度。
        """
        n = len(books)  # 获取书籍总数
        dp = [float('inf')] * (n + 1)  # 初始化动态规划数组，长度为 books 数量加一
        dp[0] = 0  # 基础情况：没有书时高度为0
        
        for i in range(1, n + 1):
            max_width = shelf_width  # 当前书架剩余宽度初始化为shelf_width
            max_height = 0  # 当前行最大高度初始化为0
            
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                # 尝试将书籍从第j本放到当前堆叠中，更新剩余宽度和最大高度
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                
                # 动态规划状态转移：更新dp[i]的值
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        
        return dp[n]  # 返回最终结果
