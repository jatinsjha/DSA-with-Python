from math import sqrt
class Solution:
    def countFactors (self, n):
        self.n = n
        count = 0
        for i in range(1,int(sqrt(n))+ 1):
            if n % i == 0:
                count = count + 1
                if n // i != i:
                    count = count + 1
        return count
        
        