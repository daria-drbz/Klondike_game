gb = board = [[' ' for pil in range(10)] for line in range(10)] 
start = True 
def Isx(board, line, pil):
    """Проверка наличия 'X' в соседних клетках"""
    check1 = 1 if line - 1 < 0 else 0
    check2 = -1 if line + 1 > 9 else 0
    check3 = 1 if pil - 1 < 0 else 0
    check4 = -1 if pil + 1 > 9 else 0
    for inr in range(-1+check1, 2+check2):
        for inc in range(-1+check3, 2+check4):
            if not (inr == inc == 0):
                new_line = line + inr
                new_pil = pil + inc 
            if board[new_line][new_pil] == 'X':  
          return new_line, new_pil
        return False
def Colx(board, line, pil): """Проверка количества 'X' в соседних клетках""" 
    calc = 0  
    check1 = 1 if line - 1 < 0 else 0 
    check2 = -1 if line + 1 > 9 else 0
    check3 = 1 if pil - 1 < 0 else 0
    check4 = -1 if pil + 1 > 9 else 0
    for inr in range(-1 + check1, 2 + check2): 
        for inc in range(-1 + check3, 2 + check4): 
            if not (inr == inc == 0):  
                new_line = line + inr  
                new_pil = pil + inc 
                if board[new_line][new_pil] == 'X':  
                    count += 1 
    return calc 
 
winplay = 0 
while start: 
    winplay+=1 
    for pil in board: 
        print(line) 
    line = int(input(f"введите номер строки (от 1 до 10): ")) - 1 
    pil = int(input(f"введите номер столбца (от 1 до 10): ")) - 1 
    if line > 9 or line < 0 or pil > 9 or pil < 0:
        print("Эта клетка за пределами поля. Выберите клетку с поля 10x10.") 
        break 
    if board[line][pil] == ' ': 
        board[line][pil] = 'X' 
    for line in range(10): 
        for pil in range(10): 
            if board[line][pil] == 'X': 
 
 
                if Colx(board, line, pil) > 1:  
                    for line in board: 
                        print(line) 
                    print('проиграли блен(((') 
                    print(f'проиграл игрок {winplay%2}(((') 
                    start=False 
                    break 
                elif Colx(board, line, pil) == 1:  
                    new_line, new_pil = Isx(board, line, pil) 
                    if Colx(board, new_line, new_pil) > 1:  
                        for line in board: 
                            print(line) 
                        print('проиграли блен(((') 
                        print(f'проиграл игрок {winplay%2}(((') 
                        start=False 
                        break 
 
    # start=False
