
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]  # 输入列表nums，其中包含整数
        :type k: int           # 整数值k
        :rtype: int            # 返回满足条件的pair数量
        """
        
        dic, pair = {}, 0  # 初始化字典dic和计数器pair
        
        for num in nums:
            # 检查num-k或num+k在字典中是否存在，同时考虑k==0的情况
            if (num - k in dic or num + k in dic) and \
               (not num in dic or (k == 0 and dic[num] == 1)) and k >= 0:
                
                # 当k不为零且num-k在字典中时，增加pair计数
                if num - k in dic and k != 0: 
                    pair += 1
                    
                # 当num+k在字典中时，增加pair计数
                if num + k in dic: 
                    pair += 1
                    
                # 如果当前数字已在字典中，则只需更新其出现次数
                if num in dic: 
                    dic[num] += 1
                    continue
            
            # 如果当前数字不在字典中，则将其加入字典并设置初始计数为1
            if num not in dic:
                dic[num] = 1
        
        return pair  # 返回满足条件的pair数量
