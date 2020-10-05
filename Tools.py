import os
from pm4py.objects.petri.importer import importer as pnml_importer
from pm4py.visualization.petrinet import visualizer as pn_visualizer

find_all = lambda data, s: [r for r in range(len(data)) if data[r] == s]

def get_transition_id_and_name(lines, start, end):
    find_all = lambda data, s: [r for r in range(len(data)) if data[r] == s]
    for i in range(start, end):
        if "transition id" in lines[i]:
            r_list = find_all(lines[i], '"')
            id = lines[i][r_list[0] + 1:r_list[1]]
        if "<text>" in lines[i]:
            r_list = find_all(lines[i], '<')
            name = lines[i][r_list[0] + 6:r_list[1]]
    return id, name

def get_place_id(lines, start, end):
    find_all = lambda data, s: [r for r in range(len(data)) if data[r] == s]
    for i in range(start, end):
        if "place id" in lines[i]:
            r_list = find_all(lines[i], '"')
            id = lines[i][r_list[0] + 1:r_list[1]]
    return id

def get_causal_net(pnml_file_path):
    net, initial_marking, final_marking = pnml_importer.apply(os.path.join("pnml","3 length loop.pnml"))
    gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    #pn_visualizer.view(gviz)
    find_all = lambda data, s: [r for r in range(len(data)) if data[r] == s]

    fp=open(pnml_file_path)
    lines = fp.readlines()

    idx=[]
    for i in range(len(lines)):
        if'<transition id=' in lines[i]:
            idx.append(i)
            #print("transtion start line ",i)
        if '</transition>' in lines[i]:
            idx.append(i)
            #print("transtion end line ", i)
    id_list=[]
    name_list=[]
    dependency_list=[]
    for i in range(0,len(idx),2):
        if i== len(idx)-1:
            break
        start = idx[i]
        end = idx[i+1]
        id,name =get_transition_id_and_name(lines,start,end)
        id_list.append(id)
        name_list.append(name)
    #print(id_list)
    #print(name_list)
    for i in range(0,len(id_list)):
        for j in range(len(lines)):
            str1= 'source='+'"'+id_list[i]+'"'
            if str1 in lines[j]:
                r_list = find_all(lines[j], '"')
                target= lines[j][r_list[4] +1:r_list[5]]
                #print(target)
                str2='source='+'"'+target+'"'
                for k in range(len(lines)):
                    if str2 in lines[k]:
                        r_list = find_all(lines[k], '"')
                        target2=lines[k][r_list[4] +1:r_list[5]]
                        dependency= id_list[i]+'-'+target2
                        dependency_list.append(name_list[i])
                        for m in range(0,len(id_list)):
                            if target2 == id_list[m]:
                                dependency_list.append(name_list[m])
    #print(dependency_list)
    source=[]
    target=[]
    for i in range (0,len(dependency_list)):
        if i%2==0:
            source.append(dependency_list[i])
        else:
            target.append(dependency_list[i])
    #print(source)
    #print(target)

    return source,target

def get_all_transition(pnml_file_path):
    idx=[]
    fp=open(pnml_file_path)
    lines = fp.readlines()
    id_list=[]
    name_list=[]
    for i in range(len(lines)):
        if'<transition id=' in lines[i]:
            idx.append(i)
            #print("transtion start line ",i)
        if '</transition>' in lines[i]:
            idx.append(i)
            #print("transtion end line ", i)
    for i in range(0,len(idx),2):
        if i== len(idx)-1:
            break
        start = idx[i]
        end = idx[i+1]
        id,name =get_transition_id_and_name(lines,start,end)
        id_list.append(id)
        name_list.append(name)
    #print(name_list)
    #print(id_list)
    return name_list,id_list
get_all_transition('pnml/3 length loop.pnml')

def get_all_place(pnml_file_path):
    idx=[]
    fp=open(pnml_file_path)
    lines = fp.readlines()
    id_list=[]
    for i in range(len(lines)):
        if'<place id=' in lines[i]:
            idx.append(i)
            #print("transtion start line ",i)
        if '</place>' in lines[i]:
            idx.append(i)
            #print("transtion end line ", i)
    for i in range(0,len(idx),2):
        if i== len(idx)-1:
            break
        start = idx[i]
        end = idx[i+1]
        id=get_place_id(lines,start,end)
        id_list.append(id)
    #print(id_list)
    return id_list

get_all_place('pnml/3 length loop.pnml')

def get_all_arcs(pnml_file_path):
    idx=[]
    fp=open(pnml_file_path)
    lines = fp.readlines()
    source_list=[]
    target_list=[]

    for i in range(0,len(lines)):
        if '<arc id='in lines[i]:
            r_list = find_all(lines[i], '"')
            source= lines[i][r_list[2] + 1:r_list[3]]
            target= lines[i][r_list[4] + 1:r_list[5]]
            source_list.append(source)
            target_list.append(target)
    #print(source_list,target_list)
    return  source_list,target_list

get_all_arcs('pnml/3 length loop.pnml')


def get_next_place(transition_id,source,target):
    place_id=[]
    for i in range(0,len(source)):
        if transition_id==source[i]:
            place_id.append(target[i])
    return place_id

def get_last_place(transition_id,source,target):
    place_id=[]
    for i in range(0,len(target)):
        if transition_id==target[i]:
            place_id.append(source[i])
    return place_id


def get_next_transition(place_id,source,target):
    transition_id=0
    for i in range(0,len(source)):
        if place_id==source[i]:
            transition_id=target[i]
    return transition_id

def get_event_name(lines,start,end):
    find_all = lambda data, s: [r for r in range(len(data)) if data[r] == s]
    for i in range(start,end):
        if "concept:name" in lines[i]:
            r_list = find_all(lines[i], '"')
            event_name = lines[i][r_list[2]+1:r_list[3]]
    return  event_name

def get_unique_trace(xes_file_path):
    log = []
    fp=open(xes_file_path)
    lines = fp.readlines()
    idx=[]
    idx_event =[]
    for i in range(len(lines)):
        if'<trace>' in lines[i]:
            idx.append(i)
        if '</trace>' in lines[i]:
            idx.append(i)
        if'<event>' in lines[i]:
            idx_event.append(i)
        if'</event>' in lines[i]:
            idx_event.append(i)

    index_in_event=0
    for i in range(0,len(idx),2):
        if i== len(idx)-1:
            break
        start = idx[i]
        end = idx[i+1]
        event_in_trace=0
        trace=[]
        for j in range(start,end):
            if '<event>' in lines[j]:
                event_in_trace=event_in_trace+1
        for k in range(0,event_in_trace):
            event_start = idx_event[index_in_event]
            event_end = idx_event[index_in_event + 1]
            event_name = get_event_name(lines, event_start, event_end)
            trace.append(event_name)
            index_in_event = index_in_event + 2
        log.append(trace)

    #print(log)
    unique_traces=[]
    unique_times=[]
    #print(log[0])
    #print(len(log))
    for i in range(0,len(log)):
        if log[i] not in unique_traces:
            unique_traces.append(log[i])
    for i in range(0,len(unique_traces)):
        n=0
        for j in range(0,len(log)):
            if unique_traces[i]==log[j]:
                n=n+1
        unique_times.append(n)
    #print(unique_traces)
    #print(unique_times)
    return unique_traces,unique_times


def get_transition_name(transition_id,transition_name_list):
    transition_name=transition_id
    for i in range(0,len(transition_name_list)):
        if transition_id==transition_name_list[i]:
            transition_name=transition_name_list[i]
    return transition_name

def get_topx_unique_trace(x,unique_times):
    import heapq
    import copy
    m=copy.deepcopy(unique_times)
    max_number = heapq.nlargest(x, m)
    max_index = []
    for t in max_number:
        index = m.index(t)
        max_index.append(index)
        m[index] = 0
    return max_index