
class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        """
        初始化蛇游戏，设置初始宽度、高度和食物位置。
        
        参数：
            width (int): 场景的宽度
            height (int): 场景的高度
            food (list[list[int]]): 食物的位置列表
        """
        from collections import deque, OrderedDict

        self.foods = deque(food)  # 使用deque存储食物位置，便于从头部移除已吃的食物
        self.snake = OrderedDict()  # 使用OrderedDict维护蛇的身体，确保插入顺序正确
        self.snake[(0, 0)] = 1  # 初始时蛇的头部在(0, 0)位置

        self.w, self.h = width, height  # 场景宽度和高度
        self.score = 0  # 蛇的得分


    def move(self, direction: str) -> int:
        """
        根据给定的方向移动蛇，返回当前得分或-1表示游戏结束。

        参数：
            direction (str): 移动方向 'U' (上), 'D' (下), 'R' (右), 'L' (左)

        返回：
            int: 当前得分或-1
        """
        x, y = self.snake.popitem(last=False)  # 移除并返回蛇头部的位置

        if direction == "U":
            self.i -= 1
        elif direction == "D":
            self.i += 1
        elif direction == "R":
            self.j += 1
        else:
            self.j -= 1

        # 更新蛇头位置，检查是否吃到食物或撞墙
        if 0 <= self.i < self.h and 0 <= self.j < self.w and (self.i, self.j) not in self.snake:
            self.snake[(self.i, self.j)] = 1

            # 如果吃到了食物
            if self.foods and self.i == self.foods[0][0] and self.j == self.foods[0][1]:
                self.score += 1  # 分数加1
                self.foods.popleft()  # 移除已吃到的食物

                # 将蛇头重新加入到snake中，并保持在最前端
                self.snake.move_to_end((x, y), last=False)
            return self.score
        else:
            return -1  # 越界或撞自己，游戏结束返回-1
