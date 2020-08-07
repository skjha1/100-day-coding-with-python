#!/usr/bin/env python
# coding: utf-8

# 1. Python program to calculate the hypotenuse of a right angled triangle.

# In[1]:


from math import sqrt 
b= float (input ('base ='))
p= float(input ('Perpendicular ='))

h= sqrt(b**2 + p**2)
print ('Length of hypotenuse is ',h)


# In[2]:


from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )


# In[3]:


import math 
b= float (input ('base ='))
p= float(input ('Perpendicular ='))

h= sqrt(b**2 + p**2)
print ('Length of hypotenuse is ',h)


# 2. Python program to convert the distance (in feet) to inches, yards, and miles.

# In[4]:


distane = float (input ('feet '))
inches = distane*12
yard = distane*0.33333
miles= distane*0.000189394
print (inches)
print (yard)
print (miles)


# In[5]:


d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)


# 3. Python program to convert all units of time into seconds.

# In[6]:


days = int (input ('Days '))*3600*24
hours= int (input ('Hours '))* 3600
minutes = int (input ('Minutes '))*60
seconds = int (input ('Sec'))
time =days+hours+minutes+seconds
print ('The toatal  sec is ', time )


# 4. Python program to convert seconds to day, hour, minutes and seconds

# In[8]:


time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


# 5. Calculate body mass index

# In[11]:


h= float(input ())
w= float(input ())
bmi= (w/(h*h))
print('body mass index is ',bmi)


# 6. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

# In[15]:


kpa = float (input ())
psi= kpa /6.8947
mmhg=kpa * 760 /101.325
atm= kpa/101.325
print ('the pressure in pound per sq inch : %.2f '%(psi))
print ('the pressure in milimeter of mercury %.2f'%(mmhg))
print ('the atmosphere pressur %.2f'%(atm))


# In[19]:


num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


# In[ ]:




