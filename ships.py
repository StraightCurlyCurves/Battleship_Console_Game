class Ship:
    def __init__(self, length = 0) -> None:
        self.length = length
        self.start_coordinates = [0, 0]
        self.position = []
        self.alignment = 'vertical'

        self.shots_per_minute = 0
        self.set_shots_per_minute()

        self.destroyed = False

    def set_alignment(self, alignment: str):
        if alignment == 'vertical':
            self.alignment = 'vertical'            
        elif alignment == 'horizontal':
            self.alignment = 'horizontal'            
        else:
            print("Incorrect input parameter!")

    def set_start_coordinates(self, coordinates: tuple):
        if len(coordinates) == 2:
            self.start_coordinates = coordinates
        else:
            print("Please provide 2 dimesnional coordinates!")

    def place_ship(self):
        self.position.clear()
        self.position.append([self.start_coordinates])
        if self.alignment == 'vertical':
            for i in self.length:
                square_position = self.start_coordinates
                square_position[1] += i + 1
                self.position.append([square_position])
        if self.alignment == 'horizontal':
            for i in self.length:
                square_position = self.start_coordinates
                square_position[0] += i + 1
                self.position.append([square_position])

    def set_shots_per_minute(self):
        self.shots_per_minute = 2 * self.length

    def got_hit(self):
        self.length -= 1
        if self.length == 0:
            self.destroyed = True
        self.set_shots_per_minute()

class Carrier(Ship):
    def __init__(self) -> None:
        super().__init__(length = 5)

class Battleship(Ship):
    def __init__(self) -> None:
        super().__init__(length = 4)

class Cruiser(Ship):
    def __init__(self) -> None:
        super().__init__(length = 3)

class Destroyer(Ship):
    def __init__(self) -> None:
        super().__init__(length = 2)

class Submarine(Ship):
    def __init__(self) -> None:
        super().__init__(length = 1)
