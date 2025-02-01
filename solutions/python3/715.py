
from bisect import bisect_left as bl, bisect_right as br

class RangeModule:
    """
    该类用于处理范围操作，支持添加、查询和移除范围。
    """

    def __init__(self):
        """
        初始化一个空的存储列表 _X 以存储标记点。
        """
        self._X = []

    def addRange(self, left, right):
        """
        添加指定范围内的所有整数。具体逻辑为：在满足条件的位置插入边界值。

        :param left: 范围起始位置
        :param right: 范围结束位置（不包括）
        """
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i % 2 == 0) + [right]*(j % 2 == 0)

    def queryRange(self, left, right):
        """
        查询指定范围内是否有标记。如果在该范围内的标记位置数量为奇数，则认为有标记。

        :param left: 范围起始位置
        :param right: 范围结束位置（不包括）
        :return: 如果范围内包含标记点返回 True，否则 False。
        """
        i, j = br(self._X, left), bl(self._X, right)
        return i == j and i % 2 == 1

    def removeRange(self, left, right):
        """
        移除指定范围内的所有整数。具体逻辑为：在满足条件的位置插入边界值。

        :param left: 范围起始位置
        :param right: 范围结束位置（不包括）
        """
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i % 2 == 1) + [right]*(j % 2 == 1)



from bisect import bisect_left as bl, bisect_right as br

class RangeModule:
    """
    该类用于处理范围操作，支持添加、查询和移除范围。
    """

    def __init__(self):
        """
        初始化一个空的存储列表 _X 以存储标记点。
        """
        self._X = []

    def addRange(self, left, right):
        """
        添加指定范围内的所有整数。具体逻辑为：在满足条件的位置插入边界值。

        :param left: 范围起始位置
        :param right: 范围结束位置（不包括）
        """
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i % 2 == 0) + [right]*(j % 2 == 0)

    def queryRange(self, left, right):
        """
        查询指定范围内是否有标记。如果在该范围内的标记位置数量为奇数，则认为有标记。

        :param left: 范围起始位置
        :param right: 范围结束位置（不包括）
        :return: 如果范围内包含标记点返回 True，否则 False。
        """
        i, j = br(self._X, left), bl(self._X, right)
        return i == j and i % 2 == 1

    def removeRange(self, left, right):
        """
        移除指定范围内的所有整数。具体逻辑为：在满足条件的位置插入边界值。

        :param left: 范围起始位置
        :param right: 范围结束位置（不包括）
        """
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i % 2 == 1) + [right]*(j % 2 == 1)
