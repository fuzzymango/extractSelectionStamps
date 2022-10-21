import nuke

def extractSelectionStamps():
	if not nuke.selectedNodes():
		return

	no_ops = []
	for node in nuke.selectedNodes():
		if node.Class() == "NoOp":
			no_op = node
			connection = node.input(0)
			no_ops.append((no_op, connection))
	nuke.extractSelected()

	if not no_ops:
		return
	for no_op, connection in no_ops:
		no_op.setInput(0, connection)

