
class Solution:
    # 定义一个类用于解决数组按奇偶性排序的问题
    
    def sortArrayByParity(self, A):
        # 对输入的列表A进行操作，返回一个新的列表，其中偶数位于奇数之前
        
        # 使用列表推导式分两部分构建新列表：首先筛选出所有偶数元素
        even_nums = [a for a in A if not a % 2]
        
        # 然后筛选出所有奇数元素
        odd_nums = [a for a in A if a % 2]
        
        # 将两部分合并，即先偶数再奇数
        return even_nums + odd_nums
