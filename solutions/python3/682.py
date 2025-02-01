
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """
        计算得分。
        
        参数:
            ops (List[str]): 操作列表，包含数字、'C'（取消最后一个操作）、'D'（双倍上一个操作）和 '+'（上两个操作之和）
            
        返回:
            int: 最终得分
        """
        arr = []  # 存储当前的操作结果
        
        for op in ops:
            # 判断当前操作是数字或者负数
            if op.isdigit() or (op[0] == '-' and len(op) > 1):
                arr.append(int(op))
            elif op == 'C' and arr:  # 取消最后一个操作
                arr.pop()
            elif op == 'D' and arr:  # 双倍上一个操作
                arr.append(arr[-1] * 2)
            elif len(arr) >= 2:  # 上两个操作之和
                arr.append(arr[-1] + arr[-2])
        
        return sum(arr)  # 返回最终得分
