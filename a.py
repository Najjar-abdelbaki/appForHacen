import tkinter as tk

def divide_rectangle(width, height, piece_dimensions):
    # تحديد عدد القطع
    num_pieces = len(piece_dimensions)
    
    # إذا كانت عدد القطع 0 أو العرض أو الطول أقل من أي قطعة ممكنة
    if num_pieces == 0 or width < min(piece_dimensions, key=lambda x: x[0])[0] or height < min(piece_dimensions, key=lambda x: x[1])[1]:
        return []

    pieces = []
    x, y = 0, 0

    for i, (piece_width, piece_height) in enumerate(piece_dimensions):
        # إذا تجاوزت المستطيل
        if x >= width or y >= height:
            break
        
        # احتساب عدد القطع في الاتجاهين
        num_horizontal = min((width - x) // piece_width, num_pieces - i)
        num_vertical = min((height - y) // piece_height, num_pieces - i)
        
        # إضافة القطع
        for _ in range(num_horizontal):
            for _ in range(num_vertical):
                piece = {"x": x, "y": y, "width": piece_width, "height": piece_height}
                pieces.append(piece)
                y += piece_height
            x += piece_width
            y = 0
        
    return pieces

def restart_program():
    # إغلاق النافذة الحالية
    window.destroy()
    # إعادة تشغيل البرنامج
    start_program()

def on_button_click():
    width = int(entry_width.get())
    height = int(entry_height.get())
    num_pieces = int(entry_num_pieces.get())

    piece_dimensions = []
    for i in range(num_pieces):
        piece_width = int(entry_piece_width[i].get())
        piece_height = int(entry_piece_height[i].get())
        piece_dimensions.append((piece_width, piece_height))

    pieces = divide_rectangle(width, height, piece_dimensions)

    canvas.delete("all")

    scale = 20
    canvas.create_rectangle(20, 20, width*scale + 20, height*scale + 20, outline="black")

    for piece in pieces:
        x1 = 20 + piece["x"] * scale
        y1 = 20 + piece["y"] * scale
        x2 = x1 + piece["width"] * scale
        y2 = y1 + piece["height"] * scale
        canvas.create_rectangle(x1, y1, x2, y2, fill="gray", outline="black")

    for i, piece in enumerate(pieces):
        label_piece_info = tk.Label(text=f"Piece {i + 1}: ({piece['x']}, {piece['y']}) - Width: {piece['width']}, Height: {piece['height']}")
        label_piece_info.pack()

def start_program():
    global window, entry_width, entry_height, entry_num_pieces, entry_piece_width, entry_piece_height, canvas

    window = tk.Tk()
    window.title("Rectangle Division")

    tk.Label(window, text="Width:").grid(row=0, column=0)
    entry_width = tk.Entry(window)
    entry_width.grid(row=0, column=1)

    tk.Label(window, text="Height:").grid(row=1, column=0)
    entry_height = tk.Entry(window)
    entry_height.grid(row=1, column=1)

    tk.Label(window, text="Number of Pieces:").grid(row=2, column=0)
    entry_num_pieces = tk.Entry(window)
    entry_num_pieces.grid(row=2, column=1)

    canvas = tk.Canvas(window, width=500, height=500)
    canvas.grid(row=3, columnspan=3)

    button_divide = tk.Button(window, text="Divide Rectangle", command=on_button_click)
    button_divide.grid(row=4, column=0, columnspan=3)

    button_restart = tk.Button(window, text="Restart Program", command=restart_program)
    button_restart.grid(row=5, column=0, columnspan=3)

    window.mainloop()

start_program()
