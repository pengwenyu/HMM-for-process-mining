from Tools import *
unique_traces,unique_times=get_unique_trace('./model 30 model file/model 30.xes')

x=25
pnml1='./model 30 model file/model 30.pnml'
#pnml2='./topx petri net/top'+str(x)+'.pnml'
pnml2='./Inductive Miner.pnml'
transition_name1,transition_id1=get_all_transition(pnml1)
transition_name2,transition_id2=get_all_transition(pnml2)
place1=get_all_place(pnml1)
place2=get_all_place(pnml2)
source1,target1=get_all_arcs(pnml1)
source2,target2=get_all_arcs(pnml2)


trace_number=0
for i in unique_times:
    trace_number=trace_number+i
#print(trace_number)
print(unique_traces)
print(unique_times)

Token_need1=[]
Token_need2=[]
for i in range(0,len(transition_id1)):
    place_id=get_last_place(transition_id1[i],source1,target1)
    Token_need1.append(len(place_id))
print(Token_need1)
for i in range(0,len(transition_id2)):
    place_id=get_last_place(transition_id2[i],source2,target2)
    Token_need2.append(len(place_id))
print(Token_need2)

Behavior_Percision=0
Behavior_Recall=0
print("Replay Start")
print("**************************")
for i in range(0,len(unique_traces)):
    A=unique_traces[i]
    a=unique_times[i]/len(A)
    print("a is",a)
    sum1 = 0
    sum2 = 0
    place_have_token1=['start']
    place_have_token2=['start']
    print(i+1," unique trace start",A)
    for j in range(0,len(A)):
        Enable_Intersection1 = 0
        Enable_Intersection2 = 0
        enable_transition1 = []
        enable_transition2 = []
        #get enable transition in model 1
        print("step ",j+1," start")
        for k in range(0,len(place_have_token1)):
            transition_id=get_next_transition(place_have_token1[k],source1,target1)
            print('Transtion that can be fired in model 1',transition_id)
            for m in range(0,len(transition_id)):
                flag = 1
                place_id=get_last_place(transition_id[m],source1,target1)
                for n in range(0,len(place_id)):
                    if place_id[n] not in place_have_token1:
                        flag=0
                if flag==1:
                    enable_transition1.append(get_transition_name(transition_id[m],transition_name1,transition_id1))
        print("enable transition in model 1 is",enable_transition1)
        # get enable transition in model 2
        for k in range(0,len(place_have_token2)):
            transition_id=get_next_transition(place_have_token2[k],source2,target2)
            print('Transtion that can be fired in model 1',transition_id)
            for m in range(0,len(transition_id)):
                flag = 1
                place_id=get_last_place(transition_id[m],source2,target2)
                for n in range(0,len(place_id)):
                    if place_id[n] not in place_have_token2:
                        flag=0
                if flag==1:
                    enable_transition2.append(get_transition_name(transition_id[m],transition_name1,transition_id1))
        print("enable transition in model 2 is", enable_transition2)
        # get intersection
        for k in range(0,len(enable_transition1)):
            if enable_transition1[k] in enable_transition2:
                Enable_Intersection1=Enable_Intersection1+1
        if len(enable_transition1) != 0:
            sum1 = Enable_Intersection1 / len(enable_transition1) + sum1
        if len(enable_transition2) != 0:
            sum2 = Enable_Intersection1 / len(enable_transition2) + sum2
        print("calculate sum1", sum1)
        print("calculate sum2", sum2)

        if A[j] in enable_transition1:
            id=get_transition_id(A[j],transition_name1,transition_id1)
            token_consumed=get_last_place(id,source1,target1)
            print('token_consumed is',token_consumed)
            for k in range(0,len(token_consumed)):
                if token_consumed[k] in place_have_token1:
                    place_have_token1.remove(token_consumed[k])

            generate_token=get_next_place(id,source1,target1)
            for k in range(0,len(generate_token)):
                place_have_token1.append(generate_token[k])
        else:
            id = get_transition_id(A[j], transition_name1, transition_id1)
            generate_token=get_next_place(id,source1,target1)
            for k in range(0,len(generate_token)):
                place_have_token1.append(generate_token[k])
        print("model 1 place have token",place_have_token1)


        if A[j] in enable_transition2:
            id=get_transition_id(A[j],transition_name2,transition_id2)
            token_consumed=get_last_place(id,source2,target2)
            print('token_consumed is',token_consumed)
            for k in range(0,len(token_consumed)):
                if token_consumed[k] in place_have_token2:
                    place_have_token2.remove(token_consumed[k])

            generate_token=get_next_place(id,source2,target2)
            for k in range(0,len(generate_token)):
                place_have_token2.append(generate_token[k])
        else:
            id = get_transition_id(A[j], transition_name2, transition_id2)
            generate_token=get_next_place(id,source2,target2)
            for k in range(0,len(generate_token)):
                place_have_token2.append(generate_token[k])
        print("model 2 place have token",place_have_token2)

        print("sum1 is",sum1)
        print("***")
    Behavior_Percision = sum1 * a + Behavior_Percision
    Behavior_Recall = sum2 * a + Behavior_Recall
print('Behavior_Percision is',Behavior_Percision/1000)
print('Behavior_Recall is',Behavior_Recall /1000)









