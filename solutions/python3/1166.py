
class FileSystem:

    def __init__(self):
        # 初始化文件系统，根目录的值设为-1
        self.d = {"" : -1}

    def create(self, path: str, value: int) -> bool:
        # 获取路径的父路径
        parent = path[:path.rfind('/')]
        # 如果存在父路径且当前路径不在字典中，则创建该路径并赋值
        if parent in self.d and path not in self.d:
            self.d[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        # 根据路径获取对应的值，不存在则返回-1
        return self.d.get(path, -1)
