user_cells = input()
new_cells = user_cells.replace("_", " ")
new_new_cells = list(new_cells)
matrix = []
k = 0


def board():
    global matrix
    print("---------")
    for i in range(0, 3):
        print("|", end="")
        for j in range(0, 3):
            print(" " + matrix[i][j], end="")
        print(" |")
    print("---------")


for i in range(0, 3):
    matrix.append([])
    for j in range(0, 3):
        matrix[i].append(new_new_cells[k])
        k += 1

board()

while True:
    x, y = input().split()
    try:
        x = int(x)
        y = int(y)
        if x < 1 or y > 3 or x < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if matrix[abs(x - 1)][abs(y - 1)] == " ":
                matrix[abs(x - 1)][abs(y - 1)] = "X"
                board()
                break
            else:
                print("This cell is occupied! Choose another one!")
    except:
        print("You should enter numbers!")
