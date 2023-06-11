import os
from PIL import Image
import matplotlib
import math
matplotlib.use('agg')
import matplotlib.pyplot as plt
import string
import tkinter as tk
from tkinter import ttk, filedialog

grid_size = 0  # Global variable to store the grid size
show_legend = False
image_paths = []

def select_images():
    global image_paths  # Access the global image_paths variable
    image_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=(("JPEG Files", "*.jpeg"), ("PNG Files", "*.png")))
    image_paths = list(image_paths)
    return image_paths

def select_images():
    global image_paths
    filetypes = (("Image Files", ("*.jpeg", "*.jpg", "*.png", "*.bmp")),)  # Specify multiple file types
    image_paths = filedialog.askopenfilenames(title="Select Image Files", filetypes=filetypes)
    image_paths = list(image_paths)
    return image_paths


def run(image_paths):
    if image_paths:
        display_images(image_paths)
    else:
        print("Empty image paths")

def display_images(image_paths):
    alphabet = list(string.ascii_lowercase)
    global grid_size
    # Clear the existing figure
    plt.clf()

    # Calculate the number of images
    num_images = len(image_paths)
    num_rows = math.ceil(num_images / grid_size)
    # Create the grid layout for the images
    if num_images < grid_size:
        grid_size = num_images
    fig, axes = plt.subplots(num_rows, grid_size, figsize=(10, 10))

    # Iterate over the image paths and plot each image
    for i, image_path in enumerate(image_paths):
        # Load the image
        image = Image.open(image_path)

        # Calculate the row and column index for the subplot
        row = i // grid_size
        col = i % grid_size

                # Plot the image
        if num_rows > 1:
            axes[row, col].imshow(image)
            axes[row, col].axis('off')
            if show_legend:
                # Add label below each image
                axes[row, col].text(0.5, -0.1, "("  + alphabet[i] + ")", transform=axes[row, col].transAxes,
                                ha='center', va='center')
                
        else:
            axes[col].imshow(image)
            axes[col].axis('off')
            if show_legend:
                # Add label below each image
                axes[col].text(0.5, -0.1, "(" + alphabet[i] + ")", transform=axes[col].transAxes,
                                ha='center', va='center')
                # axes[col].text(0.5, -0.1, "(" + str(row) + "," + str(col) + ")", transform=axes[col].transAxes,
                #                 ha='center', va='center')

        # # Plot the image
        # axes[row, col].imshow(image)
        # axes[row, col].axis('off')

        # if show_legend:
        #     # Add label below each image
        #     if num_rows > 1:
        #         axes[row, col].text(0.5, -0.1, "(" + alphabet[i] + ")", transform=axes[row, col].transAxes,
        #                     ha='center', va='center')
        #     else:
        #         axes[col].text(0.5, -0.1, "(" + alphabet[i] + ")", transform=axes[col].transAxes,
        #                     ha='center', va='center')
    # Hide empty subplots
    for i in range(num_images, grid_size * num_rows):
        row = i // grid_size
        col = i % grid_size
        if num_rows > 1:
            axes[row, col].axis('off')
        else:
            axes[col].axis('off')

    # Adjust spacing between subplots
    plt.tight_layout()

    # Save the plot to an image file
    output_file = "image_grid.png"
    plt.savefig(output_file)
    plt.close()

    # Display a message with the output file path
    result_label.config(text=f"Image grid saved to {output_file}")


def process_input():
    select_images()


def process_input2():
    global grid_size  # Access the global grid size variable
    global show_legend
    try:
        grid_size = int(grid_size_entry.get())
        if grid_size > 0:
            show_legend = show_legend_var.get()  # Get the value of the checkbox
            run(image_paths)
        else:
            result_label.config(text="Please enter a positive integer for grid size.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a positive integer for grid size.")


# Create a tkinter GUI window
window = tk.Tk()
window.title("Image Grid")

# Create a label and buttons
label = ttk.Label(window, text="Image Grid", font=("Helvetica", 16))
label.pack(pady=10)

grid_size_label = ttk.Label(window, text="Grid Size:")
grid_size_label.pack()

grid_size_entry = ttk.Entry(window)
grid_size_entry.pack()

show_legend_var = tk.BooleanVar(value=True)
legend_checkbox = ttk.Checkbutton(window, text="Show Legend", variable=show_legend_var)
legend_checkbox.pack()

process_button = ttk.Button(window, text="Search file", command=process_input)
process_button.pack(pady=5)

process_button2 = ttk.Button(window, text="Run", command=process_input2)
process_button2.pack(pady=5)

result_label = ttk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=5)

# Start the tkinter event loop
window.mainloop()
