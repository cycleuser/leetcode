
class Solution:
    # 定义解决方案类

    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> List[int]:
        # 初始化结果数组和已使用车辆集合
        ans, used = [-1] * len(W), set()
        
        # 对每个工人与每辆自行车的距离进行排序
        for d, w, b in sorted([abs(W[i][0] - B[j][0]) + abs(W[i][1] - B[j][1]), i, j] for i in range(len(W)) for j in range(len(B))):
            # 如果当前工人未分配且自行车未被使用，则进行分配
            if ans[w] == -1 and b not in used:
                ans[w] = b
                used.add(b)
            
            # 若所有工人已成功分配，提前结束循环
            if len(used) == len(ans):
                break
        
        return ans  # 返回结果数组
