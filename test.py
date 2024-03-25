import tkinter as tk

def divide_rectangle():
    # Get user inputs
    main_width = float(main_width_entry.get())
    main_height = float(main_height_entry.get())
    num_pieces = int(num_pieces_entry.get())
    piece_width = float(piece_width_entry.get())
    piece_height = float(piece_height_entry.get())

    # Calculate the dimensions of each piece
    piece_area = (main_width * main_height) / num_pieces
    piece_width_calculated = piece_area / piece_height
    piece_height_calculated = piece_height

    # Create a canvas to display the pieces
    canvas.delete("all")
    for i in range(num_pieces):
        x1 = i * piece_width_calculated
        y1 = 0
        x2 = (i + 1) * piece_width_calculated
        y2 = piece_height_calculated
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

# Create the main window
root = tk.Tk()
root.title("Rectangle Divider")

# Create input fields and labels
main_width_label = tk.Label(root, text="Main Rectangle Width:")
main_width_entry = tk.Entry(root)
main_height_label = tk.Label(root, text="Main Rectangle Height:")
main_height_entry = tk.Entry(root)
num_pieces_label = tk.Label(root, text="Number of Pieces:")
num_pieces_entry = tk.Entry(root)
piece_width_label = tk.Label(root, text="Piece Width:")
piece_width_entry = tk.Entry(root)
piece_height_label = tk.Label(root, text="Piece Height:")
piece_height_entry = tk.Entry(root)

# Create a button to divide the rectangle
divide_button = tk.Button(root, text="Divide", command=divide_rectangle)

# Create a canvas to display the pieces
canvas = tk.Canvas(root, width=400, height=200)

# Grid layout
main_width_label.grid(row=0, column=0)
main_width_entry.grid(row=0, column=1)
main_height_label.grid(row=1, column=0)
main_height_entry.grid(row=1, column=1)
num_pieces_label.grid(row=2, column=0)
num_pieces_entry.grid(row=2, column=1)
piece_width_label.grid(row=3, column=0)
piece_width_entry.grid(row=3, column=1)
piece_height_label.grid(row=4, column=0)
piece_height_entry.grid(row=4, column=1)
divide_button.grid(row=5, column=0, columnspan=2)
canvas.grid(row=6, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
