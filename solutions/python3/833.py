
class Solution:
    # 定义一个解决方案类

    def findReplaceString(self, s: str, indexes: list[int], sources: list[str], targets: list[str]) -> str:
        # 初始化结果字符串，字典用于存储索引与替换信息的对应关系，初始化指针j
        res, dic, j = "", {}, 0

        # 遍历所有需要替换的内容，构建字典dic保存起始位置和对应的源串及目标串
        for i in range(len(sources)):
            if s.find(sources[i], indexes[i]) == indexes[i]:
                dic[indexes[i]] = (sources[i], targets[i])

        # 通过指针j遍历字符串s，根据字典dic进行替换操作
        while j < len(s):
            res += j in dic and dic[j][1] or s[j]
            j += j in dic and len(dic[j][0]) or 1

        return res  # 返回最终的结果字符串
