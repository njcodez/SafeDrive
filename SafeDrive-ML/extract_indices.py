import numpy as np

# Example array
prediction = np.array([[0.1, 0.8, 0.3, 0.5]])

# Get the indices of the largest two values
largest_indices = np.argsort(prediction[0])[::-1][:2]

# Convert the indices to integers
largest_indices = largest_indices.astype(int)

print("Positions of the largest two values:", largest_indices)