import numpy as np
import matplotlib.pyplot as plt

# Define the cosine wave function
def cos_wave(t):
    return 7.4 * np.cos((4.16**-1)* t + np.pi)

# Create an array of time values
t_vals = np.arange(0, 25.89, 0.1)

# Calculate the values of the cosine wave for each time value
cos_vals = cos_wave(t_vals)

# Print the values of the cosine wave at every 10th time value
print("------------")
print(f"{cos_wave(25.89)}")
print("------------")

for i in range(0, len(t_vals), 10):
    print(f"The value of the cosine wave at time t={t_vals[i]:.2f} is {cos_vals[i]:.2f}")

# Generate a plot of the cosine wave
plt.plot(t_vals, cos_vals)
plt.title("Cosine Wave Plot")

plt.xticks(np.arange(0, 29, 1))
plt.yticks(np.arange(0, 7.4, 7.4))

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()