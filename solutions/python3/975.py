
class Solution:
    # 定义一个类，用于解决奇偶跳跃问题

    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)  # 获取数组长度
        # 初始化两个列表，分别存储更高和更低元素的下一个位置索引
        next_higher, next_lower = [0] * n, [0] * n

        # 第一次遍历，找到每个位置的更高元素下一个位置
        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i  # 更新栈中元素的更高元素索引
            stack.append(i)  # 将当前元素压入栈

        # 第二次遍历，找到每个位置的更低元素下一个位置
        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i  # 更新栈中元素的更低元素索引
            stack.append(i)  # 将当前元素压入栈

        # 初始化两个标志列表，用于记录每个位置是否可以跳到下一个更高或更低的位置
        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1  # 设置最后一个位置的初始值为1

        # 反向遍历数组，更新跳跃标志列表
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]  # 更新当前位置可以跳到更高位置的下一个位置是否可以到达终点
            lower[i] = higher[next_lower[i]]  # 更新当前位置可以跳到更低位置的下一个位置是否可以到达终点

        # 返回可以完成跳跃的数量总和
        return sum(higher)
