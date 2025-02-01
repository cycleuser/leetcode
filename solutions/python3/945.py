
class Solution:
    # 定义一个类来解决最小增量问题
    
    def minIncrementForUnique(self, A):
        """
        :param A: 列表，包含非负整数
        :return: 将列表转换为唯一值所需的最小操作次数
        
        算法思路：
            1. 使用两个集合 st 和 used 分别存储原始数组和已使用过的数字。
            2. 使用 heapq.heapify() 初始化堆 A。
            3. 创建一个空列表 empty，用于存放尚未被使用的最小整数。
            4. 当堆 A 不为空时，执行以下操作：
                - 弹出堆顶元素 num
                - 如果 num 已经在 used 中，则从 empty 列表中找到可以填补的位置，并将所需的操作次数累加到 move 变量中。
                - 将调整后的数重新推入堆 A。
            5. 返回操作次数 move 作为最终结果。
        """
        st, used, move = set(A), set(), 0
        heapq.heapify(A)
        empty = [i for i in range(80000) if i not in st][::-1] if A else [] 
        while A:
            num = heapq.heappop(A)
            if num not in used:
                used.add(num)
            else:
                while empty[-1] < num:
                    empty.pop()
                move += empty[-1] - num
                heapq.heappush(A, empty.pop())
        return move
