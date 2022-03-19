from disk import Disk
from stick import Stick

disks = [Disk(i+1) for i in range(3)]
stick = Stick(0, disks)
stick.print_level(0)
stick.print_level(1)
stick.print_level(2)