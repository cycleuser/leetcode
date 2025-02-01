
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        """
        判断是否可以完成所有课程。
        
        :param numCourses: 课程总数
        :param prerequisites: 先修课程关系列表，每个元素为 [先修课程ID, 依赖课程ID]
        :return: 如果可以完成所有课程则返回True，否则返回False
        
        通过构建图和检测环来判断是否能完成所有课程。
        """
        
        def cycle(course: int) -> bool:
            """
            检测以给定课程为起点是否存在环
            
            :param course: 当前检查的课程
            :return: 如果存在环则返回True，否则返回False
            """
            visited[course] = 0  # 标记正在访问该节点
            for next_course in route[course]:
                if visited[next_course] == 0 or (visited[next_course] == -1 and cycle(next_course)):
                    return True
            visited[course] = 1  # 标记已完全访问该节点
            return False
        
        # 构建图和初始化访问状态数组
        route, visited = {i: [] for i in range(numCourses)}, [-1] * numCourses 
        for req in prerequisites:
            route[req[1]].append(req[0])
        
        # 检查每个课程是否存在环
        for course in range(numCourses):
            if visited[course] == -1 and cycle(course):  # 只检查未访问的节点
                return False
        
        return True
