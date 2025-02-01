
class Solution:
    # 定义一个名为Solution的类，用于处理进程杀掉逻辑

    def killProcess(self, pid, ppid, kill):
        # 初始化索引字典和结果列表
        indexes, res = collections.defaultdict(list), [kill]
        
        # 遍历ppid数组，填充索引字典
        for i, p in enumerate(ppid):
            indexes[p].append(i)
            
        # 使用栈进行深度优先搜索遍历
        stack = [kill]
        while stack:
            # 从栈中弹出一个元素
            current_pid = stack.pop()
            # 将当前节点的所有子节点添加到结果列表和栈中
            for i in indexes[current_pid]:
                res.append(pid[i])
                stack.append(pid[i])
        
        return res  # 返回最终的结果列表
