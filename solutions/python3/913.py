
class Solution:
    # 定义猫鼠游戏的解法类

    def catMouseGame(self, graph: 'List[List[int]]') -> 'int':
        """
        返回游戏的结果：1表示老鼠获胜，2表示猫赢，0表示无结果
        :param graph: 鼠、猫可移动到的位置列表图
        :return: 游戏结果
        """
        # 初始化老鼠访问记录和状态表
        mouse_visited = [False] * len(graph)
        mouse_win_map = [[None for _ in range(len(graph))] for _ in range(len(graph))]
        
        # 初始化猫访问记录和状态表
        cat_visited = [False] * len(graph)
        cat_win_map = [[None for _ in range(len(graph))] for _ in range(len(graph))]

        # 检查老鼠是否能获胜
        if self.isMouseWin(graph, 1, 2, mouse_visited, mouse_win_map):
            return 1
        
        # 检查猫是否能获胜
        elif self.isCatWin(graph, 1, 2, cat_visited, cat_win_map):
            return 2

        else:
            return 0

    def isMouseWin(self, graph, mouse, cat, mouse_visited, mouse_win_map):
        """
        判断老鼠能否获胜
        :param graph: 鼠、猫可移动到的位置列表图
        :param mouse: 老鼠当前位置
        :param cat: 猫当前位置
        :param mouse_visited: 记录老鼠已访问过的节点
        :param mouse_win_map: 老鼠状态表
        :return: 是否能获胜
        """
        if mouse == 0:
            return True

        # 如果状态表中已有结果，则直接返回
        if mouse_win_map[mouse][cat] is not None:
            return mouse_win_map[mouse][cat]

        # 标记当前老鼠节点为已访问
        mouse_visited[mouse] = True

        for mouseMove in graph[mouse]:
            if mouseMove == 0 or (mouseMove not in graph[cat] and mouseMove != cat):
                # 检查老鼠移动后的情况
                if not mouse_visited[mouseMove]:
                    mouseWinFlag = True
                    for catMove in graph[cat]:
                        if catMove != 0 and not self.isMouseWin(graph, mouseMove, catMove,
                                                               mouse_visited, mouse_win_map):
                            # 如果猫无法获胜，则老鼠可以获胜
                            mouseWinFlag = False
                            break

                    # 更新状态表和访问记录
                    if mouseWinFlag:
                        mouse_visited[mouse] = False
                        mouse_win_map[mouse][cat] = True
                        return True

        # 清理当前节点的访问标记
        mouse_visited[mouse] = False
        mouse_win_map[mouse][cat] = False
        return False

    def isCatWin(self, graph, mouse, cat, cat_visited, cat_win_map):
        """
        判断猫能否获胜
        :param graph: 鼠、猫可移动到的位置列表图
        :param mouse: 老鼠当前位置
        :param cat: 猫当前位置
        :param cat_visited: 记录猫已访问过的节点
        :param cat_win_map: 猫状态表
        :return: 是否能获胜
        """
        if mouse == 0:
            return False

        # 如果状态表中已有结果，则直接返回
        if cat_win_map[mouse][cat] is not None:
            return cat_win_map[mouse][cat]

        # 标记当前猫节点为已访问
        cat_visited[cat] = True

        for mouseMove in graph[mouse]:
            if mouseMove == 0 or (mouseMove not in graph[cat] and mouseMove != cat):
                catWinFlag = True
                for catMove in graph[cat]:
                    if catMove != 0 and not cat_visited[catMove] and not self.isCatWin(graph, mouseMove, catMove,
                                                                                       cat_visited, cat_win_map):
                        # 如果老鼠无法获胜，则猫可以获胜
                        catWinFlag = False
                        break

                if not catWinFlag:
                    # 清理当前节点的访问标记
                    cat_visited[cat] = False
                    cat_win_map[mouse][cat] = False
                    return False

        # 更新状态表和访问记录
        cat_visited[cat] = False
        cat_win_map[mouse][cat] = True
        return True
