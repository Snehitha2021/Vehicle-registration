import vehicle as mp
import vehicle.bike as ms
import vehicle.car as ms1
from vehicle.bike import btype as ar
from vehicle.car import ctype as ar2
print(mp.main)
#print(mp.mainpackdemo)
print("1 for BIKE,  2 for CAR")
num=int(input("enter a number"))
if num==1:
    print(ms.subpackdemo())
    print("enter 1 for PETROL BIKE, 2 for ELECTRIC BIKE")
    num1=int(input("enter a number"))
    if num1==1:
        print(ar.petrol())
    else:
        print(ar.electric())
else:
    print(ms1.subpackdemo())
    print("enter 1 for PETROL CAR, 2 for ELECTRIC CAR,  3 for DISEL CAR")
    num1 = int(input("enter a number"))
    if num1 == 1:
        print(ar2.petrolc())
    elif num1==2:
        print(ar2.electricc())
    else:
        print(ar2.disel())

