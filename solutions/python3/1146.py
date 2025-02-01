
class SnapshotArray:

    def __init__(self, length: int):
        """
        初始化 SnapshotArray 类。
        
        参数：
        - length：数组长度。
        """
        self.s = 0  # 当前快照序列号
        self.arr = [[[0, 0]] for _ in range(length)]  # 数组初始化，每个位置为一个列表，初始值 [时间戳, 值]

    def set(self, index: int, val: int) -> None:
        """
        设置指定索引在当前快照下的值。
        
        参数：
        - index：要设置的索引。
        - val：要设置的新值。
        """
        if self.s == self.arr[index][-1][0]:  # 检查新值是否与最近一次快照时间戳相同
            self.arr[index][-1][1] = val  # 更新现有列表项
        else:
            self.arr[index].append([self.s, val])  # 添加新列表项

    def snap(self) -> int:
        """
        创建并返回一个新的快照序列号。
        
        返回：
        - 新的快照序列号。
        """
        self.s += 1
        return self.s - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        根据索引和快照ID获取值。
        
        参数：
        - index：要查询的索引。
        - snap_id：目标快照ID。
        
        返回：
        - 目标快照下的值。
        """
        i = bisect.bisect_left(self.arr[index], [snap_id])  # 使用二分查找定位到最接近快照id的位置
        if i < len(self.arr[index]):
            if self.arr[index][i][0] > snap_id:
                i -= 1  # 如果找到位置的值大于目标id，说明实际值在前一个位置
        return self.arr[index][i][1]  # 返回对应快照下的值
