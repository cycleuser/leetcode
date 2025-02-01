
class Solution:
    # 定义一个用于查找重复文件的类

    def findDuplicate(self, paths):
        """
        :param paths: 列表，包含多个路径字符串，每个路径字符串以空格分隔，形式为 "根目录 文件名(内容)"
        :return: 返回所有重复文件的列表
        """

        from collections import defaultdict  # 引入字典默认值处理模块

        dic = defaultdict(list)  # 初始化一个默认值为list的字典用于存储相同内容的文件路径
        for path in paths:
            root, *files = path.split(" ")  # 分割路径字符串，root是根目录，files是一系列文件名(内容)
            for file in files:
                name, content = file.split("(")  # 拆分文件名和内容
                dic[content[:-1]].append(root + "/" + name)  # 去除内容尾部的 ')' 并添加路径到字典中

        return [dic[key] for key in dic if len(dic[key]) > 1]  # 返回所有重复文件列表
