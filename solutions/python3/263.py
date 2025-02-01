    
    class Solution:
        def isUgly(self, num):
            """
            :type num: int
            :rtype: bool
            
            判断一个数是否只有质因数2、3或5，如果是返回True，否则返回False。
            英文：Determine if a number has only prime factors 2, 3, or 5. Return True if so, otherwise False.
            """
            while num > 1:
                # 如果num不能被2、3或5整除，则不是丑数
                if all(num % i != 0 for i in [2, 3, 5]):
                    return False
                # 否则，去除一个最小的质因数（2, 3, 或者5）
                else:
                    num /= min([i for i in [2, 3, 5] if num % i == 0])
            return num == 1
    