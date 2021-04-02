
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
logfile="D://process mining//HMM//pnml//reference//reference5.xes"
log = xes_importer.apply(os.path.join(logfile))

from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
net, im, fm = heuristics_miner.apply(log, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, im, fm)
pn_visualizer.view(gviz)

from pm4py.objects.petri.exporter import exporter as pnml_exporter
filename="Heuristic Miner.pnml"
pnml_exporter.apply(net, im, filename)