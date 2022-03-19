from disk import Disk
from stick import Stick

class Game:
    def __init__(self, disk_count) -> None:
        self.disk_count = disk_count
        self.sticks = self.__initialize_sticks()
        
    def print_sticks(self):
        for i in range(self.disk_count):
            for stick in self.sticks:
                stick.print_level(i)
            print()
        
    def __initialize_sticks(self):
        sticks = [Stick(i, []) for i in range(3)]
        sticks[0].disks = [Disk(i+1) for i in range(self.disk_count)]
        return sticks
    
    
        
    