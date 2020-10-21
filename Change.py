pnml_file_path='petri.pnml'
fp = open(pnml_file_path)
lines = fp.readlines()
for i in range(0,len(lines)):
    if "<name>" in lines[i]:
        lines[i]='\t'+'\t'+'\t' + '\t'+lines[i]
    if "</name>"in lines[i]:
        lines[i] = '\t' + '\t' + '\t' +'\t'+ lines[i]
    if "transition id"in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + lines[i]
    if "</transition>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + lines[i]
    if "<text/>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' +'\t'+ lines[i]
    if "place id" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + lines[i]
    if "</place>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + lines[i]
    if "<graphics>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + lines[i]
    if "</graphics>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + lines[i]
    if "<text>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t'+'\t' + lines[i]
    if "position" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + '\t' + lines[i]
    if "dimension" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + '\t' + lines[i]
    if "<arctype>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t'+ lines[i]
    if "</arctype>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + lines[i]
    if "arc id" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + lines[i]
    if "</arc>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + lines[i]
    if "toolspecific" in lines[i]:
        lines[i]='\t' + '\t' + '\t' + '\t' + lines[i]
    if "<initialMarking>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + lines[i]
    if "</initialMarking>" in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + lines[i]
    if "fill color"in lines[i]:
        lines[i] = '\t' + '\t' + '\t' + '\t' + '\t' + lines[i]
    if "page id" in lines[i]:
        lines[i] = '\t' + '\t'+lines[i]
file=open("modify.xes",'w')
for i in range(0,len(lines)):
    file.write(lines[i])
file.close()
