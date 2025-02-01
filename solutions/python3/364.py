
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    # 计算最大深度
    def depthSumInverse(self, nestedList):
        # 深度优先搜索，计算每个元素的最大深度
        def dfs(obj, d):
            return obj.isInteger() and d or max((dfs(item, d + 1) for item in obj.getList()), default = 0)
        
        # 深度优先搜索，计算加权和
        def dfs2(obj, d):
            return obj.isInteger() and d * obj.getInteger() or sum(dfs2(item, d - 1) for item in obj.getList())
        
        # 计算最大深度
        mx = max((dfs(item, 1) for item in nestedList), default = 0)
        
        # 如果存在最大深度，则计算加权和，否则返回0
        return mx and sum(dfs2(item, mx) for item in nestedList) or 0
