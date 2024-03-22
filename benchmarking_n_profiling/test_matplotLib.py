import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set equal scaling so the circle isn't distorted
ax.set_aspect('equal')

# Define a circle with center (x, y) = (0.5, 0.5) and radius 0.4
circle = patches.Circle((0.5, 0.5), 0.4, edgecolor='blue', facecolor='lightblue')

# Add the circle to the axes
ax.add_patch(circle)

# Set the axes limits so the circle is centered
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Display the plot
plt.show()
