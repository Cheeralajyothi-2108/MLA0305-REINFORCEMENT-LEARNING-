import pandas as pd

# Reward Matrix
reward_data = {
    "Current State": ["S1", "S1", "S1", "S1",
                      "S2", "S2", "S2", "S2",
                      "S3", "S3", "S3", "S3"],
    
    "Action": ["A1", "A2", "A1", "A2",
               "A1", "A2", "A1", "A2",
               "A1", "A2", "A1", "A2"],
    
    "Next State": ["S2", "S2", "S3", "S3",
                   "S1", "S1", "S3", "S3",
                   "S1", "S1", "S2", "S2"],
    
    "Reward": [5, 10, -1, -5,
               3, 7, 2, 1,
               4, 6, 0, -2]
}

# Create DataFrame
reward_matrix = pd.DataFrame(reward_data)

# Display Reward Matrix
print("\nReward Matrix")
print(reward_matrix.to_string(index=False))
