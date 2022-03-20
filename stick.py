class ImpossibleMove(Exception):
    pass

class Stick:
    def __init__(self, place: int, max_count: int, disks: list = []) -> None:
        self.place = place
        self.disks = disks
        self.max_count = max_count
    
    def pop_disk(self):
        try:
            return self.disks.pop(0)
        except IndexError:
            print("Nothing to move")
    
    def insert_disk(self, disk):
        try:
            if not self.is_move_possible(disk):
                raise ImpossibleMove
            disk.place = len(self.disks)
            self.disks.insert(0, disk)
        except ImpossibleMove:
            print("Move is not possible")
            return disk
        
    def print_level(self, level):
        try:
            disk = next(filter(lambda x: x.place == level, self.disks))
            print("{: >10}".format(str(disk)), end ="")
        except StopIteration:
            print("{: >10}".format("|"), end ="")
    
    def is_move_possible(self, disk):
        try:
            return disk.size < self.disks[0].size
        except IndexError:
            return True