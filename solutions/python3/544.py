
class Solution:
    # 定义一个类用于解决比赛配对问题

    def findContestMatch(self, n: int) -> str:
        # 初始化参赛选手编号列表，str(i)将数字转换为字符串形式
        arr = [str(i) for i in range(1, n + 1)]
        
        # 当数组长度大于1时继续循环
        while len(arr) > 1:
            # 对于每个配对，生成新的格式并替换原列表中的对应位置
            arr = ["(" + arr[i] + "," + arr[len(arr) - 1 - i] + ")" for i in range(len(arr) // 2)]
        
        # 最终返回数组拼接后的字符串结果
        return ",".join(arr)
