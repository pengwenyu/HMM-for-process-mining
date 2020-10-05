import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply(os.path.join("topx event log","15.xes"))

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)