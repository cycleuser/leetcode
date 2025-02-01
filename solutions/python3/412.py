
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        :param n: 输入的整数n，表示需要生成FizzBuzz序列的长度。
        :return: 返回一个包含字符串元素的列表，按照规则生成FizzBuzz序列。
        """
        result = []  # 使用更通用的名字result代替num
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
