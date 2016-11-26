##1

r = int(input("Radius?"))
S = 3.14*(r**2)
print('Area:', S)

print()
##2

x = int(input("Enter the temperature in Celsius? "))
y = x*9/5+32
print(x," C degree = ",y," F degree ")

print()
##3

x = int(input("How many B bacterias are there? "))
y = int(input("How much time will we wait? "))
z = x*(2**(y//2))

print("after ",y," minutes, it have ",z," bacterias")

print()
##4      

f1=0
f2=1
month=0
for i in range(5):#do (like pascal)
      
      f=f1+f2
      month +=1
      print("Month",month,":",f,"pair(s) of rabbits")
      f1=f2
      f2=f       

print("The number of rabbits after",4,"months are:",f)
