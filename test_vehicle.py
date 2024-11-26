import unittest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        """Reset vehicle count before each test"""
        Vehicle.vehicle_count = 0
    
    def test_vehicle_count_increment(self):
        """Test if vehicle count increases when creating new vehicles"""
        v1 = Vehicle("Model1")
        self.assertEqual(Vehicle.get_vehicle_count(), 1)
        v2 = Vehicle("Model2")
        self.assertEqual(Vehicle.get_vehicle_count(), 2)
    
    def test_vehicle_count_decrement(self):
        """Test if vehicle count decreases when deleting vehicles"""
        v1 = Vehicle("Model1")
        v2 = Vehicle("Model2")
        del v1
        self.assertEqual(Vehicle.get_vehicle_count(), 1)
    
    def test_classify_vehicle_valid(self):
        """Test vehicle classification with valid types"""
        self.assertEqual(Vehicle.classify_vehicle("car"), "This is a car")
        self.assertEqual(Vehicle.classify_vehicle("truck"), "This is a truck")
        self.assertEqual(Vehicle.classify_vehicle("motorcycle"), "This is a motorcycle")
    
    def test_classify_vehicle_invalid(self):
        """Test vehicle classification with invalid type"""
        with self.assertRaises(ValueError):
            Vehicle.classify_vehicle("boat")
    
    def test_electric_vehicle_classification(self):
        """Test electric vehicle classification"""
        self.assertEqual(ElectricVehicle.classify_vehicle("car"), 
                        "This is an electric car")
        self.assertEqual(ElectricVehicle.classify_vehicle("truck"), 
                        "This is an electric truck")
    
    def test_electric_vehicle_count(self):
        """Test if electric vehicles are counted in total vehicle count"""
        v1 = Vehicle("Regular Car")
        ev1 = ElectricVehicle("Tesla")
        self.assertEqual(Vehicle.get_vehicle_count(), 2)
        self.assertEqual(ElectricVehicle.get_vehicle_count(), 2)

if __name__ == '__main__':
    unittest.main() 