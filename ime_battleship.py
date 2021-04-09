import turtle
from sys import exit
from random import randint

# setup
player_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    (-150, -330),
]
enemy_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    (-150, 30),
]
player_fleet = [
    ["Patrol Boat", ["k0", "k0"], [1, 1], False],
    ["Destroyer", ["k0", "k0", "k0"], [1, 1, 1], False],
    ["Cruiser", ["k0", "k0", "k0", "k0"], [1, 1, 1, 1], False],
    ["Battleship", ["k0", "k0", "k0", "k0", "k0"], [1, 1, 1, 1, 1], False],
    ["Submarine", ["k0", "k0", "k0"], [1, 1, 1], False],
]
enemy_fleet = [
    ["Patrol Boat", ["k0", "k0"], [1, 1], False],
    ["Destroyer", ["k0", "k0", "k0"], [1, 1, 1], False],
    ["Cruiser", ["k0", "k0", "k0", "k0"], [1, 1, 1, 1], False],
    ["Battleship", ["k0", "k0", "k0", "k0", "k0"], [1, 1, 1, 1, 1], False],
    ["Submarine", ["k0", "k0", "k0"], [1, 1, 1], False],
]
player_guesses, enemy_guesses = [], []
enemy_brain = [
    ["k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0"],
    ["k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0"]
]

def draw_menu(anchor):
    turtle.goto(anchor)


def print_board(board):
    for row in board:
        print(row)
    print()


def reset_board(board):
    for i in range(0, 10):
        board[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def index_to_tag(row, col):
    tag = ""
    tag += chr(65 + row)
    tag += str(col + 1)
    return tag


def check_tile(board, tag):
    # unpack tag into alphabetical and numerical component
    tag_let = tag[0]
    tag_num = int(tag[1:])

    # check board state at corresponding index
    row = ord(tag_let) - 65
    col = tag_num - 1
    tile_state = board[row][col]
    return tile_state


def change_tile(board, tag, value):
    # unpack tag into alphabetical and numerical component
    tag_let = tag[0]
    tag_num = int(tag[1:])

    # check board state at corresponding index
    row = ord(tag_let) - 65
    col = tag_num - 1
    board[row][col] = value


def draw_menu():
    turtle.showturtle()
    turtle.hideturtle()
    turtle.pensize(1)
    turtle.color("white")
    turtle.speed(0)
    ts = turtle.getscreen()
    ts.bgcolor("black")
    turtle.write("WELCOME TO BATTLESHIP", font=("Impact", 70, "normal"), align="Center")


def draw_legend(anchor, title, color):
    # unpack anchor coordinates
    x, y = anchor[0], anchor[1]
    turtle.penup()

    # Write title
    turtle.goto(x - 2, y + 300)
    turtle.color(color)
    turtle.write(title, font=("Impact", 20, "normal"), align="right")
    turtle.color("black")

    # Write alphabetical, horizontal coordinate axis
    turtle.goto(x + 15, y + 300)
    turtle.setheading(0)
    turtle.color("white")
    for i in range(10):
        turtle.write(str(i + 1), align="center", font=("Impact", 20, "normal"))
        turtle.forward(30)

    # Write numerical, vertical coordinate axis
    turtle.goto(x - 20, y + 268)
    turtle.setheading(-90)
    for i in range(10):
        turtle.write(chr(65 + i), align="center", font=("Impact", 20, "normal"))
        turtle.forward(30)
    turtle.setheading(0)


def draw_reset_sea(board, fleet, anchor):
    # unpack anchor coordinates
    x, y = anchor[0], anchor[1]
    turtle.penup()
    turtle.goto(x, y)

    turtle.pendown()
    turtle.seth(90)
    turtle.color("black")
    turtle.fillcolor("light blue")
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.fd(300)
        turtle.rt(90)
    turtle.end_fill()
    turtle.seth(90)

    for i in range(1, 10):
        turtle.penup()
        turtle.goto(x + (30 * i), y)
        turtle.pendown()
        turtle.fd(300)
    turtle.seth(0)
    for i in range(1, 10):
        turtle.penup()
        turtle.goto(x, y + (30 * i))
        turtle.pendown()
        turtle.fd(300)


def add_boat(ship_length, fleet_index, board, fleet):
    ship_direction = randint(0, 1)
    blocked = False
    if ship_direction == 0:
        row = randint(0, 9)
        col = randint(0, 10 - ship_length)
        for i in range(0, ship_length):
            if board[row][col + i] == 1:
                blocked = True
        if not blocked:
            for n in range(0, ship_length):
                board[row][col + n] = 1
                fleet[fleet_index][1][n] = index_to_tag(row, col + n)
            if board[10] == (-150, -330):
                draw_ship(board[10], ship_length, ship_direction, (row, col))
        elif blocked:
            add_boat(ship_length, fleet_index, board, fleet)

    elif ship_direction == 1:
        row = randint(0, 10 - ship_length)
        col = randint(0, 9)
        for i in range(0, ship_length):
            if board[row + i][col] == 1:
                blocked = True
        if not blocked:
            for n in range(0, ship_length):
                board[row + n][col] = 1
                fleet[fleet_index][1][n] = index_to_tag(row + n, col)
            if board[10] == (-150, -330):
                draw_ship(board[10], ship_length, ship_direction, (row, col))
        elif blocked:
            add_boat(ship_length, fleet_index, board, fleet)


def how_to_play():
    draw_menu()
    print("""
    HOW TO PLAY:
        If you already know how to play the board game BATTLESHIP, skip
        to the section called "TAKING YOUR TURN." 
        
        Your goal is to sink the enemy fleet. The enemy fleet is located
        in the enemy sea. Each ship of the enemy (and your) fleet occupy
        a certain number of tiles. To sink a ship, you must shoot each 
        of its tiles once. Sink the entire enemy fleet to win. 
        
        The locations of the enemy ships are hidden. Use
        critical thinking and luck to determine the location of enemy
        ships and SHOOT AT THOSE TILES. Shooting a tile that contains an
        enemy ship highlights that tile in RED. Shooting a tile that
        does not contain an enemy ship highlights that tile WHITE.
        
     -> TAKING YOUR TURN <-
        On your turn, you may shoot at the enemy sea once for each of
        your ships that is still afloat.
        
        Do this by typing with your keyboard to specify which tile you 
        wish to shoot at. Typing J10 followed by [ENTER] will shoot at
        tile J10 of the enemy sea. Likewise, typing A1 followed by 
        [ENTER] will shoot at tile A1 of the enemy sea. 
        
        After each of your turns, the enemy will take one turn. The
        enemy will shoot at your sea and attempt to sink your fleet.
        Don't let the enemy win!
        
        Good luck.
        Press [ENTER] to continue.
        """)
    input("")
    turtle.clear()
    print("LOADING")


def setup_board_and_fleet(board, fleet, is_player):
    if is_player:
        draw_reset_sea(board, fleet, (-150, -330))
    else:
        draw_reset_sea(board, fleet, (-150, 30))
    for i in range(2, 6):
        add_boat(i, i - 2, board, fleet)
    add_boat(3, 4, board, fleet)


def update_game_state():
    for ship in player_fleet:
        if ship[3]:
            for tag in ship[1]:
                change_tile(player_board, tag, 5)
    for ship in enemy_fleet:
        if ship[3]:
            for tag in ship[1]:
                change_tile(enemy_board, tag, 5)
    sum = 0
    for ship in player_fleet:
        if ship[3]:
            sum += 1
    if sum == 5:
        print("*" * 25, "\nThe enemy sunk your fleet!\nGAME OVER")
        exit()
    sum = 0
    for ship in enemy_fleet:
        if ship[3]:
            sum += 1
    if sum == 5:
        print("*" * 25, "\nYou sunk the enemy fleet!\nYOU WIN")
        exit()


def reset_enemy_brain():
    del enemy_brain[:]
    for i in range(0, 2):
        enemy_brain.append([
            "k0", "k0", "k0", "k0", "res", "k0", "k0", "k0", "k0"
        ])
    enemy_brain[1][4] = "k0"


def tag_to_xy(anchor, tag):
    x = ((int(tag[1:]) - 1) * 30) + anchor[0]
    y = anchor[1] + 300 - ((ord(tag[0]) - 65) * 30)
    # DEBUG print(x, y)
    return (x, y)


def update_tile_ui(anchor, tag, color):
    turtle.color("black")
    turtle.fillcolor(color)
    turtle.penup()

    # fill square
    turtle.goto(tag_to_xy(anchor, tag))
    turtle.seth(0)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.fd(30)
        turtle.rt(90)
    turtle.penup()
    turtle.end_fill()




def draw_ship(anchor, size, direction, index_coords):
    # anchor is the tuple coordinates of the up-left corner of the anchor tile
    # size is the size of the ship in tiles (ex: 2)
    # direction is either 0 for horizontal or 1 for vertical
    # sea_scale should be equivalent to the scaling_factor value of the sea onto which the ship is being placed

    # unpack anchor coordinates
    x, y = anchor[0], anchor[1]
    row, col = index_coords[0], index_coords[1]
    length_step = (size * 30) / 6
    turtle.penup()

    if direction == 0:
        # draw horizontal ship

        # 285 is length of board minus half a tile
        # ... so that bow of ship is in middle of tile
        turtle.goto(x + (30 * col), y + 285 - (row * 30))
        turtle.color("black")
        turtle.fillcolor("grey")
        turtle.pensize(3)
        turtle.pendown()
        turtle.begin_fill()

        # draw ship as a combination of 4 parabolic curves
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx + length_step, cury + (15 / (2 ** i)))
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx + length_step, (cury - (15 / (2 ** (4 - i)))))
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx - length_step, cury - (15 / (2 ** i)))
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx - length_step, (cury + (15 / (2 ** (4 - i)))))
    elif direction == 1:
        # draw vertical ship

        turtle.goto(x + 15 + (col * 30), y + 300 - (row * 30))
        turtle.color("black")
        turtle.fillcolor("grey")
        turtle.pensize(3)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx + (15 / (2 ** i)), cury - length_step)
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx - (15 / (2 ** (4 - i))), cury - length_step)
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx - (15 / (2 ** i)), cury + length_step)
        for i in range(1, 4):
            curx = turtle.xcor()
            cury = turtle.ycor()
            turtle.goto(curx + (15 / (2 ** (4 - i))), (cury + length_step))
    turtle.end_fill()
    turtle.penup()
    turtle.color("white")
    turtle.pensize(1)


def enemy_guess():
    if enemy_brain[0][4] == "k0":
        # Before entering search mode, check for crumbs
        net_reds, justified_reds, crumbs = [], [], []
        # get list of reds that the ai sees
        for n in range(0, len(player_board) - 1):
            for i in range(0, 10):
                if player_board[n][i] == 4:
                    net_reds.append(index_to_tag(n, i))
        # get list of reds that the ai SHOULD see based on how many ships it sank
        for ship in player_fleet:
            if ship[3]:
                for tag in ship[1]:
                    justified_reds.append(tag)
        # identify crumbs
        if not len(net_reds) == len(justified_reds):
            for tag in net_reds:
                if tag not in justified_reds:
                    enemy_brain[0][4] = tag
                    val = enemy_guess()
                    return val
        # If no crumbs found, enter search mode
        while True:
            tag_let = chr(65 + randint(0, 9))
            tag_num = str(randint(1, 10))
            tag = tag_let + tag_num
            if tag not in enemy_guesses:
                return tag
    else:
        # unpack pivot and reset possibility axes
        pivot = enemy_brain[0][4]
        pivot_let = enemy_brain[0][4][0]
        pivot_num = int(enemy_brain[0][4][1:])
        reset_enemy_brain()
        enemy_brain[0][4] = pivot

        # get maximum evaluation range; equivalent to the length of the largest non-sunk player vessel
        eval_range = 2
        for ship in player_fleet:
            if not ship[3] and len(ship[2]) > eval_range:
                eval_range = len(ship[2])

        exclude_horz = False
        exclude_vert = False
        # evaluate possibilities on axis 12:00
        for i in range(1, eval_range):
            # check if out of board bounds
            poss_let_raw = ord(pivot_let) - i
            if poss_let_raw < 65:
                break
            # check if is previous miss
            poss = chr(poss_let_raw) + str(pivot_num)
            if check_tile(player_board, poss) == 3 or check_tile(player_board, poss) == 5:
                break
            if check_tile(player_board, poss) == 4:
                # DEBUG print("excluding horz")
                exclude_horz = True
                continue
            enemy_brain[1][i - 1] = poss
            break
        # evaluate possibilities on axis 3:00
        for i in range(1, eval_range):
            # check if out of board bounds
            poss_num = pivot_num + i
            if poss_num > 10:
                break
            # check if is previous miss
            poss = pivot_let + str(poss_num)
            if check_tile(player_board, poss) == 3 or check_tile(player_board, poss) == 5:
                break
            if check_tile(player_board, poss) == 4:
                # DEBUG print("excluding vert")
                exclude_vert = True
                continue
            enemy_brain[0][4 + i] = poss
            break
        # evaluate possibilities on axis 6:00
        for i in range(1, eval_range):
            # check if out of board bounds
            poss_let_raw = ord(pivot_let) + i
            if poss_let_raw > 74:
                break
            # check if is previous miss
            poss = chr(poss_let_raw) + str(pivot_num)
            if check_tile(player_board, poss) == 3 or check_tile(player_board, poss) == 5:
                break
            if check_tile(player_board, poss) == 4:
                # DEBUG print("excluding horz")
                exclude_horz = True
                continue
            enemy_brain[1][4 + i] = poss
            break
        # evaluate possibilities on axis 9:00
        for i in range(1, eval_range):
            # check if out of board bounds
            poss_num = pivot_num - i
            if poss_num < 1:
                break
            # check if is previous miss
            poss = pivot_let + str(poss_num)
            if check_tile(player_board, poss) == 3 or check_tile(player_board, poss) == 5:
                break
            if check_tile(player_board, poss) == 4:
                # DEBUG print("excluding vert")
                exclude_vert = True
                continue
            enemy_brain[0][i - 1] = poss
            break

        # guessing time
        temp_list = []
        if not exclude_horz:
            for tag in enemy_brain[0]:
                if tag != "k0" and tag != pivot:
                    temp_list.append(tag)
        if not exclude_vert:
            for tag in enemy_brain[1]:
                if tag != "k0" and tag != pivot:
                    temp_list.append(tag)
        # DEBUG print("temp list: ", temp_list)
        if len(temp_list) == 0:
            for axis in enemy_brain:
                for tag in axis:
                    if tag != "k0" and tag != pivot:
                        temp_list.append(tag)
            # DEBUG print("Revised temp list:", temp_list)
        return temp_list[randint(0, len(temp_list) - 1)]


def take_turn(is_player, skip, guess_list, target_board, target_fleet):
    if not skip:
        print("Use your keyboard to specify which enemy tile you wish "
              "to shoot at.")
    if is_player:
        user_in = (input("").strip()).upper()
    if not is_player:
        user_in = enemy_guess()

    # check format of user input
    if is_player:
        if user_in.casefold() == "quit":
            user_in = input("[+] Press [ENTER] to quit.\n[+] Type NO then press [ENTER] to cancel.\n")
            if user_in == "":
                exit()
            else:
                take_turn(is_player, False, guess_list, target_board, target_fleet)
                return
        if user_in == "" or len(user_in) == 1:
            print("Invalid input. Try typing something like A1 or J10.")
            take_turn(is_player, True, guess_list, target_board, target_fleet)
            return
        if 3 < len(user_in) < 2 or not user_in[0].isalpha() or not user_in[1].isdigit() or 1 > int(user_in[1]) > 9 or ord(user_in[0]) > 74:
            print("Invalid input. Try typing something like A1 or J10.")
            take_turn(is_player, True, guess_list, target_board, target_fleet)
            return
        elif len(user_in) > 2:
            if user_in[1] != "1" or user_in[2] != "0":
                print("Invalid input. Try typing something like A1 or J10.")
                take_turn(is_player, True, guess_list, target_board, target_fleet)
                return

    # check if this tile has already been guessed
    if user_in in guess_list and is_player:
        print(f"You already shot at {user_in}! Try a different tile.")
        take_turn(is_player, True, guess_list, target_board, target_fleet)
        return
    guess_list.append(user_in)

    # shoot at the corresponding enemy tile
    result = check_tile(target_board, user_in)
    if result == 0:
        change_tile(target_board, user_in, 3)
        if is_player:
            print("Miss!")
        else:
            print(f"The enemy shoots at your tile {user_in} and hits nothing.")
        update_tile_ui(target_board[10], user_in, "white")
    elif result == 1:
        if is_player:
            print("Hit!")
        update_tile_ui(target_board[10], user_in, "red")
        change_tile(target_board, user_in, 4)
        # identify which ship has been hit and update data accordingly
        for ship in target_fleet:
            if user_in in ship[1]:
                if not is_player:
                    print(f"The enemy shoots at your tile {user_in} and hits your {ship[0]}.")
                # update ship damage state
                i = ship[1].index(user_in)
                ship[2][i] = 0
                # check if ship is still afloat and update its 'sunk' boolean as necessary
                sum = 0
                for hitpoint in ship[2]:
                    sum += hitpoint
                if sum == 0:
                    ship[3] = True
                    if not is_player:
                        print(f"Your {ship[0]} has sunk!")
                        reset_enemy_brain()
                    else:
                        print(f"The enemy {ship[0]} is sleeping with the fishes!")
        # ai controls
        if not is_player:
            # if ai is in search mode, set ai to kill mode
            if enemy_brain[0][4] == "k0":
                enemy_brain[0][4] = user_in
            # if ai just sunk a boat, set ai to search mode
            elif enemy_brain[0][4] == "res":
                enemy_brain[0][4] = "k0"

    # update the game stats
    update_game_state()


# BEGIN PROGRAM --------------------------------------------------------

# Display the "how to play" menu
how_to_play()

# setup legends
draw_legend((-150, -330), "YOUR SEA", "Green")
draw_legend((-150, 30), "ENEMY SEA", "Red")

# setup boards and fleets
setup_board_and_fleet(player_board, player_fleet, True)
setup_board_and_fleet(enemy_board, enemy_fleet, False)
print("FINISHED")

# Let player choose fleet layout.
while True:
    user_in = str(input("[+] Press [ENTER] to use this fleet.\n[+]"
                        " Type NO then press [ENTER] to generate a"
                        " different fleet.\n: "))
    if user_in == "":
        break
    else:
        print("LOADING")
        reset_board(player_board)
        setup_board_and_fleet(player_board, player_fleet, True)
        print("FINISHED")

# start the game
while True:
    print("YOUR TURN")
    for ship in player_fleet:
        if not ship[3]:
            take_turn(True, False, player_guesses, enemy_board, enemy_fleet)
    print("ENEMY TURN")
    for ship in enemy_fleet:
        if not ship[3]:
            take_turn(False, True, enemy_guesses, player_board, player_fleet)

