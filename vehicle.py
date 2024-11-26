class Vehicle:
    # Class variable to track total vehicles
    vehicle_count = 0
    
    def __init__(self, make: str, model: str, year: int):
        """Initialize vehicle with make, model name, and year"""
        self.make = make
        self.model = model
        self.year = year
        Vehicle.vehicle_count += 1
    
    @classmethod
    def get_vehicle_count(cls) -> int:
        """Class method to return total number of vehicles"""
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(vehicle_type: str) -> str:
        """Static method to classify vehicle types"""
        valid_types = {"car", "truck", "motorcycle"}
        if vehicle_type.lower() not in valid_types:
            raise ValueError(f"Invalid vehicle type. Must be one of: {valid_types}")
        return f"This is a {vehicle_type.lower()}"
    
    def __del__(self):
        """Destructor to decrease vehicle count when instance is deleted"""
        Vehicle.vehicle_count -= 1


class ElectricVehicle(Vehicle):
    def __init__(self, make: str, model: str, year: int):
        """Initialize electric vehicle with make, model name, and year """
        super().__init__(make, model, year)  # Call the parent class's __init__
    
    @staticmethod
    def classify_vehicle(vehicle_type: str) -> str:
        """Override static method to specify electric vehicles"""
        valid_types = {"car", "truck", "motorcycle"}
        if vehicle_type.lower() not in valid_types:
            raise ValueError(f"Invalid vehicle type. Must be one of: {valid_types}")
        return f"This is an electric {vehicle_type.lower()}" 
