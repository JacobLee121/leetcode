class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roma = {'M':1000,'D':500,'C':100,'L':10,'V':5,'I':1,'X':50}
        num = 0
        for i in range(0,len(s) - 1):
            if roma[s[i]] < roma[s[i+1]]:

                num -= roma[s[i]]
            else:
                num += roma[s[i]]
        return num + roma[s[-1]]
