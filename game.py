from telnetlib import GA
from disk import Disk
from stick import Stick
from itertools import permutations

HUMANIZED_INDEXES = {
    0: 'first',
    1: 'second',
    2: 'third'
}

class Game:
    def __init__(self, disk_count) -> None:
        self.disk_count = disk_count
        self.sticks = self.__initialize_sticks()
        
    def print_sticks(self):
        for i in range(self.disk_count - 1, -1, -1):
            for stick in self.sticks:
                stick.print_level(i)
            print()
        
    def __initialize_sticks(self):
        sticks = [Stick(i, self.disk_count, []) for i in range(3)]
        sticks[0].disks = [Disk(i+1, self.disk_count - i - 1) for i in range(self.disk_count)]
        return sticks

for move_from, move_to in permutations(HUMANIZED_INDEXES.keys(), 2):
    def _move_to(self, move_from=move_from, move_to=move_to):
        selected_disk = self.sticks[move_from].pop_disk()
        if not selected_disk: return None
        
        not_inserted_disk = self.sticks[move_to].insert_disk(selected_disk)
        if not_inserted_disk:
            self.sticks[move_from].insert_disk(not_inserted_disk)
        self.print_sticks()
        
        
    name = HUMANIZED_INDEXES[move_from] + "_to_" + HUMANIZED_INDEXES[move_to]
    setattr(Game, name, _move_to)

    
        
    