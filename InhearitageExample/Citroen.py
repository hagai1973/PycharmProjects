from Car import Car

class Citroen(Car):
    def __init__(self):
        super().__init__()

    def manufacture_country(self):
        print("I am from France")

    def driving(self):
        super().driving()
        print("driveing very comfort")
