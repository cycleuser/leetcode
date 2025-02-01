
class Solution:
    # 定义一个类来解决信封嵌套问题

    def maxEnvelopes(self, envelopes):
        """
        :param envelopes: List[List[int]], 二维列表表示每个信封的宽和高
        :return: int，可以相互嵌套的最大信封数
        """
        # 对信封按照宽度升序、高度降序排序
        tails = []
        for w, h in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            # 使用二分查找找到tails中第一个大于等于当前高度的位置i
            i = bisect.bisect_left(tails, h)
            if i == len(tails):  # 如果插入位置在尾巴末端，说明找到了一个更长的递增子序列
                tails.append(h)
            else:  # 否则用当前高度替换tails中对应位置的高度
                tails[i] = h
        return len(tails)  # 返回最长递增子序列的长度，即最大嵌套信封数
