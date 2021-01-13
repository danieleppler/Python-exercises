class Agent:
	name: str
	 # Worker name, for display.
	preferences: list
	# preferences[0] is the best shift for the worker.
	# preferences[1] is the 2nd-best shift for the worker. etc...
	current_shift: int
	# The shift to which the worker is currently assigned