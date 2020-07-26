
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        ### Method 1. Recursively
        if N == 1:
            return 0
        if K % 2 == 0:
            if self.kthGrammar(N-1, K//2) == 0:
                return 1
            else:
                return 0
        else:
            return self.kthGrammar(N-1, (K+1)//2)
        ### Method 2
        # Observation:
        # Output value is decided by the number of 1s in binary representation of (K-1)
        # If binary representation of K-1 has odd 1s, then output value is 1
        # If binary representation of K-1 has even 1s, then output value is 0
        return bin(K-1).count('1') % 2

