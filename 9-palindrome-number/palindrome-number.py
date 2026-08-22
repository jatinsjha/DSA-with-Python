class Solution(object):
    def isPalindrome(self, x):
        self.x = x
        z = x
        y = ''
        if x == 0:
            return True
        elif x < 0:
            return False
        else:
            while x > 0:
                temp = x % 10
                y = y + str(temp)
                x = x // 10
            y = int(y)
            if z == y:
                return True
            else:
                return False
        