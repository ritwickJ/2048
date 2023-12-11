import matplotlib.pyplot as plt

# Your dictionary
data_dict = {4: 1, 8: 30, 16: 331, 32: 525, 64: 112, 128: 1}

# Extract keys (values) and values (frequencies) from the dictionary
values, frequencies = zip(*data_dict.items())
values_new = [str(a) for a in values]

# Plot the values and frequencies
plt.bar(values_new, frequencies)
plt.title('Value Frequencies')
plt.xlabel('Value')
plt.ylabel('Frequency')
# plt.grid(axis='y')
plt.show()