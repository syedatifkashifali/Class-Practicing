#Example 1
import math#including external file which contain pre-defined function related to mathematics
x = math.sqrt(64) #math is the method and sqrt is the function
print(x)

#Example 2
import math#including external file which contain pre-defined function related to mathematics
x = math.ceil(1.4)#calling ceil function from math method
y = math.floor(1.4)#calling floor function from math method
print(x)#printing x
print(y)#printing y

#Example 3
import math#including external file which contain pre-defined function related to mathematics
x = math.pi#calling value of pie from math method
print(x)#printing pi value in x

#Example 4
import datetime#including external file which contain pre-defined function related to date and time
x = datetime.datetime.now()#used to get the current date and time
print(x)

#Example 5
import datetime#including external file which contain pre-defined function related to date and time
x = datetime.datetime(2019, 6, 1)#can put own date and time to display
print(x)

#Example 6
import datetime#including external file which contain pre-defined function related to date and time
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%C"))
