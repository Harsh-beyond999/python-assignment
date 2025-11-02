# WAP to Print the Area of circle
from math import pi
try:
    r =float(input("Enter the radius of circle: "))
    a = pi*(r**2)
    print("Area of the circle is: ",a)
except ValueError:
    print("Enter a valid numeric radius.")     
