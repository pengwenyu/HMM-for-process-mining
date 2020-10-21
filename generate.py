import os
from pm4py.objects.log.importer.xes import importer as xes_importer
x=2
log = xes_importer.apply(os.path.join('topx event log',str(x)+".xes"))


from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

from pm4py.objects.petri.exporter import exporter as pnml_exporter
filename="top"+str(x)+".pnml"
pnml_exporter.apply(net, initial_marking, filename)