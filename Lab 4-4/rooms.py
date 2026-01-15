"""
Phuvisa Chotphan
683040157-7
P1
"""

from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    @abstractmethod
    def get_purpose(self):
        """Returns a string describing purposes of the room"""
        pass

    @abstractmethod
    def get_recommended_lighting(self):
        """Returns recommended lighting in lumens per square foot"""
        pass

    def calculate_area(self):
        return self.length * self.width
    
    def describe_room(self):
        area = self.calculate_area()
        return f"A {self.__class__.__name__} of {area} sq ft used for {self.get_purpose()}"

class Bedroom(Room):
    def __init__(self, length, width, bed_size):
        super().__init__(length, width)
        self.bed_size = bed_size

    def get_purpose(self):
        """Returns recommended lighting in lumens per square foot"""
        return f"Sleepy...Zzz U.U (Bed Size: {self.bed_size} ft)"
    
    def get_recommended_lighting(self):
        """Returns recommended lighting in lumens per square foot"""
        return 15
    
class Kitchen(Room):
    def __init__(self, length, width, has_island = True):
        super().__init__(length, width)
        self.has_island = has_island

    def get_purpose(self):
        if self.has_island:
            return "Cooking food witn an island"
        return "Cooking food"

    def get_recommended_lighting(self):
        """Returns recommended lighting in lumens per square foot"""
        return 35

    def calculate_counter_space(self):
        """Calculates Kitchen Area
        
        Parameters:
        ------
        nothing
        
        Reises
        ------
        tuple(float, float)
                island_counter_area is a area of the island counter area in square feet
                wall_counter is a area of wall counter in feet
        
        Reises
        ------
        nothing
        
        Example
        ------
        >>> adj.calculate_counter_space()
        """
        

        room_area = self.calculate_area()

        if self.has_island:
            island_counter = room_area / 5
            wall_counter = room_area / 4
        else:
            island_counter = 0
            wall_counter = room_area / 2
        return island_counter, wall_counter