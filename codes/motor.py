import matplotlib.pyplot as plt
import imageio

# Define the letters and their positions
letters = [
    ("T", 1), ("H", 2), ("A", 3), ("N", 4), ("K", 5),
    ("Y", 6), ("O", 7), ("U", 8)
]

# Create a list to store file names for each frame
file_names = []

# Create frames for each letter
for i, (letter, x) in enumerate(letters):
    plt.figure(figsize=(10, 6))
    plt.xlim(0, 10)
    plt.ylim(0, 6)
    plt.axis("off")
    
    # Add letters up to the current index
    for j in range(i + 1):
        char, xpos = letters[j]
        color = "blue" if xpos <= 5 else "red"
        plt.text(xpos, 5, char, fontsize=40, ha='center', va='center', color=color)
    
    # Save the frame as a temporary image
    file_name = f"/mnt/data/frame_{i}.png"
    plt.savefig(file_name)
    file_names.append(file_name)
    plt.close()

# Create the GIF
gif_file = "/mnt/data/thank_you.gif"
with imageio.get_writer(gif_file, mode="I", duration=0.5) as writer:
    for file_name in file_names:
        image = imageio.imread(file_name)
        writer.append_data(image)

# Cleanup: Remove temporary files (optional)
import os
for file_name in file_names:
    os.remove(file_name)

print(f"GIF created: {gif_file}")
