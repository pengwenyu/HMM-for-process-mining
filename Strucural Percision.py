from Tools import *


def deleteDuplicatedElementFromList2(list):
    resultList = []
    for item in list:
        if not item in resultList:
            resultList.append(item)
    return resultList

x=4
pnml1='./model 30.pnml'
pnml2='./topx petri net/top'+str(x)+'.pnml'

source1,target1=get_causal_net(pnml1)
source2,target2=get_causal_net(pnml2)

print(source1)
print(target1)
print(source2)
print(target2)

list1=[]
list2=[]
for i in range(0,len(source1)):
    list1.append(source1[i]+'-'+target1[i])

for i in range(0, len(source2)):
    list2.append(source2[i] +'-'+ target2[i])

list1=deleteDuplicatedElementFromList2(list1)
list2=deleteDuplicatedElementFromList2(list2)

Cr_Cm=0
for i in range(0,len(list1)):
    for j in range(0, len(list2)):
        if list1[i]==list2[j]:
            Cr_Cm = Cr_Cm+1
print(list1)
print(list2)
print('Structural_Percision is',Cr_Cm/len(list1))
print('Structural_Recall is',Cr_Cm/len(list2))