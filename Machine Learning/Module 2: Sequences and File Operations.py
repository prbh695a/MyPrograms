#1.What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
#Answer:4


#2.What will be the output?
d ={"john":40, "peter":45}
print(list(d.keys()))
#Answer:john,peter

#3.Write a program to check the validity of password given by user
import re
password="th2isMyFst#"

def checkcriteria(x,check):
    return(re.search(r"(["+check+"])", x))

def detailcondition(x,check):
    if (checkcriteria(password,check) != None):
        print("The password {} contain {}".format(x,check))
        return 0
    else:
        print("The password {} doesnt contain {}".format(x,check))
        return 1

def checklength(x):
    flag=0
    if (len(x)<6):
        print("The password has length smaller than 6 and is not acceptable")
        flag=1
    else:
        print("The password length greater than 6")
        flag=0
    if (len(x)>12):
        print("The password cannot have maximum greater the 12")
        flag=flag+1
    else:
        print("The password have maximum length upto 12")
        flag=flag+0
    return flag

flag=0
for i in ["a-z","0-9","A-Z","$#@"]:
    flag=flag+detailcondition(password,i)
flag=flag+checklength(password)
if (flag>=1):
    print("Please try again, the password doesn't meet minimum criteria")
else:
    print("Congratulations!!!, the password meet minimum criteria")

#4.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9]
for i,j in enumerate(a):
    print("The element at pos{} is {}".format(i,j))

#5.Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes
a = "H1e2l3l4o5w6o7r8l9d"
b=[]
for i in a:
    if(i.isalpha()):
        prev=i
    if(i.isnumeric()):
        b.insert(int(i), prev)
b.append(i)
c = ''.join(map(str, b))
print(c)

#6.Please write a program which accepts a string from console and print it in reverse order
a = "rise to vote sir"
a=a.split(" ")
b=[]
for i in a:
    b.append(i[::-1])
b.reverse()
c = ' '.join(map(str, b))
print(c)

#7.Please write a program which count and print the numbers of each character in a string input by console.
a = "abcdefgabc"
b={}
for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
print(b)

#8.write   a program to make a list whose elements are intersection of the above given lists.
a=set([1,3,6,78,35,55,12])
b=set([12,24,35,24,88,120,155])
print (list(a.intersection(b)))

#9.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved
a=[12,24,35,24,88,120,155,88,120,155]
a.reverse()
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

#10.please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]
a=[12,24,35,24,88,120,155]
for i in a:
    if i==24:
        a.remove(i)
print(a)

#11.please write a program to print the list after removing the 0th,4th,5th numbers
a=[12,24,35,70,88,120,155]
a.pop(0)
a.pop(4-1)
a.pop(5-2)
print(a)

#12.please write a program to print the list after removing delete numbers which are divisible by 5 and 7
a=[12,24,35,70,88,120,155]
for i in a:
    if i%5==0 and i%7==0:
        a.remove(i)
print(a)

import random

#13.Please  write  a  program  to  randomly  generate  a  list  with  5  numbers
b = []
count = 0
while (True):
    i = random.randint(1, 1000)
    if i % 35 == 0:
        b.append(i)
        count = count + 1
    if count == 5:
        break

print(b)

#14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1
count=5
num=1
denom=2
tsum=0
while (num<=count):
    tsum=tsum+num/denom
    num=num+1
    denom=denom+1
print(tsum)

#CaseStudy2:
import re
from cryptography.fernet import Fernet

key = Fernet.generate_key()
Reference_ID = "12345ofjojsf"
check = "a-z0-9A-Z"
y = re.search(r"([" + check + "]*)", Reference_ID)
if (len(y.group(0)) != 12):
    print("Then length of Reference_ID should be 12 and it should only contain number and alphabet")
else:
    fernet = Fernet(key)
    encrypted = fernet.encrypt(Reference_ID.encode())
    print(encrypted)


