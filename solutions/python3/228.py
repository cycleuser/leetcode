
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 初始化结果列表和栈
        res, stack = [], [nums[0] if nums else None, None]

        for i, num in enumerate(nums):
            # 检查当前数是否与前一个数连续，如果是，则更新栈顶元素
            if i > 0 and nums[i - 1] == num - 1:
                stack[1] = num

            # 如果当前数不连续，则将栈中的范围加入结果，并清空栈
            elif i > 0 and nums[i-1] != num - 1:
                res, stack[0], stack[1] = res + ["->".join(str(q) for q in stack if q != None)], num, None

            # 处理列表最后一个元素的情况
            if i == len(nums) - 1:
                res.append("->".join(str(q) for q in stack if q != None))

        return res
