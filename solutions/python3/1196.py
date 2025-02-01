
class Solution:
    # 定义一个方法，计算最多可以装入多少个苹果
    def maxNumberOfApples(self, arr: List[int]) -> int:
        # 对苹果重量列表进行排序
        sorted_arr = sorted(arr)
        
        # 使用 accumulate 函数生成累加和的列表
        cum_sum = list(itertools.accumulate(sorted_arr))
        
        # 使用 bisect 函数在累加和列表中查找第一个大于5000的位置索引，即最多可以装入多少个苹果
        return bisect.bisect(cum_sum, 5000)
