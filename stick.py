class Stick:
    def __init__(self, place: int, disks: list = []) -> None:
        self.place = place
        self.disks = disks
        
    def print_level(self, level):
        if level <= len(self.disks) - 1:
            print("{: >10}".format(str(self.disks[level])), end ="")
        else:
            print("{: >10}".format("|"), end ="")