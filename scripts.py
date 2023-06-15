grid = list(range(1, 10))

def show_grid(grid): #визуализируем решетку
    print("Cхема поля:")
    print("---------")
    for i in range(3):
        print("|", grid[i*3+0], grid[i*3+1], grid[i*3+2], "|")
    print("---------")


def victory_check(grid): #проверка на победу
    win_combination =   ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_combination:
        if grid[each[0]] == grid[each[1]] == grid[each[2]]:
            return grid[each[0]]
    return False

def try_input(playern):
    noterror = False
    while not noterror:
        print("Введите номер еще не битого поля.")
        player_input = input("Ход за " + playern + ": ")
        try:
            player_input = int(player_input)
        except ValueError:
            print("Введите целое число!")
            continue
        if 1 <= player_input <= 9:
            if str(grid[player_input - 1]) not in "XO":
                grid[player_input - 1] = playern
                noterror = True
            else:
                print("Поле бито, выберите номер еще раз.")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

iter = int("0")
victory = False
while not victory:
    show_grid(grid)
    if iter % 2 == 0:
        try_input("X")
    else:
        try_input("O")
    iter += 1
    tmp = victory_check(grid)
    if tmp:
        print("Игрок за", tmp, "выиграл!")
        victory = True
        break
    if iter == 9:
        print("Ничья!")
        break
