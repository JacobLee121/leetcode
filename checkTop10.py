import sys
sys.path.append(r'D:\Users\LiXinqiang\PycharmProjects\LeetcodeEasy\'')
from MaxDeptofBinaryTree import RevStr
from MaxDeptofBinaryTree import SingleNumber1
from MaxDeptofBinaryTree import SoluMovZeroe

from MaxDeptofBinaryTree import SoulutionFizz

####fizz###########
a = SoulutionFizz()
aa = a.fizzBuzz(15)
print(aa)
k=17
for i in range(k):
    kk = a.fizzBuzz(i)
    print(kk)
print("End Fizz")

b = RevStr()
s="Hello."
# s = "a."
bb = b.reverseString(s)
print(s,bb)
print("done!")
#########################
c = SingleNumber1()
l= [1,1,2,3,3,2,"g"]
cc = c.singelNumber(l)
print(cc)
############
d = SoluMovZeroe()
l2 = [0,3,0,5]
dd = d.moveZeroes(l2)
print(dd)
