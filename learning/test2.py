from libhfst import *

fsm =HfstBasicTransducer()
fsm.add_state(1)
fsm.add_state(2)
tr = HfstBasicTransition(1,'foo','bar',0.1)
fsm.add_transition(0,tr)
tr = HfstBasicTransition(2,'bar','bar',0.2)
fsm.add_transition(1,tr)

for state, arcs in enumerate(fsm):
	for arc in arcs:
		print('%i'%(state), end=' ')
		print(arc)
	if fsm.is_final_state(state):
		print('final haha')
