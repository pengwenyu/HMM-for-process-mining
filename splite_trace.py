from Tools import *
unique_trace,unique_times =get_unique_trace('model 30.xes')
x=15
index=get_topx_unique_trace(x,unique_times)
topx=[]
for i in index:
    topx.append(unique_trace[i])

#print(topx)

log = []

fp = open('model 30.xes')
lines = fp.readlines()
idx = []
idx_event = []
idx_unique=[]
for i in range(len(lines)):
    if '<trace>' in lines[i]:
        idx.append(i)
    if '</trace>' in lines[i]:
        idx.append(i)
    if '<event>' in lines[i]:
        idx_event.append(i)
    if '</event>' in lines[i]:
        idx_event.append(i)
print(len(idx)/2)
index_in_event = 0
for i in range(0, len(idx), 2):
    if i == len(idx) - 1:
        break
    start = idx[i]
    end = idx[i + 1]
    event_in_trace = 0
    trace = []
    for j in range(start, end):
        if '<event>' in lines[j]:
            event_in_trace = event_in_trace + 1
    for k in range(0, event_in_trace):
        event_start = idx_event[index_in_event]
        event_end = idx_event[index_in_event + 1]
        event_name = get_event_name(lines, event_start, event_end)
        trace.append(event_name)
        index_in_event = index_in_event + 2
    #print(trace)
    for m in range(0,len(topx)):
        if trace == topx[m]:
            #print(trace)
            idx_unique.append(start)
            idx_unique.append(end)
log1=[]
print(len(idx_unique)/2)
head='<log xes.version="1.0" xes.features="nested-attributes" openxes.version="1.0RC7">'+'\n'
tail= '</log>'

log1.append(head)
for i in range(0,len(idx_unique),2):
    if i==len(idx_unique)-1:
        break
    start=idx_unique[i]
    end=idx_unique[i+1]
    for j in range(start, end):
        log1.append(lines[j])
    log1.append(lines[end])
log1.append(tail)


file=open('log2.xes','w')
for i in range(len(log1)):
    file.write(log1[i]);
file.close()

