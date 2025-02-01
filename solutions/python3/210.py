
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[tuple[int, int]]) -> list[int]:
        """
        :param numCourses: 课程总数
        :param prerequisites: 先修课程列表，每个元素为一个元组 (后续课程, 先修课程)
        :return: 满足先修条件的课程顺序列表，如果不存在这样的顺序则返回空列表

        使用拓扑排序来找出满足所有先修关系的课程学习顺序。
        """
        
        # 构建邻接表
        children = collections.defaultdict(set)  # 后续课程 -> 先修课程集合
        parent = collections.defaultdict(set)    # 先修课程 -> 后续课程集合
        
        for course, pre_course in prerequisites:
            children[course].add(pre_course)
            parent[pre_course].add(course)

        # 初始入度为0的节点入栈
        stack = [i for i in range(numCourses) if not children[i]]

        # 拓扑排序
        while stack:
            current_course = stack.pop()
            for next_course in parent[current_course]:
                children[next_course].discard(current_course)
                if not children[next_course]:  # 如果先修课程的入度变为0，加入栈中
                    stack.append(next_course)

        return stack if len(stack) == numCourses else []
