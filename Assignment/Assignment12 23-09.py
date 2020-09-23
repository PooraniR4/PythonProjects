roar=1
class Animal:
     def bigLion(self):
         for i in roar:
             i=i+1
             print(i)
         print("Lion Roars")
     def smallLion(self):
         print("It weighs less than a lion")
class Lion(Animal):
    print("Inherits Animal")

L=Lion()
L.bigLion()
L.smallLion()