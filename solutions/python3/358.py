
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """
        s: 需要重新排列的字符串
        k: 重排后两个相同字符之间至少需要间隔的最小距离
        返回值：按要求重新排列后的字符串，如果无法满足要求则返回空字符串
        """

        from collections import Counter
        import heapq

        # 统计每个字符出现的次数，并构建优先队列
        q, last, res, wq = [(-v, k) for k, v in Counter(s).items()], {}, "", []
        heapq.heapify(q)

        # 主循环，处理字符串 s 中的每个字符
        for i in range(len(s)):
            if wq and (wq[0][1] not in last or last[wq[0][1]] + k <= i):
                cnt, char = heapq.heappop(wq)
            else:
                # 当优先队列为空或者没有满足插入条件时，从主队列中取出元素并处理
                while q and (not (q[0][1] not in last or last[q[0][1]] + k <= i)):
                    heapq.heappush(wq, heapq.heappop(q))
                if not q:
                    return ""
                cnt, char = heapq.heappop(q)

            # 将字符添加到结果字符串中，并更新相关数据
            res += char
            cnt += 1
            last[char] = i

            # 如果该字符还有剩余，则重新加入优先队列
            if cnt:
                heapq.heappush(q, (cnt, char))

        return res
