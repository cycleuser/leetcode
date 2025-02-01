
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # 获取初始颜色和图片尺寸 - Initial color and dimensions of the image
        old, m, n = image[sr][sc], len(image), len(image[0])
        
        if old != newColor:  # 如果初始颜色不等于新颜色，进行填充操作 - If initial color is not equal to new color, perform filling operation
            q = collections.deque([(sr, sc)])  # 初始化队列 - Initialize queue with starting position
            while q:  # 当队列不为空时循环 - While the queue is not empty
                i, j = q.popleft()  # 弹出队列中的元素 - Pop an element from the queue
                image[i][j] = newColor  # 将当前位置的颜色更新为新颜色 - Update current position's color to new color
                
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):  # 遍历四个方向 - Traverse four directions
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old:  # 检查边界条件和颜色是否匹配 - Check boundary conditions and color match
                        q.append((x, y))  # 将符合条件的位置加入队列 - Append valid positions to the queue
        
        return image  # 返回填充后的图像 - Return the filled image
