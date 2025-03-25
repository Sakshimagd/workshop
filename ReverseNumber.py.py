#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def reverse_number(n):
    reversed_n=0
    while n>0:
        digit=n%10
        reversed_n=reversed_n*10+digit
        n//10
    return reversed_n
num=int(input("Enter the Number: "))
print("Reversed Number: ",reversed_number(num))


# In[ ]:


def reverse_number(n):
    return int(str(n)[::-1])
num=int(input("Enter the Number: "))
print("Reversed Number: ",reversed_number(num))


# In[ ]:




