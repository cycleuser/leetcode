
class Solution:
    # 定义一个解题类

    def scheduleCourse(self, courses):
        """
        :param courses: 课程列表，每个元素为 (开始时间, 结束时间) 的元组
        :return: 最多可以完成的课程数
        """
        import heapq
        pq = []  # 使用优先队列来存储选中的课程时长（取负数以利用最小堆实现最大堆效果）
        
        start = 0  # 当前已完成课程的时间总和
        
        for t, end in sorted(courses, key=lambda x: x[1]):  # 按照结束时间排序
            start += t  # 加入当前课程所需时间到已选课程总时间中
            heapq.heappush(pq, -t)  # 将当前课程时长取负后加入优先队列
            
            while start > end:  # 若已完成课程总时间超过了当前课程的结束时间
                start += heapq.heappop(pq)  # 移除优先队列中时长最大的课程（即弹出并加上正值）
        
        return len(pq)  # 返回优先队列中的元素个数，即最多可以完成的课程数量
