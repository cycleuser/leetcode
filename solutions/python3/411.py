
class Solution(object):
    
    # 提取数字，支持多位数
    def extract_number(self, j: int, abbr: str, M: int) -> (int, int):
        """
        :param j: 当前索引
        :param abbr: 简写字符串
        :param M: abbr 的长度
        :return: 数字和更新后的索引
        """
        num = 0
        while j < M and abbr[j].isdigit():
            num, j = num * 10 + int(abbr[j]), j + 1
        return num, j
    
    # 验证简写是否有效
    def valid(self, word: str, abbr: str) -> bool:
        """
        :param word: 目标单词
        :param abbr: 简写字符串
        :return: 是否为有效的简写
        """
        i, j, N, M = 0, 0, len(word), len(abbr)
        while i < N and j < M:
            if abbr[j].isalpha() and abbr[j] != word[i]:
                return False
            elif abbr[j].isalpha() and abbr[j] == word[i]:
                i, j = i + 1, j + 1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num, j = self.extract_number(j, abbr, M)
                i += num
        return (i == N and j == M)

    # 处理生成的简写
    def process_solution(self, so_far: list) -> (str, int):
        """
        :param so_far: 当前构建的简写列表
        :return: 构建的字符串和长度
        """
        csofar, i, cnt = [], 0, 0
        while i < len(so_far):
            if so_far[i].isalpha():
                csofar.append(so_far[i])
                i, cnt = i + 1, cnt + 1
            else:
                num = 0
                while i < len(so_far) and so_far[i].isdigit():
                    num, i = num + 1, i + 1
                cnt += 1
                csofar.append(str(num))
        return "".join(csofar), cnt

    # 检查简写是否在字典中有效
    def test(self, abbr: str, dictionary: list) -> bool:
        """
        :param abbr: 简写字符串
        :param dictionary: 字典列表
        :return: 是否为有效简写
        """
        for wrd in dictionary:
            if self.valid(wrd, abbr):
                return False
        return True

    # 辅助函数，递归构建简写
    def helper(self, word: str, so_far: list, i: int, dictionary: list) -> None:
        """
        :param word: 目标单词
        :param so_far: 当前构建的简写列表
        :param i: 当前索引
        :param dictionary: 字典列表
        """
        if i == len(word):
            abbr, cnt = self.process_solution(so_far)
            if cnt < self.result_len and self.test(abbr, dictionary):
                self.result, self.result_len = abbr, cnt
            return
        else:
            so_far.append("1")
            self.helper(word, so_far, i + 1, dictionary)
            so_far.pop()
            so_far.append(word[i])
            self.helper(word, so_far, i + 1, dictionary)
            so_far.pop()

    # 主函数，找到最简缩写
    def minAbbreviation(self, target: str, dictionary: list) -> str:
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """

        # 预处理：过滤掉那些不可能的单词
        filtered_dictionary = []
        for wrd in dictionary:
            if len(wrd) != len(target):
                continue
            filtered_dictionary.append(wrd)
        dictionary = filtered_dictionary
        if len(dictionary) == 0:
            return str(len(target))

        self.result_len = len(target) + 1
        self.result, so_far, i = target, [], 0
        self.helper(target, so_far, i, dictionary)
        return self.result
