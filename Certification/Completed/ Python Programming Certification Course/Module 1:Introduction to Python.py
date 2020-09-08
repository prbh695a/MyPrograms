#1.Write a program which will find factors of given number and find whether the factor is even or odd.
number = 32
i = 2
factors = []
x = number
while (1):
    while x % i == 0:
        factors.append(i)
        x = x / i
    i = i + 1
    if x == 1:
        break

print("The Factors for {} are {}".format(number, factors))
if len(factors) % 2 == 0:
    print("Factors are even")
else:
    print("Factors are odd")

#2.Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
string="my nanny is great and my mom is awesome"
seq=string.split(" ")
seq.sort()
print(seq)

#3.Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
def checkdigit(num):
    if num%2==0 or num==0:
        return 0
    else:
        return 1
finalist=[]
for i in range(1000,3001):
    j=int(i)
    flag=0

    while(j>0):
        rem=j%10
        if(checkdigit(rem)==1):
            flag=1
            break
        j=j//10
    if(flag==0):
        finalist.append(i)

print(finalist)

#4.Write a program that accepts a sentence and calculate the number of letters and digits.
val="Python0325"
letter=0
digit=0
for i in val:
    if i.isdigit():
        digit=digit+1
    if i.isalpha():
        letter=letter+1

print("LETTER",letter)
print("DIGITS",digit)

#5.Design a code which will find the given number is Palindrome number or not.
val="122"
rval=val[::-1]
if(val==rval):
    print("Its a palindrome")
else:
    print("Not a palindrome")