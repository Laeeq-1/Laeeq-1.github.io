import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Create components of the device
pipe_in = patches.FancyBboxPatch((0, 2.5), 2, 1, boxstyle="round,pad=0.1", color="blue", alpha=0.6)
pipe_out = patches.FancyBboxPatch((8, 2.5), 2, 1, boxstyle="round,pad=0.1", color="blue", alpha=0.6)
device_body = patches.FancyBboxPatch((2, 2), 6, 2, boxstyle="round,pad=0.2", color="gray", alpha=0.8)

# Add components to the plot
ax.add_patch(pipe_in)
ax.add_patch(pipe_out)
ax.add_patch(device_body)

# Water flow as a circle
water_circle = patches.Circle((1, 3), 0.2, color="cyan", alpha=0.7)
ax.add_patch(water_circle)

# Chemical reaction indicator
reaction_box = patches.Rectangle((4, 2.5), 2, 1, color="green", alpha=0.5)
ax.add_patch(reaction_box)
reaction_text = ax.text(5, 3, "Testing", color="white", ha="center", va="center", fontsize=10, alpha=0)

# Result display text
result_text = ax.text(5, 4.5, "", color="red", ha="center", fontsize=12)

# Animation update function
def update(frame):
    # Move water circle through the device
    if frame < 20:
        water_circle.center = (1 + frame * 0.3, 3)
    elif frame < 40:
        water_circle.center = (7, 3)
        reaction_text.set_alpha(1)  # Show testing text
    else:
        reaction_text.set_alpha(0)  # Hide testing text
        if frame < 60:
            result_text.set_text("Legionella Detected!")  # Example result
        else:
            result_text.set_text("Water is Not Safe!")

    return water_circle, reaction_text, result_text

# Create the animation
anim = FuncAnimation(fig, update, frames=80, interval=100, blit=True)

# Save the animation as an MP4 video
anim.save("waterwise_simulation.gif", writer="pillow", fps=10)


print("Animation saved as 'waterwise_simulation.gif'")
