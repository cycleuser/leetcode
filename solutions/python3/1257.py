
class Solution:
    # 寻找两个区域中的最小共同祖先

    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        # 构建从子区域指向父区域的映射
        nex = {r: region[0] for region in regions for r in region[1:]}

        # 初始化起始地区
        r1, r2 = region1, region2

        # 循环直到找到共同祖先
        while r1 != r2:
            r1 = nex[r1] if r1 in nex else region2  # 如果r1没有父节点，则移动到region2所在的分支
            r2 = nex[r2] if r2 in nex else region1  # 同上

        return r1  # 返回共同祖先
