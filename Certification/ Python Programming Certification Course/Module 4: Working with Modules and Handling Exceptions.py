#Case Study I
#1.Write a program to compute the distance current position after sequence of movements
import math
class robot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self, distance):
        self.x = self.x + distance

    def down(self, distance):
        self.x = self.x - distance

    def left(self, distance):
        self.y = self.y + distance

    def right(self, distance):
        self.y = self.y - distance
r = robot(0, 0)
while (True):
    inp = input("Enter the traces(Press n/N to stop)")
    if inp == 'N' or inp == 'n':
        break
    direction = inp.split(" ")[0]
    distance = int(inp.split(" ")[1])
    if "UP" in direction:
        r.up(distance)
    if "DOWN" in direction:
        r.down(distance)
    if "LEFT" in direction:
        r.left(distance)
    if "RIGHT" in direction:
        r.right(distance)

print(math.hypot(r.x, r.y))

#2.Write a program for searching specific data from that list.
data=[1,2,3,4,5,6,7,8,9]
search=44
if search in data:
    print("Data found at position: ",data.index(search)+1)
else:
    print("Data not found")

#3.write a program for such organization to find whether is it dark outside or not.
import datetime
time = datetime.datetime.now()
if((time.hour>7) and (time.hour<18 and time.minute<30)):
   print("Its day")
else:
   print("Its Night")

#4.Write a program to find distancebetween two locations when their latitude and longitudes are given
import math
lat1=math.radians(18.516726)
log1=math.radians(73.856255)
lat2=math.radians(19.076090)
log2=math.radians(72.877426)
r=6371
dlat=lat2-lat2
dlong=log2-log1
'''a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
c = 2 ⋅ atan2( √a, √(1−a) )
d = R ⋅ c'''
def havcalc(delta):
    return math.pow(math.sin(delta/2),2)

a=havcalc(dlat)+math.cos(lat1)*math.cos(lat2)*havcalc(dlong)
c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
d=r*c
print("The distance between two point is: ",d)

#5.Design a software for bank system
balance = 0
oldpassw = "old"
while (-1):
    print("1.Cash Withdraw")
    print("2.Cash credit")
    print("3.Change password")
    print("4.Exit")
    inp = int(input("Enter the option: "))
    if (inp == 4):
        break
    if (inp == 1):
        amount = int(input("Enter the amount to withdraw: "))
        if (amount < balance):
            balance = balance - amount
            print("The current balance is:", balance)
        else:
            print("The current balance is low, cannot withdraw", balance)
    if (inp == 2):
        amount = int(input("Enter the amount to credit: "))
        balance = balance + amount
        print("The current balance is:", balance)
    if (inp == 3):
        passw = input("Enter the old password:")
        if (passw == oldpassw):
            npassw = input("Enter the new password: ")
            oldpassw = npassw
            print("The password has been successfully changed")
        else:
            print("Please enter correct password!!!")

#6. Write a program which will find all such numbers which are divisible by 7
number=[]
for i in range(2000,3201):
    if(i %7 ==0 and i%5!=0):
        number.append(i)
print(number)

#7.Write a program which can compute the factorial of a given numbers. Use recursion to find it.
number=5
def fact(n):
    if(n!=1):
        return(n*fact(n-1))
    else:
        return 1

factorial=fact(number)
print(factorial)

#8.Write a program that calculates and prints the value according to the given formula
import math

def calfor(n):
    num = (2 * 50 * n)
    Q = math.sqrt(num / 30)
    return int(Q)

seq = []
inp = input("Enter the Sequence: ")
x = inp.split(",")
for i in x:
    if (i != ","):
        seq.append(calfor(int(i)))

print(seq)

#9.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array
import numpy as np

X=int(input("Enter the size of rows: "))
Y=int(input("Enter the size of columns: "))
arr=np.zeros((X, Y))
for i in range(0,X):
    for j in range(0,Y):
        arr[i][j]=i*j
print(arr)

#10.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically
words=(input("Enter the sequence of words seperated by comma :"))
print("Before sorting: ",words)
afterSort= ""
for i in sorted(words.split(",")):
    if afterSort == "":
        afterSort=afterSort+i
    else:
        afterSort=afterSort+","+i
print("After Sorting: ",afterSort)

#11.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
print("Enter the sequence of lines:")
inputline=""
outputline=""
while True:
    inputline=input()
    if inputline:
        outputline = outputline+inputline.upper()+"\n"
    else:
        break
print("The sequence after changing case:")
print(outputline)

#12.Write a program that accepts a sequence of whitespace separated words as input and   prints   the   words   after   removing   all   duplicate   words   and   sorting   them alphanumerically.
rawString=input("Enter the string with whitespace :")
removeDup=""
for i in rawString.split(" "):
    if i not in removeDup:
        removeDup= removeDup+i+" "
print("After removing duplicates: ",removeDup)
afterSort=""
for i in sorted(removeDup.split(" ")):
    if afterSort == "":
        afterSort=afterSort+i
    else:
        afterSort=afterSort+" "+i
print("After Sorting: ",afterSort)

#13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.  The numbers that are divisible by 5 are to be printed in a comma separated sequence.
SeqNum=input("Enter the string with whitespace :")
finalSeq=""
for i in SeqNum.split(","):
    if int(i,2)%5 ==0:
        if finalSeq == "":
            finalSeq=finalSeq+i
        else:
            finalSeq=finalSeq+","+i

print(finalSeq)

#14.Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters and lower case letters.
sentence=input("Enter the string : ")
uc=0
lc=0
for i in sentence:
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("UPPER CASE ",uc)
print("LOWER CASE ",lc)

#15.Give example of fsum and sum function of math library.
import math
numbers=[1,2,3,4,5,6,7,8,9,10]
s=sum(numbers)
fs=math.fsum(numbers)
print(s,fs)

#============================================================================================
#Case Study II

import sys

#1.Read file bank-data.csv
file=open("bank-data.csv","r")

#2.Build a set of unique jobs
age=[]
job=[]
maritial=[]
for x in file:
    if "age" not in x:
        i=x.split(",")
        age.append(i[0])
        i[1]=i[1].strip('.')
        job.append(i[1])
        maritial.append(i[2])
ujobs=[]
for i in job:
    if i not in ujobs:
        ujobs.append(i)
print("The unique jobs are",ujobs)

#3.Read the input from command line –profession
#profession=sys.argv[1] #Enable this line for taking command line arguments
profession = "admin"

#4.Check if  profession is in list
if profession.lower() in ujobs:
#5.Print  whether client is eligible
    print("The profession is in the unique set, hence client is eligible")
else:
    print("The profession is not in the unique set, hence client is not eligible")

#1.Compute max and min age for loan eligibility based on data in csv file
#2.Store max and min age in dictionary
agedict={'minage':min(age),'maxage':max(age)}
print("The minimum age for loan eligibilty is :" ,agedict['minage'])
print("The maximum age for loan eligibilty is :" ,agedict['maxage'])

#3.Make the profession check case insensitive
#if profession.lower() in ujobs:
#already case insensitive

#============================================================================================
#Case Study III


import re
from Customer import Customer


class Error(Exception):
    """CustomerNotAllowedException"""
    pass

class CustomerNotAllowedException(Error):
    pass
#1.Read FairDealCustomerData.css
file=open("FairDealCustomerData.csv","r")

#2.Name field contains full name –use regular expression to separate title, first name, last name
def createOrder(x):
    out = re.search(r"(.*),\s(.*)\.\s(.*),([0-9])", x)
    c = Customer()
    c.setLname(out.group(1))
    c.setTitle(out.group(2))
    c.setFname(out.group(3))
    c.setIsblacklisted(out.group(4))
    return c

#3.Store the data in Customer Class
for x in file:
    cust=createOrder(x)
    try:
#4.Create Custom Exception –CustomerNotAllowedException
        if int(cust.isblacklisted) == 1:
#5.Pass a customer to function "createOrder" and throw CustomerNotAllowedException in case of blacklisted value is 1
            raise CustomerNotAllowedException
    except CustomerNotAllowedException:
        print("The customer is not allowed!!!!!!!!!!", cust.__str__())

    print("Order created Successfully for customer",cust.__str__())





