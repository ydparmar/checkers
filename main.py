import turtle

restart = False
turtle.hideturtle()
turtle.speed(0)
storage_x = []
storage_y = []
storage_num = []
storage_square = []
storage_x_white = []
storage_y_white = []
storage_num_white = []
storage_square_white = []


# TODO: enable kings and jumping

def move(color, letter):
    if color == "white":
        if letter:
            letter = False
        else:
            letter = True
    turtle.penup()
    if color == "white":
        if letter:
            turtle.left(180)
        for i in range(2):
            turtle.forward(68)
            if letter:
                turtle.left(90)
            else:
                turtle.right(90)
    else:
        turtle.right(270)
        turtle.forward(68)
    if not letter and color == "white":
        turtle.backward(68)
    if letter:
        if color != "white":
            turtle.right(270)
            turtle.forward(68)
            turtle.left(180)
        turtle.forward(36)
        turtle.right(270)
    else:
        if color != "white":
            turtle.right(90)
            turtle.forward(136)
            turtle.left(180)
        turtle.forward(31)
        turtle.right(90)
    turtle.forward(5)
    turtle.right(90)


def check():
    global row, column, x, square_var, number, y
    position = turtle.pos()
    x = position[0]
    y = position[1]
    if -332 < x < -272:
        row = 0
    if -272 < x < -204:
        row = 1
    elif -204 < x < -136:
        row = 2
    elif -136 < x < -68:
        row = 3
    elif -68 < x < 0:
        row = 4
    elif 0 < x < 68:
        row = 5
    elif 68 < x < 136:
        row = 6
    elif 136 < x < 204:
        row = 7
    elif 204 < x < 272:
        row = 8
    elif 272 < x < 332:
        row = 9
    if -332 < y < -272:
        column = 0
    elif -272 < y < -204:
        column = 1
    elif -204 < y < -136:
        column = 2
    elif -136 < y < -68:
        column = 3
    elif -68 < y < 0:
        column = 4
    elif 0 < y < 68:
        column = 5
    elif 68 < y < 136:
        column = 6
    elif 136 < y < 204:
        column = 7
    elif 204 < y < 272:
        column = 8
    elif 272 < y < 332:
        column = 9

    square_var = [row, column]


def square():
    for a in range(4):
        turtle.forward(68)
        turtle.left(90)


# This function will draw a row of 10 circles.
def draw_square_row():
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    square()
    turtle.end_fill()
    turtle.penup()
    turtle.backward(68)


def draw_square_row_2():
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    square()
    turtle.end_fill()
    turtle.penup()
    turtle.backward(68)


def move_up_a_row():
    turtle.left(90)
    turtle.forward(68)
    turtle.right(90)
    turtle.forward(544)


turtle.penup()
turtle.setposition(200, -270)

for i in range(4):
    for j in range(2):
        if j == 0:
            for k in range(4):
                draw_square_row()
                draw_square_row_2()
        else:
            for g in range(4):
                draw_square_row_2()
                draw_square_row()
        move_up_a_row()


def piece(x, y, color, number, back, size, setup):
    global pum
    pum = number
    if x != "?":
        turtle.setposition(x, y)
    else:
        position = turtle.pos()
        x = position[0]
        y = position[1]
    check()
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(30)
    turtle.end_fill()
    turtle.color("black")
    turtle.penup()
    num = int(number)
    turtle.backward(back)
    if color == "blue":
        if setup:
            storage_x.append(x)
            storage_y.append(y)
            storage_num.append(num)
            storage_square.append(square_var)
        else:
            storage_x[old_pum - 1] = x
            storage_y[old_pum - 1] = y
            storage_num[old_pum - 1] = num
            storage_square[old_pum - 1] = square_var
    else:
        if setup:
            storage_x_white.append(x)
            storage_y_white.append(y)
            storage_num_white.append(num)
            storage_square_white.append(square_var)
        else:
            storage_x_white[old_pum - 1] = x
            storage_y_white[old_pum - 1] = y
            storage_num_white[old_pum - 1] = num
            storage_square_white[old_pum - 1] = square_var
    if size == 45:
        turtle.left(90)
        turtle.forward(5)
        turtle.right(90)
    turtle.write(number, True, font=("Arial", size, "normal"))


piece(-241, -131, "blue", "1", 15, 55, True)
piece(-105, -131, "blue", "2", 15, 55, True)
piece(31, -131, "blue", "3", 15, 55, True)
piece(167, -131, "blue", "4", 15, 55, True)
piece(-173, -199, "blue", "5", 15, 55, True)
piece(-37, -199, "blue", "6", 15, 55, True)
piece(99, -199, "blue", "7", 15, 55, True)
piece(235, -199, "blue", "8", 15, 55, True)
piece(-241, -267, "blue", "9", 15, 55, True)
piece(-105, -267, "blue", "10", 25, 45, True)
piece(31, -267, "blue", "11", 25, 45, True)
piece(167, -267, "blue", "12", 25, 45, True)
piece(235, 73, "white", "1", 15, 55, True)
piece(99, 73, "white", "2", 15, 55, True)
piece(-37, 73, "white", "3", 15, 55, True)
piece(-173, 73, "white", "4", 15, 55, True)
piece(167, 141, "white", "5", 15, 55, True)
piece(31, 141, "white", "6", 15, 55, True)
piece(-105, 141, "white", "7", 15, 55, True)
piece(-241, 141, "white", "8", 15, 55, True)
piece(235, 209, "white", "9", 15, 55, True)
piece(99, 209, "white", "10", 25, 45, True)
piece(-37, 209, "white", "11", 25, 45, True)
piece(-173, 209, "white", "12", 25, 45, True)
while True:
    for i in range(2):
        if i == 0:
            color = "blue"
        else:
            color = "white"
        if restart:
            restart = False
            continue
        pum = input(color + ": ")
        letter = pum[0]
        if letter == "b":
            back = True
            letter = pum[1]
        else:
            back = False
        for i in range(49):
            try:
                word_test = pum[i]
                total = i + 1
            except IndexError:
                break
        if total == 2:
            pum = pum[-1]
        elif total == 3:
            if pum[-2:] == 11 or 12 or 10:
                pum = pum[-2:]
            elif back:
                pum = pum[-1]
            else:
                print("Invalid command!")
                restart = True
                continue
        elif total == 4:
            if not back:
                print("Invalid command!")
                restart = True
                continue
            pum = pum[-2:]
        try:
            pum = int(pum)
        except ValueError:
            print("Invalid command!")
            restart = True
            continue
        turtle.showturtle()
        if letter == "l":
            letter = True
        elif letter == "r":
            letter = False
        if color == "white":
            turtle.left(180)
            if letter:
                letter = False
            else:
                letter = True
        if color == "white":
            turtle.setposition(storage_x_white[pum - 1], storage_y_white[pum - 1])
        else:
            turtle.setposition(storage_x[pum - 1], storage_y[pum - 1])
        turtle.showturtle()
        if letter:
            turtle.left(180)
            turtle.forward(68)
            turtle.right(90)
            turtle.forward(70)
        else:
            turtle.forward(68)
            turtle.left(90)
            turtle.forward(70)
        turtle.left(270)
        check()
        if color == "blue":
            if square_var == storage_square[0] or square_var == storage_square[1] or square_var == storage_square[2] \
                    or square_var == storage_square[3] or square_var == storage_square[4] or square_var == storage_square[5] \
                    or square_var == storage_square[6] or square_var == storage_square[7] or square_var == storage_square[8] \
                    or square_var == storage_square[9] or square_var == storage_square[10] or square_var == storage_square[11]:
                print("There is already a piece there.")
                restart = True
                continue
        else:
            if square_var == storage_square_white[0] or square_var == storage_square_white[1] or square_var == \
                    storage_square_white[2] \
                    or square_var == storage_square_white[3] or square_var == storage_square_white[4] or square_var == \
                    storage_square_white[5] \
                    or square_var == storage_square_white[6] or square_var == storage_square_white[7] or square_var == \
                    storage_square_white[8] \
                    or square_var == storage_square_white[9] or square_var == storage_square_white[10] or square_var == \
                    storage_square_white[11]:
                print("There is already a piece there.")
                restart = True
                continue
        if row == 9:
            print("This piece cannot go past the board!")
            restart = True
            continue
        if row == 0:
            print("This piece cannot go past the board!")
            restart = True
            continue
        if color == "blue":
            if column == 8:
                storage_num[pum - 1] = pum + 100
        else:
            if column == 1:
                storage_num_white[pum - 1] = pum + 100
        old_pum = pum
        if color == "blue":
            x = storage_x[pum - 1] - 36
            y = storage_y[pum - 1] - 5
        else:
            x = storage_x_white[pum - 1] - 36
            y = storage_y_white[pum - 1] - 5
        turtle.setposition(x, y)
        turtle.begin_fill()
        if color == "white":
            turtle.left(180)
        square()
        turtle.end_fill()
        move(color, letter)
        if old_pum != 10 and old_pum != 11 and old_pum != 12:
            piece("?", "?", color, str(old_pum), 15, 55, False)
        else:
            piece("?", "?", color, str(old_pum), 25, 45, False)

        last = input()
        if last == "end":
            turtle.clear()
            break
