import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.circle = Circle(5.0)
    
    def test_radius_getter(self):
        """Test if radius getter returns correct value"""
        self.assertEqual(self.circle.radius, 5.0)
    
    def test_radius_setter(self):
        """Test if radius setter updates value correctly"""
        self.circle.radius = 7.0
        self.assertEqual(self.circle.radius, 7.0)
    
    def test_negative_radius(self):
        """Test if setting negative radius raises ValueError"""
        with self.assertRaises(ValueError):
            self.circle.radius = -1.0
    
    def test_diameter_calculation(self):
        """Test if diameter is calculated correctly"""
        self.assertEqual(self.circle.diameter, 10.0)

    def test_area_caching(self):
        """Test if area is cached after first calculation"""
        # First access to calculate and cache the area
        initial_area = self.circle.area
        
        # Capture print output to verify calculation message
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Second access should use cached value without calculation
        cached_area = self.circle.area
        
        # Restore stdout
        sys.stdout = original_stdout
        
        # Verify areas match
        self.assertEqual(initial_area, cached_area)
        # Verify no "Calculating" message on second access
        self.assertEqual(captured_output.getvalue(), '')

    def test_area_calculation(self):
        """Test if area is calculated correctly"""
        expected_area = math.pi * 25  # pi * r^2
        self.assertEqual(self.circle.area, expected_area)
    
    def test_properties_update_with_radius(self):
        """Test if diameter and area update when radius changes"""
        self.circle.radius = 3.0
        self.assertEqual(self.circle.diameter, 6.0)
        self.assertEqual(self.circle.area, math.pi * 9)
    

if __name__ == '__main__':
    unittest.main() 