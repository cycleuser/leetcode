
class Solution:
    def rotatedDigits(self, N: int) -> int:
        """
        :type N: int
        :rtype: int
        """
        # 初始化结果计数器
        res = 0
        
        # 遍历范围[1, N]
        for i in range(1, N + 1):
            # 将数字转换为字符串形式
            i_str = str(i)
            tmp_list = []
            check_flag = True
            
            # 遍历每个字符，检查并转换可旋转数字
            for char in i_str:
                if char in ("3", "4", "7"):
                    # 发现不可旋转的数字，设置标志位结束循环
                    check_flag = False
                    break
                elif char in ("0", "1", "8"):
                    # 可保持不变的数字直接加入临时列表
                    tmp_list.append(char)
                elif char == "2":
                    # 旋转2到5
                    tmp_list.append("5")
                elif char == "5":
                    # 旋转5到2
                    tmp_list.append("2")
                elif char == "6":
                    # 旋转6到9
                    tmp_list.append("9")
                elif char == "9":
                    # 旋转9到6
                    tmp_list.append("6")
            
            # 检查转换后与原数字是否不同且没有不可旋转的数字
            if check_flag and i != "".join(tmp_list):
                res += 1
        
        return res
