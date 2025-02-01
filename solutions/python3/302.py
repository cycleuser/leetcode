
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        """
        Given an "image" represented by a 2D array of '1's (land) and '0's (water),
        return the area of the smallest rectangle that contains all land in the matrix.
        
        Args:
            image: A list of lists of strings representing the image. Each cell is either '1' or '0'.
            x, y: Coordinates within the image to start searching for the bounding box.

        Returns:
            The area (number of pixels) of the smallest rectangle containing all land in the matrix.
        """
        
        l, r, u, d = [y], [y], [x], [x]  # 初始化左右上下边界
        m, n = len(image), len(image[0])  # 获取图像的行数和列数

        def dfs(i: int, j: int) -> None:
            """
            Depth-first search to explore the land cells and update the boundaries.
            
            Args:
                i: Current row index in the image.
                j: Current column index in the image.
            """
            if i < u[0]: u[0] = i  # 更新上边界
            elif i > d[0]: d[0] = i
            if j < l[0]: l[0] = j  # 更新左边界
            elif j > r[0]: r[0] = j
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == "1":
                    image[x][y] = "0"  # 标记已访问过的陆地
                    dfs(x, y)
        
        dfs(x, y)  # 从起始点进行深度优先搜索
        
        return (r[0] - l[0] + 1) * (d[0] - u[0] + 1)  # 计算矩形面积
