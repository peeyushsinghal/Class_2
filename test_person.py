import unittest
from datetime import datetime
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.current_year = datetime.now().year
        self.person = Person("", "", 1990)
    
    def test_age_calculation(self):
        """Test if age is calculated correctly"""
        expected_age = self.current_year - 1990
        self.assertEqual(self.person.age, expected_age)
    
    def test_birth_year_getter(self):
        """Test if birth_year getter returns correct value"""
        self.assertEqual(self.person.birth_year, 1990)
    
    def test_birth_year_setter(self):
        """Test if birth_year setter updates value correctly"""
        self.person.birth_year = 1995
        self.assertEqual(self.person.birth_year, 1995)
        
    def test_age_updates_with_birth_year(self):
        """Test if age updates when birth_year is changed"""
        self.person.birth_year = 1995
        expected_age = self.current_year - 1995
        self.assertEqual(self.person.age, expected_age)
    
    def test_negative_age(self):
        """Test handling of future birth years"""
        future_year = self.current_year + 10
        self.person.birth_year = future_year
        self.assertEqual(self.person.age, 0)

    def test_empty_name_initially(self):
        """Test that name is empty when person is created"""
        self.assertEqual(self.person.full_name, '')
    
    def test_set_full_name_two_parts(self):
        """Test setting full name with first and last name"""
        self.person.full_name = "John Smith"
        self.assertEqual(self.person.full_name, "John Smith")
    
    def test_set_full_name_multiple_parts(self):
        """Test setting full name with multiple parts"""
        self.person.full_name = "John William Smith"
        self.assertEqual(self.person.full_name, "John William Smith")
    
    def test_set_full_name_single_part(self):
        """Test setting full name with only first name"""
        self.person.full_name = "John"
        self.assertEqual(self.person.full_name, "John")
    
    def test_set_empty_name(self):
        """Test setting empty name"""
        self.person.full_name = ""
        self.assertEqual(self.person.full_name, "")

    
    def test_base_salary_getter(self):
        """Test if base_salary getter returns correct value"""
        self.person.base_salary = 50000.0
        self.assertEqual(self.person.base_salary, 50000.0)
    
    def test_base_salary_setter(self):
        """Test if base_salary setter updates value correctly"""
        self.person.base_salary = 60000.0
        self.assertEqual(self.person.base_salary, 60000.0)
    
    def test_bonus_getter(self):
        """Test if bonus getter returns correct value"""
        self.person.bonus = 10.0
        self.assertEqual(self.person.bonus, 10.0)
    
    def test_bonus_setter_valid(self):
        """Test if bonus setter accepts valid percentage"""
        self.person.bonus = 15.0
        self.assertEqual(self.person.bonus, 15.0)
    
    def test_bonus_setter_invalid(self):
        """Test if bonus setter rejects invalid percentage"""
        with self.assertRaises(ValueError):
            self.person.bonus = 150.0
        with self.assertRaises(ValueError):
            self.person.bonus = -10.0
    
    def test_salary_calculation(self):
        """Test if salary is calculated correctly with base salary and bonus"""
        self.person.base_salary = 50000.0
        self.person.bonus = 20.0
        expected_salary = 50000.0 * 1.20  # 20% bonus
        self.assertEqual(self.person.salary, expected_salary)
    
    def test_current_year(self):
        """Test that current_year property returns the current year"""
        from datetime import datetime
        expected_year = datetime.now().year
        self.assertEqual(self.person.current_year, expected_year)


if __name__ == '__main__':
    unittest.main()  