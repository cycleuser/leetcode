
class Solution:
    def totalHammingDistance(self, nums):
        # 初始化一个长度为32的列表ones来存储每个位上1的数量，初始化nums长度变量n和结果变量res
        ones, n, res = [0] * 32, len(nums), 0
        
        # 遍历输入的nums列表中的每一个数字num
        for num in nums:
            # 将数字转换为二进制字符串，并反转该字符串，从最低位开始计算
            for i, c in enumerate(bin(num)[2:][::-1]):
                if c == "1":  # 如果当前位是1，则ones对应索引位置加一
                    ones[i] += 1
        
        # 遍历ones列表中的每个值，累加结果res为每个位上1的数量与0的数量之积
        for one in ones: 
            res += one * (n - one)
        
        return res  # 返回最终的汉明距离总和
