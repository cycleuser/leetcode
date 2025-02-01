
class Solution:
    # 判断给定整数N是否为混淆数字，即反转后映射的数字与原数字不同且不是合法数字
    def confusingNumber(self, N: int) -> bool:
        # 反转字符串并替换字符：0->0，1->1，9->6，8->8，6->9，其它字符（#）表示非法数字
        ret = ''.join("01####9#86"[int(n)] for n in str(N)[::-1])
        
        # 检查替换后的字符串是否包含非法字符且与原字符串不同
        return '#' not in ret and ret != str(N)
