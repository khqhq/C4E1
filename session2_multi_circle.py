#4: Multi-circles

from turtle import *
color('green')

step = ["1","2","3","4","5","6"]

for i in step:
    circle(100)
    lt(60)
    if i == "6":
        break
