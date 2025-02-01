
class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        
        输入两个列表，验证pushed序列是否可以通过栈操作按顺序得到popped序列。
        - 使用一个辅助数组arr模拟栈
        - i指针用于跟踪popped中当前需要匹配的元素
        """
        arr, i = [], 0
        for num in pushed:
            arr.append(num)
            # 当前栈顶与popped[i]相等时，出栈并i++
            while arr and arr[-1] == popped[i]:
                i += 1
                arr.pop()
        # 最终检查arr剩余元素是否能逆序匹配popped
        return arr == popped[i:][::-1]
