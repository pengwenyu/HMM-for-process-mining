import os
from pm4py.objects.log.importer.xes import importer as xes_importer
x=60
#log = xes_importer.apply(os.path.join(str(x)+".xes"))


log=xes_importer.apply('3 length loop 2.0.xes')
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

from pm4py.objects.petri.exporter import exporter as pnml_exporter
pnml_exporter.apply(net, initial_marking, "petri.pnml")