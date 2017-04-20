# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        leftChildHeight = self.maxDepth(root.left)
        rightChildHeight = self.maxDepth(root.right)
        return max(leftChildHeight, rightChildHeight) +1
class SoulutionFizz(object):
    def fizzBuzz(self,n):
        '''
        :type n:int
        :rtype: List[str]
        :param n: 
        :return: 
        '''
        result = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 ==0:
                result.append("FizzBuzz")
            elif i%3 == 0:
                result.append("Fizz")
            elif i%5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
class RevStr(object):
    def reverseString(self,s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s =list(s)
        if n%2 == 0:
            nn = int(n/2)
            for i in range(nn-1):
                temp = s[i]
                s[i] = s[n-1-i]
                s[n-1-i] = temp
        else:
            nn = int((n-1)/2)
            for i in range(nn-1):
                temp = s[i]
                s[i] = s[n-1-i]
                s[n-1-i] = temp
        return "".join(s)#用“”中的字符吧list中的字符连城一个新的字符串

class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
class SingleNumber1(object):
    def singelNumber(self,nums):
        """
        Given an array of integers, every element appears twice except for one. Find that single one.
        nums list[int]
        rtype: int
        :param nums: 
        :return: 
        """
        dic = {}
        for data in nums:
            dic[data] = dic.get(data,0)+1
        for key, value in dic.items():
            if value == 1:
                return key
        return  key
class SoluMovZeroe(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i] == 0:
                while i < n:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i +=1
            return nums
        return nums