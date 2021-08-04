#!/usr/bin/env python
# coding: utf-8

# 1) After running the following code, what does the variable bacon contain?
# bacon = 22
# 
# bacon + 1

# Ans: After running the folowing code we will get the value of bacon =22
# as when bacon is added with 1 it is not stored anywhere s of which it will not be updated and will remain same
# 

# In[1]:


bacon = 22
bacon+1
print(bacon)


# 2) What should the values of the following two terms be?
# 
# 'spam' + 'spamspam'
# 
# 'spam' * 3

# Ans: Both when executed will return same String value: "spamspamspam".

# In[2]:


#ans
b='spam'+"spamspam"
c="spam"*3
print(b)
print(c)


# 3) How can you tell the difference between break and continue?

# Ans: The diffrence between break and continue is that in a loop when the code needs to be terminated from the loop when a particular value comes then break is used, at that particular iteration that particular loop will be terminated, whereas at a particular value , the need of the code is such that it should skip the following iteration and pass the loop to another iteration, continue is used.
# 
# below are some examples of break and continue.

# In[10]:


#code
for x in range(10):
    print(x)
    if(x==5):
        break
print()
for y in range(10):
    if(y%2==0):
        continue
    print(y)


# 4) In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# Ans: In for loop in python range(10), range(0, 10), and range(0, 10, 1) all means the same, they all initiate from 0 and end at 10 iterating(or increament) 1 everytime. range(10) is sort of short way of writting the other two forms, in range(0,10) 0 means the initial value whereas 10 means the final value( the loop will run from 0 to 9, 10 times it doesn't mean that the final value for this loop will be 10 it will be 10(final value-1)=9), though here the iteration(or increament) isn't defined python takes a default value of 1.
# In range(0,10,1) all values are defined ) being initial, 10 being the final and 1 being the iteration(or increament), increament can be any integer.
# 

# 5) Using a for loop, write a short programme that prints the numbers 1 to 10 Then, using a while loop, create an identical programme that prints the numbers 1 to 10.

# In[1]:


#code
print("using for loop")
for x in range(1,11,1):
    print(x)

print()
print("using while loop")
a=1
while(a<=10):
    print(a)
    a+=1


# 6) Given a number x, determine whether the given number is Armstrong number or not.
# 
# Input : 153
# 
# Output : Yes
# 
# 153 is an Armstrong number.
# 
# 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 = 153

# In[2]:


#code
num = input("Enter the number: ")
length = len(num)
int_num =int(num)
str_num=""
total=0
y=0
for x in range(length):
    y = int_num%10
    total += y**length
    int_num//=10
for i in range(length):
        if(i==length-1):
            str_num += num[i] + ' * '+ num[i] + ' * '+ num[i] + ' = '
        else:
            str_num += num[i] + ' * '+ num[i] + ' * '+ num[i] + ' + '
if(total==int(num)):
        print("yes \n\n"+num+" is a armstrong number\n\n"+str_num+ num)
else:
        print("No " +num +" is not a armstrong number" )


# 7) Program to find Sum of squares of first n natural numbers.

# In[63]:


#code

num =int(input("Enter natural number n: "))
total=0
for x in range(num+1):
    total+= x**2
print("The sum of squares of n natural numbers is "+ str(total))


# 8) Program to Reverse words in a given String in Python.

# In[66]:


#code

string = input("Enter String: ")
rev_str=""
for x in range(len(string)-1,-1,-1):
    rev_str+=string[x]
print(rev_str)


# 9) Given a list of numbers, write a Python program to find the sum of all the elements in the list.
# 
# Input: [10,12,13]
# 
# Output: 35

# In[81]:


#code(i did it in 3 ways)



#list=[10,12,13]
#total=0
#for x in list:
#    total += x
#print(total)

int_list=[]
total=0
n=int(input("enter number of elements in list "))
for x in range(n):
    l_input=int(input())
    int_list.append(l_input)
        
for y in int_list:
      total += y
print("The sum of numbers given in list is "+str(total))
      


# In[83]:


#code(for ques 9)
total = 0
n=input("enter number of elements in list seperated by commas ")
str_list=n.split(",")
new_list=[]
for i in range(len(str_list)):
    new_list.append(int(str_list[i]))
        
for y in new_list:
      total += y
print("The sum of numbers given in list is "+str(total))


# 10) Write a Python program to print all even numbers between 10-1000.

# In[3]:


#code

for x in range(10,1001,1):
    if(x%2==0):
        print(x)


# In[85]:


#code(2nd way for ques 10)
for x in range(10,1001,2):
    print(x)


# In[ ]:




