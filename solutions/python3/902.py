
class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        Given a set of digits D and a number N, find how many numbers can be formed with the digits in D that are less than or equal to N.
        
        Args:
            D: A list of unique digits (str).
            N: The target number as a string.
        
        Returns:
            The count of numbers <= N which can be formed using only digits from set D.
        """
        def less(c):
            """
            Count how many digits in the set are smaller than c.
            
            Args:
                c: A single character representing a digit.
                
            Returns:
                The count of digits in D that are smaller than c.
            """
            return len([char for char in D if char < c])
        
        d, cnt, l = len(D), 0, len(str(N))
        # For numbers with fewer digits than N, simply the number of combinations is |D|^digits_length
        for i in range(1, l):
            cnt += d ** i
        
        """
        We need to consider cases where the leading digits match. In such cases,
        we can form a number by adding 'previous valid digits' + (digits less than N[i]) + D ** remaining length.
        """
        for i, c in enumerate(str(N)):
            cnt += less(c) * (d ** (l - i - 1))
            if c not in D: break
            if i == l - 1: cnt += 1
        
        return cnt
