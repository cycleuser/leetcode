
class Solution:
    # 定义一个类来解决寻找两个数组最长相同子数组的问题

    def findLength(self, A, B):
        # 在A和B的开始和结束添加特殊字符，方便匹配
        A, res, sub = "X%sX" % "X".join(map(str, A)), 0, "X"
        
        for num in B:
            # 将当前数字追加到子字符串中，并在后面加上特殊字符
            sub += str(num) + "X"
            
            # 如果新的子字符串存在于A中，说明找到了一个匹配的子数组
            if sub in A: 
                res += 1
            
            # 否则，从子字符串中去掉最旧的一个数字，继续寻找
            else:
                sub = sub[sub[1:].index("X") + 1:]
        
        return res  # 返回找到的最长相同子数组的数量

