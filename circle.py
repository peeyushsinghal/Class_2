import math

class Circle:
    def __init__(self, radius: float):
        """Initialize circle with given radius"""
        self._radius = radius
        self._area = None
    
    @property
    def radius(self) -> float:
        """Getter for radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        """Setter for radius with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
        self._area = None
    
    @property
    def diameter(self) -> float:
        """Computed property for diameter"""
        return 2 * self._radius
    
    @property
    def area(self) -> float:
        """Computed property for area"""
        if self._area is None:
            # value not cached - calculate it
            print('Calculating area...')
            self._area = math.pi * (self._radius ** 2)
        return self._area