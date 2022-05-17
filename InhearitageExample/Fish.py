from Animal import Animal


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("in water")