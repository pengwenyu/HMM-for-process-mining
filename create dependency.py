from pm4py.objects.petri.petrinet import PetriNet, Marking
net = PetriNet("new_petri_net")

start = PetriNet.Place("start")
end = PetriNet.Place("end")
p_1 = PetriNet.Place("({'Activity A'}, {'Activity B'})")
p_2 = PetriNet.Place("({'Activity A'}, {'Activity C'})")
p_3 = PetriNet.Place("({'Activity A'}, {'Activity C'})")
p_4 = PetriNet.Place("({'Activity A'}, {'Activity C'})")
# add the places to the Petri Net
net.places.add(start)
net.places.add(end)
net.places.add(p_1)
net.places.add(p_2)
net.places.add(p_3)
net.places.add(p_4)

t_1 = PetriNet.Transition("Activity A", "Activity A")
t_2 = PetriNet.Transition("Activity B", "Activity B")
t_3 = PetriNet.Transition("Activity C", "Activity C")
t_4 = PetriNet.Transition("Activity D", "Activity D")
# Add the transitions to the Petri Net
net.transitions.add(t_1)
net.transitions.add(t_2)
net.transitions.add(t_3)
net.transitions.add(t_4)

from pm4py.objects.petri import utils
utils.add_arc_from_to(start, t_1, net)
utils.add_arc_from_to(t_4, end, net)
utils.add_arc_from_to(t_1, p_1, net)
utils.add_arc_from_to(t_1, p_2, net)
utils.add_arc_from_to(p_1, t_2, net)
utils.add_arc_from_to(p_2, t_3, net)
utils.add_arc_from_to(t_2, p_3, net)
utils.add_arc_from_to(t_3, p_4, net)
utils.add_arc_from_to(p_3, t_4, net)
utils.add_arc_from_to(p_4, t_4, net)
initial_marking = Marking()
initial_marking[start] = 1
final_marking = Marking()
final_marking[end] = 1

from pm4py.objects.petri.exporter import exporter as pnml_exporter
pnml_exporter.apply(net, initial_marking, "createdPetriNet1.pnml", final_marking=final_marking)

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)
