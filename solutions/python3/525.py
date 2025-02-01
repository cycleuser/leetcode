    
    class Solution:
        # 定义一个类，包含一个寻找最长有效括号子串的方法
    
        def findMaxLength(self, nums: List[int]) -> int:
            # 初始化索引字典、结果变量和当前计数值
            ind, res, sm = {0: -1}, 0, 0
            
            # 遍历输入列表，计算前缀和，并更新结果和索引映射
            for i, num in enumerate(nums):
                sm += num and 1 or -1  # 更新当前计数值：遇到1增加1，遇到0减少1
                
                if sm in ind:
                    res = max(res, i - ind[sm])  # 如果当前计数值已存在字典中，则更新最大长度
                else:
                    ind[sm] = i  # 否则将当前计数值及其索引存入字典
            
            return res  # 返回最长有效子串的长度
    