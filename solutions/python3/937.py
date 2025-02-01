
class Solution:
    # 定义一个用于重新排列日志文件的方法
    def reorderLogFiles(self, logs):
        """
        :param logs: 列表，包含字符串形式的日志信息
        :return: 排列后的日志列表

        1. 过滤出以字母开头的行 (letter-logs)
        2. 对这些行按照 " " 后面的内容和前面的部分排序
        3. 然后过滤出以数字开头的行 (digit-logs)
        4. 最后将两个结果合并

        示例:
            输入: ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
            输出: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

        """
        # 过滤出以字母开头的行
        letter_logs = filter(lambda l: l[l.find(" ") + 1].isalpha(), logs)
        # 对这些行按照 " " 后面的内容和前面的部分排序
        sorted_letter_logs = sorted(letter_logs, key=lambda x: (x[x.find(" "):], x[:x.find(" ")]))
        
        # 过滤出以数字开头的行
        digit_logs = filter(lambda l: l[l.find(" ") + 1].isdigit(), logs)
        
        # 合并两个结果列表
        return sorted_letter_logs + list(digit_logs)
