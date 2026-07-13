import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(14,7))

ax.set_xlim(0,4)
ax.set_ylim(0,3)
ax.axis('off')

# Data
states = ["S1","S2","S3"]
best_actions = ["A1","A1","A1"]
expected_rewards = [2.8,3.1,3.6]

transitions = [
"""A1→S2 : P=0.6 R=5
A1→S3 : P=0.2 R=-1
A2→S2 : P=0.4 R=10
A2→S3 : P=0.8 R=-5""",

"""A1→S1 : P=0.7 R=3
A1→S3 : P=0.5 R=2
A2→S1 : P=0.3 R=7
A2→S3 : P=0.5 R=1""",

"""A1→S1 : P=0.9 R=4
A1→S2 : P=0.4 R=0
A2→S1 : P=0.1 R=6
A2→S2 : P=0.6 R=-2"""
]

colors = ["lightgreen","lightskyblue","khaki","lightcoral"]

for i in range(3):

    # State
    ax.add_patch(Rectangle((0,2-i),1,1,
                           facecolor=colors[0],
                           edgecolor='black'))
    ax.text(0.5,2.5-i,
            f"State\n{states[i]}",
            ha='center',
            va='center',
            fontsize=11,
            fontweight='bold')

    # Actions
    ax.add_patch(Rectangle((1,2-i),1,1,
                           facecolor=colors[1],
                           edgecolor='black'))
    ax.text(1.5,2.5-i,
            "Actions\nA1\nA2",
            ha='center',
            va='center',
            fontsize=11,
            fontweight='bold')

    # Transitions
    ax.add_patch(Rectangle((2,2-i),1,1,
                           facecolor=colors[2],
                           edgecolor='black'))
    ax.text(2.5,2.5-i,
            transitions[i],
            ha='center',
            va='center',
            fontsize=8)

    # Best Action
    ax.add_patch(Rectangle((3,2-i),1,1,
                           facecolor=colors[3],
                           edgecolor='black'))
    ax.text(3.5,2.5-i,
            f"Best Action\n{best_actions[i]}\nReward={expected_rewards[i]}",
            ha='center',
            va='center',
            fontsize=11,
            color='darkred',
            fontweight='bold')

plt.title("Markov Decision Process (MDP)\nStates, Actions, Transitions and Best Action",
          fontsize=16,
          fontweight='bold')

plt.show()
