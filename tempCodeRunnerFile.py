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