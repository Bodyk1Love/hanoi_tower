from game import Game

game = Game(3)
game.print_sticks()

while True:
    inp = input("Command: ")
    eval("game." + inp)