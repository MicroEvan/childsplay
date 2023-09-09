import tkinter as tk
import random

# List of colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']

def change_color():
    # Generate random RGB values
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Convert RGB values to hexadecimal
    color = '#%02x%02x%02x' % (red, green, blue)
    
    # Change the window background color
    window.configure(bg=color)
    
    # Randomly select a color name
    color_name = random.choice(colors)
    
    # Create a label with the color name
    label.configure(text=color_name.upper(), fg=color_name, bg=color)
    
    # Schedule the next color change after 1 second
    window.after(1000, change_color)

# Create the main window
window = tk.Tk()

# Set the initial background color
#window.configure(bg='white')

# Set the window size
window.geometry('400x300')

# Create a label for the color name
label = tk.Label(window, text='', font=('Arial', 72))
label.pack(pady=50)

# Start changing colors
window.after(0, change_color)

# Run the main event loop
window.mainloop()