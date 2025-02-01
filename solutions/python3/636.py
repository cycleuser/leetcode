
class Solution:
    # 定义一个类来解决exclusive时间的问题

    def exclusiveTime(self, n: int, logs: list) -> list:
        # 初始化结果列表和栈
        res = [0] * n
        stack = []

        for log in logs:
            # 解析日志字符串
            log_info = log.split(":")

            if log_info[1] == "start":
                # 开始任务，记录开始时间和任务ID入栈
                stack.append([int(log_info[2]), 0])
            else:
                # 结束任务，计算执行时间并更新结果列表
                start_time, prev_exec_time = stack.pop()
                duration = int(log_info[2]) - start_time + 1

                # 更新当前任务的执行时间
                res[int(log_info[0])] += duration - prev_exec_time

                if stack:
                    # 如果栈不为空，将子任务的执行时间累加到父任务上
                    stack[-1][1] += duration
        
        return res
