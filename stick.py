class Stick:
    def __init__(self, place: int, disks: list) -> None:
        self.place = place
        self.disks = disks or ['|'] * 3
        
    def print_level(self, level):
        print("{: >10}".format(str(self.disks[level])), end ="")