import numpy as np

# States
states = ["S1", "S2", "S3"]

# Transition Probability Matrix for Action A1
P_A1 = np.array([
    [0.0, 0.6, 0.2],
    [0.7, 0.0, 0.5],
    [0.9, 0.4, 0.0]
])

# Transition Probability Matrix for Action A2
P_A2 = np.array([
    [0.0, 0.4, 0.8],
    [0.3, 0.0, 0.5],
    [0.1, 0.6, 0.0]
])

# Display matrices
print("States:", states)
print("\nTransition Probability Matrix for Action A1")
print("      S1    S2    S3")
for i in range(len(states)):
    print(states[i], P_A1[i])

print("\nTransition Probability Matrix for Action A2")
print("      S1    S2    S3")
for i in range(len(states)):
    print(states[i], P_A2[i])
