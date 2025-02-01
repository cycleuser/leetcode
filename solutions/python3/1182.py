
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """
        初始化距离数组，用于存储每个位置到最近颜色的距离。
        1. left：从左向右遍历，计算每个位置到最近颜色的距离。
        2. right：从右向左遍历，再次计算每个位置到最近颜色的距离，并合并结果。
        """
        l1 = l2 = l3 = -1
        # 初始化距离数组left，存储到最近的三种颜色的距离
        left = [[float('inf') for _ in range(3)] for __ in range(len(colors))]
        
        for i, c in enumerate(colors):
            if c == 1:
                l1 = i
            elif c == 2:
                l2 = i
            else:
                l3 = i
            
            # 更新left[i]，如果当前颜色是1、2或3之一，则更新距离
            if l1 != -1:
                left[i][0] = i - l1
            if l2 != -1:
                left[i][1] = i - l2
            if l3 != -1:
                left[i][2] = i - l3
                
        # 重置位置索引，以便从右向左遍历
        l1 = l2 = l3 = -1
        # 初始化距离数组right，存储到最近的三种颜色的距离
        right = [[float('inf') for _ in range(3)] for __ in range(len(colors))]
        
        # 从右向左遍历colors列表，更新right数组
        for i in range(len(colors) - 1, -1, -1):
            c = colors[i]
            if c == 1:
                l1 = i
            elif c == 2:
                l2 = i
            else:
                l3 = i
            
            # 更新right[i]，如果当前颜色是1、2或3之一，则更新距离
            if l1 != -1:
                right[i][0] = l1 - i
            if l2 != -1:
                right[i][1] = l2 - i
            if l3 != -1:
                right[i][2] = l3 - i
                
        # 根据queries生成结果
        res = []
        
        for i, c in queries:
            # 从left和right中选择最小距离，如果为inf则置为-1
            res.append(min(left[i][c - 1], right[i][c - 1]))
            
        return [c if c != float('inf') else -1 for c in res]
