from utils.binary_tuple import multiply_binary_tuple
from utils.physics import Acceleration, Speed, Position, decompose_acceleration, distance, earth_size, get_proportion
from utils.screen import center_position

class Moveable:
    earth_weight = 5.972 * 10**24 * get_proportion()
    gravitational_constant = 6.674 * 10**-11 * get_proportion()

    def __init__(self, position: Position, speed: Speed,
                 acceleration: Acceleration, weight: float):
        self.__position = position
        self.__speed = multiply_binary_tuple(speed, self.proportion)
        self.__acceleration = multiply_binary_tuple(acceleration, self.proportion)
        self.__weight = weight

    @property
    def position(self):
        return self.__position
        
    @property
    def proportion(self):
        return get_proportion()
        
    @property
    def weight(self):
        return self.__weight

    @property
    def speed(self):
        return self.__speed

    @property
    def acceleration(self):
        return self.__acceleration

    @property
    def earth_distance(self):
        return distance(self.position, center_position)

    @property
    def colidded_to_earth(self):
        return self.radius + earth_size/2 >= self.earth_distance

    def update_acceleration(self):
        new_acceleration = self.gravitational_constant * self.earth_weight / self.earth_distance**2
        self.__acceleration = decompose_acceleration(new_acceleration, self.position, center_position)

    def update_speed(self):
        self.update_acceleration()
        speed_x, speed_y = self.speed
        acceleration_x, acceleration_y = self.acceleration
        self.__speed = tuple([0, 0]) if self.colidded_to_earth else tuple([speed_x + acceleration_x, speed_y + acceleration_y])

    ## Update movable position
    def update_position(self):
        self.update_speed()
        x, y = self.position
        speed_x, speed_y = self.speed
        self.__position = [x + speed_x, y + speed_y]