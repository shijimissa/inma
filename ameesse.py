import matplotlib.pyplot as plt

# Example data
epochs = [1, 2, 3, 4, 5]
loss_values = [0.1, 0.15, 0.08, 0.12, 0.05]

# Plotting
plt.plot(epochs, loss_values, marker='o')  # Example plot
plt.xlabel('Epochs')  # Set x-axis label
plt.ylabel('Loss')    # Set y-axis label
plt.title('Loss vs. Epochs')  # Set plot title
plt.grid(True)        # Show grid
plt.show()            # Display plot
