from graphviz import Digraph

flow = Digraph("MDP_Detailed_Flowchart", format="png")

# Graph Settings
flow.attr(rankdir="TB",
          splines="ortho",
          bgcolor="white",
          nodesep="0.4",
          ranksep="0.6")

flow.attr('node',
          style='filled',
          fontname='Arial',
          fontsize='11')

# ---------------- START ----------------
flow.node('A','START',
          shape='ellipse',
          fillcolor='palegreen')

# ---------------- INPUT ----------------
flow.node('B',
'''Input MDP Parameters

States = {S1,S2,S3}
Actions = {A1,A2}
Transition Probabilities
Reward Matrix''',
shape='parallelogram',
fillcolor='lightcyan')

# ---------------- PROCESS ----------------

flow.node('C',
'Initialize\nStates & Actions',
shape='rectangle',
fillcolor='lightyellow')

flow.node('D',
'Create Transition\nProbability Matrix',
shape='rectangle',
fillcolor='khaki')

flow.node('E',
'Create Reward Matrix',
shape='rectangle',
fillcolor='moccasin')

flow.node('F',
'Display Transition\nMatrix',
shape='parallelogram',
fillcolor='lavender')

flow.node('G',
'Display Reward\nMatrix',
shape='parallelogram',
fillcolor='lavenderblush')

# ---------------- LOOP ----------------

flow.node('H',
'Select Current State',
shape='rectangle',
fillcolor='honeydew')

flow.node('I',
'More States?',
shape='diamond',
fillcolor='lightpink')

flow.node('J',
'Select Action\n(A1 or A2)',
shape='rectangle',
fillcolor='lightyellow')

flow.node('K',
'More Actions?',
shape='diamond',
fillcolor='lightpink')

flow.node('L',
'''Calculate

Expected Reward

ER = Σ P × R''',
shape='rectangle',
fillcolor='azure')

flow.node('M',
'Store Expected Reward',
shape='rectangle',
fillcolor='mintcream')

flow.node('N',
'Compare Rewards\nof A1 & A2',
shape='diamond',
fillcolor='mistyrose')

flow.node('O',
'''Select Best Action

S1 → A1
S2 → A1
S3 → A1''',
shape='rectangle',
fillcolor='lightgreen')

flow.node('P',
'''Display

Expected Reward Table

Best Action

Grid Environment''',
shape='parallelogram',
fillcolor='aliceblue')

flow.node('Q',
'END',
shape='ellipse',
fillcolor='palegreen')

# ---------------- CONNECTIONS ----------------

flow.edge('A','B')

flow.edge('B','C')

flow.edge('C','D')

flow.edge('D','E')

flow.edge('E','F')

flow.edge('F','G')

flow.edge('G','H')

flow.edge('H','I')

flow.edge('I','J',label='Yes')

flow.edge('J','K')

flow.edge('K','L',label='Yes')

flow.edge('L','M')

flow.edge('M','K',label='Next Action')

flow.edge('K','N',label='No')

flow.edge('N','H',label='Next State')

flow.edge('I','O',label='No')

flow.edge('O','P')

flow.edge('P','Q')

flow.render("Detailed_MDP_Flowchart",view=True)
