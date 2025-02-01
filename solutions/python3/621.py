
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        计算最少需要的空闲时间单位以确保每个任务之间至少有n个空闲时间单位。
        
        :param tasks: 需要执行的任务列表，形式为字符串
        :param n: 两个相同任务之间的最小间隔数（不包含当前任务）
        :return: 最少需要的空闲时间单位数量
        """
        from collections import Counter

        # 统计每个任务出现的次数并排序
        cnt = sorted(Counter(tasks).values())
        
        # 计算最大频率的任务的数量，并计算初始空闲槽数
        idles = (cnt[-1] - 1) * n
        
        # 减去最小间隔中可以利用的最大空闲时间
        for i in range(len(cnt) - 1):
            idles -= min(cnt[i], cnt[-1] - 1)
        
        # 返回需要的空闲时间单位数量，考虑边界情况
        return (idles > 0 and idles + len(tasks)) or len(tasks)
