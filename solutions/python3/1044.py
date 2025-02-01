
from functools import reduce

# Solution class to find the longest duplicate substring in a given string
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # Convert each character in S to its corresponding integer value (0-25)
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        # Function to test if a substring of length L is duplicated
        def test(L):
            # Calculate the base power needed for hashing
            p = pow(26, L, mod)
            # Hash value of the first L characters
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                # Update hash value as we move one character forward
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
            return None

        # Binary search for the longest duplicated substring length
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1

        # Return the longest duplicated substring found
        return S[res:res + lo]
