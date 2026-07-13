import pandas as pd

# States and Actions
states = ["S1", "S2", "S3"]
actions = ["A1", "A2"]

# Transition Probabilities
P = {
    ("S1", "A1"): {"S2": 0.6, "S3": 0.2},
    ("S1", "A2"): {"S2": 0.4, "S3": 0.8},
    ("S2", "A1"): {"S1": 0.7, "S3": 0.5},
    ("S2", "A2"): {"S1": 0.3, "S3": 0.5},
    ("S3", "A1"): {"S1": 0.9, "S2": 0.4},
    ("S3", "A2"): {"S1": 0.1, "S2": 0.6}
}

# Rewards
R = {
    ("S1", "A1", "S2"): 5,
    ("S1", "A1", "S3"): -1,
    ("S1", "A2", "S2"): 10,
    ("S1", "A2", "S3"): -5,

    ("S2", "A1", "S1"): 3,
    ("S2", "A1", "S3"): 2,
    ("S2", "A2", "S1"): 7,
    ("S2", "A2", "S3"): 1,

    ("S3", "A1", "S1"): 4,
    ("S3", "A1", "S2"): 0,
    ("S3", "A2", "S1"): 6,
    ("S3", "A2", "S2"): -2
}

summary = []

print("=" * 65)
print("EXPECTED IMMEDIATE REWARD CALCULATION")
print("=" * 65)

for state in states:
    print("\nCurrent State:", state)
    print("Number of Actions:", len(actions))

    for action in actions:

        expected_reward = 0
        expression = ""

        first = True

        for next_state, prob in P[(state, action)].items():
            reward = R[(state, action, next_state)]
            value = prob * reward
            expected_reward += value

            if not first:
                expression += " + "
            expression += f"({prob} × {reward})"
            first = False

        print("\nAction:", action)
        print("Calculation:")
        print("Expected Reward =", expression)
        print("= {:.2f}".format(expected_reward))

        summary.append([state, action, round(expected_reward, 2)])

# Summary Table
summary_df = pd.DataFrame(
    summary,
    columns=["Current State", "Action", "Expected Immediate Reward"]
)

print("\n" + "=" * 65)
print("OUTPUT SUMMARY TABLE")
print("=" * 65)
print(summary_df.to_string(index=False))
