# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:40:34 2024

@author: User
"""
import time
import matplotlib.pyplot as plt

x_label = [x for x in range(1,101)]  #value of the target num
time_stamp = [] #excution time of calculating the target

#buttom_up method
def buttom_up(last_num:int) -> int:
    result = [] #list to store result of F(x)
    
    for i in range(last_num):
        if i == 0 or i == 1:
            result.append(1)
        else:
            result.append(result[i-1] + result[i-2])
    
    return result[last_num-1]

for i in x_label:
    start_time = time.time()
    print(buttom_up(i))
    end_time = time.time()

    excution_time = end_time - start_time
    time_stamp.append(excution_time)

plt.plot(x_label, time_stamp)
plt.xlabel('x')
plt.ylabel('time')
plt.show()