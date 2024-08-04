#!/usr/bin/env python
# coding: utf-8

# In[26]:


#program for codsoft, project : basic arithmatic calculator.
num1= float(input("enter the first number:"))
num2= float(input("enter the second number:"))
operation= str( input("enter the operation that you want to perform:"))
if operation =="+":
    result=(num1+num2)
    print(num1,"+",num2,"=",result)
elif operation =="-":
    result=(num1-num2)
    print(num1,"-",num2,"=",result)
elif operation =="/":
    result=(num1/num2)
    print(num1,"/",num2,"=",result)
elif operation =="*":
    result=(num1*num2)
    print(num1,"*",num2,"=",result)
elif operation =="%":
    result=(num1%num2)
    print(num1,"%",num2,"=",result)
elif operation =="//":
    result=(num1//num2)
    print(num1,"//",num2,"=",result)
elif operation =="**":
    result=(num1**num2)
    print(num1,"**",num2,"=",result)
else :
                print("wrong operator")


# In[ ]:





# In[ ]:




