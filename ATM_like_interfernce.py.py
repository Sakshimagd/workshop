#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("welcome!!")
Balance=123456;
print("menu>=\n1.check balance\n2.Deposite Money\n3.Withdraw Money\n4.Exit the system")
ch=int(input("Enter your choice"))
if ch==1:  
    print("Your balance is",Balance)
elif ch==2:
        Amount=int(input("enter your amount: "))
        print("current balance is ",Balance+Amount)
elif ch==3:
        money=int(input("Enter withdrawing money: "))
        print("current balance is ",Balance-money)
else: 
      print("Exit the system")


# In[ ]:




