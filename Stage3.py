def board(inp):
    print("---------")
    print("|", " ".join(inp[0:3]), "|")
    print("|", " ".join(inp[3:6]), "|")
    print("|", " ".join(inp[6:9]), "|")
    print("---------")


def winner(inp, var):
    win = []
    for x in wins:
        win.append(len([y for y in x if inp[y] == var]))
    return win.count(3)


init = list(input().replace(" ", "_"))
board(init)

wins = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

x_win = winner(init, "X")
y_win = winner(init, "O")

if abs(init.count("X") - init.count("O")) >= 2 or (x_win == 1 and y_win == 1):
    print("Impossible")
elif x_win == 1:
    print("X wins")
elif y_win == 1:
    print("O wins")
elif x_win == 0 and y_win == 0 and init.count("_") != 0:
    print("Game not finished")
else:
    print("Draw")
