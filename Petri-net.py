import os
from pm4py.objects.log.importer.xes import importer as xes_importer


pnmlfile="D://process mining//HMM//pnml//reference//reference 7.pnml"
import os
from pm4py.objects.petri.importer import importer as pnml_importer
net, initial_marking, final_marking = pnml_importer.apply(os.path.join(pnmlfile))

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

