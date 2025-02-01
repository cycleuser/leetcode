
class Solution:
    # 定义一个类来解决问题

    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # 初始化结果列表
        res = []
        
        # 按照学生ID降序，分数升序排序
        items.sort(key=lambda x: (-x[0], x[1]))
        
        while items:
            # 选择前5个最高分计算平均分并加入结果中
            res.append([items[-1][0], sum(b for a, b in items[-5:]) // 5])
            
            # 移除已处理的学生记录
            while items and items[-1][0] == res[-1][0]:
                items.pop()
        
        return res
    # 返回每个学生ID及其对应的平均分数
