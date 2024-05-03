# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:59:09 2024

@author: User
"""
import time
import matplotlib.pyplot as plt

x_label = [x for x in range(1,101)]  #value of the target num
time_stamp = [] #excution time of calculating the target


#top_buttom method
def top_buttom(last_num: int) -> int:
    if last_num == 1 or last_num == 2:
        return 1
    else:
        return top_buttom(last_num-1) + top_buttom(last_num-2)


for i in x_label:
    start_time = time.time()
    print(top_buttom(i))
    end_time = time.time()

    excution_time = end_time - start_time
    time_stamp.append(excution_time)

plt.plot(x_label, time_stamp)
plt.xlabel('x')
plt.ylabel('time')
plt.show()


times = []  #to save the times that F(4) is calculated of each F(x)
#the times that F(4) is calculated is also a Fibonacci Sequence
def f(num:int, val=1, pre=0) -> int:
    if num == 1:
        return val
    else:
        return f(num-1, val=val+pre, pre=val)
    
#to calculate times of each x(a Fibonacci Sequence from 2nd to 48th)
for i in range(2,48):
    times.append(f(i))


x_label = [x for x in range(5,51)]  #range of x

plt.plot(x_label, times)
plt.xlabel('x')
plt.ylabel('times')
plt.show()