class Disk:
    def __init__(self, size) -> None:
        self.size = size
    
    def __str__(self) -> str:
        return "x" * self.size