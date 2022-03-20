from game import Game
import sys

HUMANIZED_MOVES = {
    1: 'first',
    2: 'second',
    3: 'third'
}

class NumberError(Exception):
    pass

disk_count = None
while not disk_count:
    try:
        disk_count = int(input("Enter number of disks (min 3 max 10): "))
        if not 3 <= disk_count <= 10:
            raise NumberError
    except ValueError:
        print("Enter a number!")
    except NumberError:
        disk_count = None
        print("Enter a number between 3 and 10")
    except KeyboardInterrupt:
        print("Bye-bye!")
        sys.exit()

game = Game(disk_count)

while True:
    try:
        move_from = int(input("From: "))
        move_to = int(input("To: "))
        command = HUMANIZED_MOVES[move_from] + "_to_" + HUMANIZED_MOVES[move_to]
        eval("game." + command + "()")
    except AttributeError:
        print("Impossible move to itself")
    except ValueError:
        print("Enter a number!")
    except KeyError:
        print("The move is out of range 1-3")
    except KeyboardInterrupt:
        print("Bye-bye!")
        sys.exit()