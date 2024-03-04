import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def multiply_matrices():
    # Get vector from user input
    vector = np.array([float(entry_vector.get()), float(entry_vector2.get())])

    # Get matrix elements from user input
    matrix = np.array([[float(entry_matrix[0][0].get()), float(entry_matrix[0][1].get())],
                       [float(entry_matrix[1][0].get()), float(entry_matrix[1][1].get())]])

    # Perform matrix multiplication
    result_vector = np.dot(vector,matrix)

    # Display result vector
    result_label.config(text="Result Vector: {}".format(result_vector))

    # Clear previous plot, if any
    if hasattr(multiply_matrices, 'canvas'):
        multiply_matrices.canvas.get_tk_widget().destroy()

    # Plot the vectors
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector')
    ax.quiver(0, 0, result_vector[0], result_vector[1], angles='xy', scale_units='xy', scale=1, color='b', label='Result')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.legend()
    ax.set_title('Vector Multiplication')

    # Embed the plot in tkinter window
    multiply_matrices.canvas = FigureCanvasTkAgg(fig, master=window)
    multiply_matrices.canvas.draw()
    multiply_matrices.canvas.get_tk_widget().grid(row=7, columnspan=4)

# Create tkinter window
window = tk.Tk()
window.title("Matrix-Row Vector Multiplication")

# Vector input
label_vector = tk.Label(window, text="X")
label_vector.grid(row=0, column=0)
label_vector2 = tk.Label(window, text="Y")
label_vector2.grid(row=0, column=1)
entry_vector = tk.Entry(window)
entry_vector.grid(row=1, column=0)
entry_vector2 = tk.Entry(window)
entry_vector2.grid(row=1, column=1)

# Matrix input
label_matrix = tk.Label(window, text="Matrix")
label_matrix.grid(row=2, column=0)
entry_matrix = [[tk.Entry(window) for _ in range(2)] for _ in range(2)]
for i in range(2):
    for j in range(2):
        entry_matrix[i][j] = tk.Entry(window)
        entry_matrix[i][j].grid(row=i+3, column=j+1)

# Button to calculate
calculate_button = tk.Button(window, text="Calculate", command=multiply_matrices)
calculate_button.grid(row=4, column=3)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=5, columnspan=4)

window.mainloop()
