
class Solution:
    # 定义一个类用于求解格雷码

    def grayCode(self, n: int) -> List[int]:
        # 初始化结果列表，包含0作为起点
        results = [0]
        
        for i in range(n):
            # 对当前结果列表进行逆序操作，并与当前位的2的幂次相加后添加到结果中
            results += [x + pow(2, i) for x in reversed(results)]
            
        return results  # 返回最终生成的格雷码列表
