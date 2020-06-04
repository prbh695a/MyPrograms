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