
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """
        判断字符串A和B是否可以通过交换A中的两个字符得到B。
        
        :param A: 第一个字符串
        :param B: 第二个字符串
        :return: 如果可以通过交换A中的两个字符得到B则返回True，否则返回False
        """
        if len(A) != len(B):
            return False  # 如果长度不等，则不能通过交换字符使两者相等

        # 找出A和B中不同的字符对，并检查A中是否有重复字符
        diff_pairs = [(a, b) for i, (a, b) in enumerate(zip(A, B)) if a != b]
        has_duplicate = len(set(A)) < len(A)

        # 只能通过交换两个不同位置的字符得到B，且这两位字符必须互换才能使A变成B
        return len(diff_pairs) == 2 and diff_pairs[0] == diff_pairs[1][::-1] or (not diff_pairs and has_duplicate)
