# Markov Decision Process (MDP)

# States
states = ["S1", "S2", "S3"]

# Actions
actions = ["A1", "A2"]

# Transition Probabilities
transition_probabilities = {
    ("S1", "A1"): {"S2": 0.6, "S3": 0.2},
    ("S1", "A2"): {"S2": 0.4, "S3": 0.8},
    ("S2", "A1"): {"S1": 0.7, "S3": 0.5},
    ("S2", "A2"): {"S1": 0.3, "S3": 0.5},
    ("S3", "A1"): {"S1": 0.9, "S2": 0.4},
    ("S3", "A2"): {"S1": 0.1, "S2": 0.6}
}

# Rewards
rewards = {
    ("S1", "A1", "S2"): 5,
    ("S1", "A2", "S2"): 10,
    ("S1", "A1", "S3"): -1,
    ("S1", "A2", "S3"): -5,

    ("S2", "A1", "S1"): 3,
    ("S2", "A2", "S1"): 7,
    ("S2", "A1", "S3"): 2,
    ("S2", "A2", "S3"): 1,

    ("S3", "A1", "S1"): 4,
    ("S3", "A2", "S1"): 6,
    ("S3", "A1", "S2"): 0,
    ("S3", "A2", "S2"): -2
}

# Display Number of States and Actions
print("===== Markov Decision Process =====")
print("Number of States:", len(states))
print("States:", states)

print("\nNumber of Actions:", len(actions))
print("Actions:", actions)

# Display Transition Probabilities
print("\n===== Transition Probabilities =====")
for (state, action), transitions in transition_probabilities.items():
    print(f"\nState: {state}, Action: {action}")
    for next_state, prob in transitions.items():
        print(f"   P({next_state} | {state}, {action}) = {prob}")

# Display Rewards
print("\n===== Rewards =====")
for (state, action, next_state), reward in rewards.items():
    print(f"R({state}, {action}, {next_state}) = {reward}")
