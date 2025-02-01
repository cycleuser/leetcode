
class Solution:
    # 定义一个类，用于解决重建队列问题

    def reconstructQueue(self, people):
        """
        :param people: List[List[int]], 每个元素是一个人高和需要在前面看到的人数的列表
        :return: List[List[int]], 重构后的队列，满足所有人的条件
        """
        arr = [0] * len(people)
        
        # 首先按高度降序排序，如果高度相同则按k升序排序
        people.sort(key=lambda x: (-x[0], x[1]))
        
        for h, k in people:
            cnt = 0
            # 找到合适的位置插入当前人
            for i in range(len(arr)):
                if not arr[i] or arr[i][0] == h:
                    cnt += 1
                    if cnt == k + 1:
                        arr[i] = [h, k]
        
        return arr
