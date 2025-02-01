
class Solution:
    # Python 解决方案类

    def generateAbbreviations(self, word: str) -> List[str]:
        # 给定单词生成所有可能的缩写形式
        l, res = len(word), []  # 记录单词长度，初始化结果列表
        
        def dfs(s: str, i: int):
            # 深度优先搜索函数，s是当前构建的字符串，i是当前处理到的位置索引
            if i == l:
                res.append(s)  # 到达单词末尾，将当前构造的结果加入结果列表中
            else:
                dfs(s + word[i], i + 1)  # 继续处理下一个字符
                if not s or s[-1] > "9":  # 当前构建字符串为空或最后一个字符不是数字时
                    for j in range(i + 1, l + 1):
                        dfs(s + str(j - i), j)  # 尝试将字符数加入结果中

        dfs("", 0)  # 初始调用深度优先搜索，空字符串从索引0开始
        return res  # 返回所有可能的缩写形式
