from Tools import *
import heapq
import numpy as np
a1,a2 =get_unique_trace('model 30 event logs/20% noise.xes')

import heapq

index=get_topx_unique_trace(30,a2)
print(index)

file = open('reference.txt','w');

a3=[]
for i in index:
    a3.append(i)

for i in a3:
    file.write(str(a1[i]))
    file.write('\n')
    file.write(str(a2[i]))
    file.write('\n')

file.write('the top x has been sorted')
file.write('\n')
file.write('\n')
file.write('\n')


for i in range(0,len(a1)):
    if i in a3:
        print('already saved')
    else:
        file.write(str(a1[i]))
        file.write('\n')
        file.write(str(a2[i]))
        file.write('\n')
file.close()
