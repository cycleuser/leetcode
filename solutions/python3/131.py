
class Solution:
    def partition(self, s):
        """
        中文注释: 
        将字符串s进行分割，使得每个子串都是回文串。
        
        英文注释:
        Partition the string s such that every substring is a palindrome.
        """
        q, n = [[s[0]]], len(s)
        
        for i in range(1, n):
            new = []
            for arr in q:
                cur = arr[-1] + s[i]
                # 中文注释: 
                # 如果当前子串不是最后一个字符，并且当前子串是回文，或者已经是字符串末尾，则继续添加
                # 英文注释:
                # If the current substring is not the last character and it's a palindrome, or if we've reached the end of the string, continue adding.
                if i < n - 1 or cur == cur[::-1]:
                    new.append(arr[:-1] + [cur])
                # 中文注释: 
                # 如果当前子串本身是回文，则可以单独作为一个分割项
                # 英文注释:
                # If the current substring itself is a palindrome, it can be added as a separate partition.
                if arr[-1] == arr[-1][::-1]:
                    new.append(arr + [s[i]])
            q = new
        
        return q
