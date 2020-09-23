import random
class Animal:
     def bigLion(self):
          w=random.randint(100,200)
          print(w)
          print("Big Lion Roars")
     def smallLion(self):
         print("Small Lion is knownas Calf and it weighs less than a lion")
class Lion(Animal):
    print("Inherits Animal")
A=Animal()
L=Lion()
L.bigLion()
L.smallLion()