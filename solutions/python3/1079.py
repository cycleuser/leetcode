
class Solution:
    # 中文注释：定义一个名为Solution的类，包含numTilePossibilities方法用于计算给定瓷砖组合的所有可能排列数量。
    # 英文注释: Define a class named Solution with the method numTilePossibilities to calculate the number of possible permutations of given tiles.
    
    def numTilePossibilities(self, tiles: str) -> int:
        # 中文注释：使用itertools.permutations生成给定字符串tiles的所有可能排列组合，并计算长度大于0的组合数量。
        # 英文注释: Use itertools.permutations to generate all possible permutations of the given string tiles and calculate the count of non-empty combinations.
        
        return sum(len(set(itertools.permutations(tiles, i))) for i in range(1, len(tiles) + 1))
