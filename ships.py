class Ship:
    def __init__(self, length = 0) -> None:
        self.length = length
        self.start_coordinates = [100, 100]
        self.position = []
        self.position_destroyed = []
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
        for i in range(self.length):
            square_position = self.start_coordinates.copy()
            if self.alignment == 'vertical':
                square_position[1] += i
            if self.alignment == 'horizontal':
                square_position[0] += i
            self.position.append(square_position.copy())

    def set_shots_per_minute(self):
        self.shots_per_minute = 2 * self.length

    def got_hit(self):
        self.length -= 1
        if self.length == 0:
            self.destroyed = True
        self.set_shots_per_minute()

    def check_hit(self, coordinates):
        if coordinates in self.position_destroyed:
            return False
        if coordinates in self.position:
            self.position_destroyed.append(coordinates)
            return True
        else:
            return False

class Carrier(Ship):
    def __init__(self) -> None:
        super().__init__(length = 5)
        self.name = 'carrier'

class Battleship(Ship):
    def __init__(self) -> None:
        super().__init__(length = 4)
        self.name = 'battleship'

class Cruiser(Ship):
    def __init__(self) -> None:
        super().__init__(length = 3)
        self.name = 'cruiser'

class Destroyer(Ship):
    def __init__(self) -> None:
        super().__init__(length = 2)
        self.name = 'destroyer'

class Submarine(Ship):
    def __init__(self) -> None:
        super().__init__(length = 1)
        self.name = 'submarine'

class Fleet:
    def __init__(self) -> None:
        self.ships = {}
        self.ships['carrier_1'] = Carrier()
        self.ships['battleship_1'] = Battleship()
        self.ships['cruiser_1'] = Cruiser()
        self.ships['destroyer_1'] = Destroyer()
        self.ships['destroyer_2'] = Destroyer()
        self.ships['submarine_1'] = Submarine()
        self.ships['submarine_2'] = Submarine()

        self.shots_per_minute = self.get_shots_per_minute()

    def get_shots_per_minute(self):
        spm_sum = 0
        for ship in self.ships.values():
            spm_sum += ship.shots_per_minute
        return spm_sum

    def place_ships(self):
        for ship in self.ships.values():
            ship.place_ship()

    def get_positions(self):
        positions = []
        for ship in self.ships.values():
            positions.append(ship.position)
        return positions

    def hit_coordinates(self, coordinates):
        '''
        checks if the shot hit a ship and if it's destroyed
        returns: hit / no hit (True/False), destroyed / not destroyed (True/False)
        '''
        for ship in self.ships.values():
            if ship.check_hit(coordinates):
                ship.got_hit()
                self.shots_per_minute = self.get_shots_per_minute()
                if ship.destroyed:
                    return True, True
                return True, False
        return False, False