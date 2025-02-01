
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 检查剩余数据是否足够
        def rest(i):
            """Check if there are enough remaining bytes."""
            if len(data) < i:
                return False
            for _ in range(i):
                if not data.pop().startswith("10"):
                    return False
            return True

        # 将整数转换为8位二进制字符串并反转列表方便从高位开始处理
        data, byte = [str(bin(seq)[2:].zfill(8)) for seq in data[::-1]], None
        
        while data:
            seq = data.pop()
            
            # 单字节情况：以'0'开头的二进制串直接跳过
            if seq.startswith("0"):
                continue
            
            # 两字节序列：前缀为"110"
            elif seq.startswith("110"):
                if not rest(1):
                    return False
                
            # 三字节序列：前缀为"1110"
            elif seq.startswith("1110"):
                if not rest(2):
                    return False
            
            # 四字节序列：前缀为"11110"
            elif seq.startswith("11110"):
                if not rest(3):
                    return False
            
            else:
                return False
        
        return True
