class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x<0:
            return False
        digits = []
        while x > 0:
            x, digit = divmod(x, 10)
            digits.append(digit)
        for i in range(len(digits)):
            if digits[i] != digits[len(digits)-i-1]:
                return False
        return True
    
    def isStringPalindrome(self, x):
        if x<0:
            return False
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x)-i-1]:
                return False
        return True
    
    def isFastPalindrome(self, x):
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10
