
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """
        Solution to find the maximum integer index such that all elements in the array up to this index are equal.

        中文注释：求解数组中从0到该索引处所有元素都相等的最大整数索引。
        """

        def okay():
            """
            Check if it's possible to make all counts of numbers equal or have only one unique count that is 1.

            中文注释：检查是否可以通过改变使得所有数字的计数相同，或者只有一个独特的计数为1。
            """
            if len(dic) == 1 and (1 in dic or 1 in dic.values()):
                return True
            if len(dic) == 2:
                c1, c2 = sorted(dic.keys())
                if c2 - c1 == 1 and dic[c2] == 1 or (c1 == 1 and dic[1] == 1):
                    return True

        cnt = collections.Counter(nums)
        dic = collections.Counter(cnt.values())
        l = len(nums)
        for num in nums[::-1]:
            if okay():
                return l
            dic[cnt[num]] -= 1
            if not dic[cnt[num]]:
                dic.pop(cnt[num])
            cnt[num] -= 1
            if cnt[num]:
                dic[cnt[num]] += 1
            l -= 1
            if okay():
                return l
