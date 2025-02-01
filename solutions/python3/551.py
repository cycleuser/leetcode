
class Solution:
    # 检查学生成绩记录是否合格
    def checkRecord(self, s):
        """
        :type s: str  # 输入字符串s，表示学生的出勤记录
        :rtype: bool   # 返回布尔值，True表示合格，False表示不合格
        """

        # 如果s中包含"LLL"或者A的数量超过1次，则返回False
        return False if "LLL" in s or s.count("A") > 1 else True
