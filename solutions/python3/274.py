
class Solution:
    # 定义一个类来解决h指数问题

    def hIndex(self, citations):
        # 排序引用数组，以便后续处理
        citations.sort()

        # 遍历排序后的引用数组
        for i in range(len(citations)):
            if len(citations) - i <= citations[i]:
                # 如果当前索引对应的引用数大于等于剩余的论文数量，则返回h指数
                return len(citations) - i

        # 若未找到满足条件的情况，返回0
        return 0
