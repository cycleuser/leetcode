
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        # 递归函数，计算当前员工及其下属的重要性总和
        def dfs(id):
            self.val += dic[id].importance
            for sub in dic[id].subordinates:
                dfs(sub)
        
        # 构建员工字典
        dic = {emp.id: emp for emp in employees}
        
        # 初始化结果变量
        self.val = 0
        
        # 开始递归计算重要性总和
        dfs(id)
        
        return self.val
