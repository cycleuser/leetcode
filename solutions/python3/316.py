
class Solution:
    # 定义一个类来解决移除重复字符的问题

    def removeDuplicateLetters(self, s: str) -> str:
        # 创建一个字典，记录每个字符最后出现的位置
        rindex = {c: i for i, c in enumerate(s)}

        result = ''
        # 遍历字符串中的每一个字符
        for i, c in enumerate(s):
            if c not in result:
                # 如果当前字符不在结果中，则需要判断是否可以加入结果中
                while result and c < result[-1] and i < rindex[result[-1]]:
                    result = result[:-1]
                # 将符合条件的字符添加到结果中
                result += c
        # 返回最终的结果
        return result
