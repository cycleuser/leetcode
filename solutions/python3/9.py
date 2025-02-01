
class Solution:
    # 判断一个整数是否为回文数
    def isPalindrome(self, x: int) -> bool:
        # 将整数转换为字符串，并与反转后的字符串比较
        return str(x) == str(x)[::-1]
