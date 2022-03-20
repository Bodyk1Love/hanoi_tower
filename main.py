from game import Game

HUMANIZED_MOVES = {
    1: 'first',
    2: 'second',
    3: 'third'
}

game = Game(4)
game.print_sticks()

while True:
    move_from = int(input("From: "))
    move_to = int(input("To: "))
    command = HUMANIZED_MOVES[move_from] + "_to_" + HUMANIZED_MOVES[move_to]
    eval("game." + command + "()")