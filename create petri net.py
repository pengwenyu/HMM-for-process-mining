from pm4py.objects.petri.petrinet import PetriNet, Marking
net = PetriNet("new_petri_net")

start = PetriNet.Place("start")
end = PetriNet.Place("end")
p_1 = PetriNet.Place("({'Activity A'}, {'Activity C', 'Activity D'})")
p_2 = PetriNet.Place("({'Activity C','Activity E'}, {'Activity B'})")
p_3 = PetriNet.Place("({'Activity D','Activity H'}, {'Activity F'})")
p_4 = PetriNet.Place("({'Activity F'}, {'Activity G', 'Activity E'})")
p_5 = PetriNet.Place("({'Activity G'}, {'Activity I'})")
p_6 = PetriNet.Place("({'Activity G'}, {'Activity J'})")
p_7 = PetriNet.Place("({'Activity I','Activity J'}, {'Activity H'})")
# add the places to the Petri Net
net.places.add(start)
net.places.add(end)
net.places.add(p_1)
net.places.add(p_2)
net.places.add(p_3)
net.places.add(p_4)
net.places.add(p_5)
net.places.add(p_6)
net.places.add(p_7)


t_1 = PetriNet.Transition("Activity A", "Activity A")
t_2 = PetriNet.Transition("Activity B", "Activity B")
t_3 = PetriNet.Transition("Activity C", "Activity C")
t_4 = PetriNet.Transition("Activity D", "Activity D")
t_5 = PetriNet.Transition("Activity E", "Activity E")
t_6 = PetriNet.Transition("Activity F", "Activity F")
t_7 = PetriNet.Transition("Activity G", "Activity G")
t_8 = PetriNet.Transition("Activity H", "Activity H")
t_9 = PetriNet.Transition("Activity I", "Activity I")
t_10 = PetriNet.Transition("Activity J", "Activity J")
# Add the transitions to the Petri Net
net.transitions.add(t_1)
net.transitions.add(t_2)
net.transitions.add(t_3)
net.transitions.add(t_4)
net.transitions.add(t_5)
net.transitions.add(t_6)
net.transitions.add(t_7)
net.transitions.add(t_8)
net.transitions.add(t_9)
net.transitions.add(t_10)

from pm4py.objects.petri import utils
utils.add_arc_from_to(start, t_1, net)
utils.add_arc_from_to(t_2, end, net)
utils.add_arc_from_to(t_1, p_1, net)
utils.add_arc_from_to(p_1, t_3, net)
utils.add_arc_from_to(p_1, t_4, net)
utils.add_arc_from_to(t_3, p_2, net)
utils.add_arc_from_to(p_2, t_2, net)
utils.add_arc_from_to(t_4, p_3, net)
utils.add_arc_from_to(p_3, t_6, net)
utils.add_arc_from_to(t_6, p_4, net)
utils.add_arc_from_to(p_4, t_5, net)
utils.add_arc_from_to(p_4, t_7, net)
utils.add_arc_from_to(t_5, p_2, net)
utils.add_arc_from_to(t_7, p_5, net)
utils.add_arc_from_to(t_7, p_6, net)
utils.add_arc_from_to(p_5, t_9, net)
utils.add_arc_from_to(p_6, t_10, net)
utils.add_arc_from_to(t_9, p_7, net)
utils.add_arc_from_to(t_10, p_7, net)
utils.add_arc_from_to(p_7, t_8, net)
utils.add_arc_from_to(t_8, p_3, net)


initial_marking = Marking()
initial_marking[start] = 1
final_marking = Marking()
final_marking[end] = 1

from pm4py.objects.petri.exporter import exporter as pnml_exporter
pnml_exporter.apply(net, initial_marking, "createdPetriNet1.pnml", final_marking=final_marking)

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

from pm4py.objects.petri.exporter import exporter as pnml_exporter
filename="petri.pnml"
pnml_exporter.apply(net, initial_marking, filename)