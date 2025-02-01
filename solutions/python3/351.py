
class Solution:
    # 定义一个解决方案类

    def numberOfPatterns(self, m: int, n: int) -> int:
        # 方法：计算从m到n个数字的模式数量

        # 初始化起点列表和模式计数器
        q, pattern = [[c] for c in range(1, 10)], 0
        
        while q:
            # 开始广度优先搜索
            new = []
            
            for arr in q:
                if m <= len(arr) <= n:  # 如果当前路径长度在给定范围内，则计数器加一
                    pattern += 1
                    
                if len(arr) < n:  # 如果当前路径长度小于n，继续扩展
                    last = arr[-1]  # 获取上一步选择的数字

                    for c in range(1, 10):
                        if c not in arr:  # 确保新的选择不在已选列表中
                            # 根据起点位置的不同，设定不同的跳转规则
                            if last in (1, 4, 7) and c == last + 2:
                                if last + 1 in arr:
                                    new.append(arr + [c])
                                    
                            elif last in (3, 6, 9) and c == last - 2:
                                if last - 1 in arr:
                                    new.append(arr + [c])

                            elif last in (1, 2, 3) and c == last + 6:
                                if last + 3 in arr:
                                    new.append(arr + [c])

                            elif last in (7, 8, 9) and c == last - 6:
                                if last - 3 in arr:
                                    new.append(arr + [c])

                            elif last == 1 and c == 9:
                                if 5 in arr:
                                    new.append(arr + [9])

                            elif last == 9 and c == 1:
                                if 5 in arr:
                                    new.append(arr + [1])

                            elif last == 3 and c == 7:
                                if 5 in arr:
                                    new.append(arr + [7])

                            elif last == 7 and c == 3:
                                if 5 in arr:
                                    new.append(arr + [3])

                            else:
                                new.append(arr + [c])
            
            q = new
        return pattern
