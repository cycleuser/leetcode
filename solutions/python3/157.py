
class Solution:
    # 读取指定数量的字符到buf中
    def read(self, buf, n):
        idx = 0
        # 不断循环直到读取完所需字符或缓冲区为空
        while True:
            # 一次性读取4个字符到临时缓存buf4中
            buf4 = [""] * 4
            curr = min(read4(buf4), n - idx)
            # 将有效字符逐个复制到目标buf中并更新索引idx
            for i in range(curr):
                buf[idx] = buf4[i]
                idx += 1
            
            # 如果当前读取的字符不足4个或已达到所需数量，返回实际读取的数量
            if curr != 4 or idx == n:
                return idx
