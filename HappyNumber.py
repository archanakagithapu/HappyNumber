'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares
of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1'''
def isHappy():
    n = int(input("Enter a number: "))
    L = []
    while n != 1 and n not in L:
        L.append(n)
        sum = 0
        while n > 0:
            digit = n % 10
            sum = sum + digit * digit
            n = n // 10
        n = sum
    return n == 1
print(isHappy())










class Solution:
    def ishappy(self, n: int) -> bool:
        hashset = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in hashset:
                return False
            hashset.add(n)
        return True
solution = Solution()
n = int(input())
print( solution.ishappy(n))
