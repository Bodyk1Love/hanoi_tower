class Disk:
    def __init__(self, size, place) -> None:
        self.size = size
        self.place = place
    
    def __str__(self) -> str:
        return "x" * self.size