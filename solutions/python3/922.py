
class Solution:
    # Python 方法：根据奇偶性对数组进行排序
    
    def sortArrayByParityII(self, A):
        # 分离出偶数和奇数列表
        even = [a for a in A if not a % 2]
        odd = [a for a in A if a % 2]

        # 根据索引的奇偶性，交替插入偶数和奇数
        return [even.pop() if i % 2 == 0 else odd.pop() for i in range(len(A))]
