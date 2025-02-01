
class NumArray:
    # 初始化树状数组，传入一个整数列表nums
    def __init__(self, nums):
        if nums:  # 如果输入的nums不为空
            self.n = len(nums)
            self.tree = [0] * (2 * (2 ** int(math.ceil(math.log(self.n, 2)))) - 1)  # 初始化树状数组，大小为4*n-1

            def dfs(node, s, e):
                # 如果是叶子节点，则直接赋值
                if s == e: self.tree[node] = nums[s]
                else:
                    m = (s + e) // 2  # 找到中间节点
                    dfs(2 * node + 1, s, m)  # 递归左子树
                    dfs(2 * node + 2, m + 1, e)  # 递归右子树
                    self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]  # 更新当前节点值

            dfs(0, 0, self.n - 1)  # 从根节点开始构建

    def update(self, i, val):
        # 更新树状数组中索引i的值为val
        def dfs(node, s, e, idx, val):
            if s == e: self.tree[node] = val  # 如果是叶子节点，直接更新
            else:
                m = (s + e) // 2  # 找到中间节点
                if s <= idx <= m:  # 在左子树中递归查找
                    dfs(2 * node + 1, s, m, idx, val)
                else:  # 在右子树中递归查找
                    dfs(2 * node + 2, m + 1, e, idx, val)
                self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]  # 更新当前节点值

        dfs(0, 0, self.n - 1, i, val)  # 从根节点开始更新

    def sumRange(self, i, j):
        # 计算索引i到j的区间和
        def dfs(node, s, e, l, r):
            if r < s or l > e: return 0  # 如果区间为空，则返回0
            if l <= s and e <= r: return self.tree[node]  # 如果当前节点完全在查询范围内，直接返回其值
            m = (s + e) // 2  # 找到中间节点
            return dfs(2 * node + 1, s, m, l, r) + dfs(2 * node + 2, m + 1, e, l, r)  # 分别递归查询左右子树的和

        return dfs(0, 0, self.n - 1, i, j)  # 从根节点开始计算区间和
