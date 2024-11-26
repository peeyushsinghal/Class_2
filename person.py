from datetime import datetime

class Person:
    def __init__(self, first_name: str = '', last_name: str = '', birth_year: int = 0):
        self._birth_year = birth_year
        self._first_name = first_name
        self._last_name = last_name
        self._base_salary = 50000
        self._bonus = 10.0
    
    @property
    def current_year(self) -> int:
        """Returns the current year"""
        return datetime.now().year
    
    @property
    def age(self) -> int:
        """Calculate age dynamically based on birth year and current year"""
        current_year = datetime.now().year
        if not isinstance(current_year, int) or not isinstance(self._birth_year, int):
            raise TypeError("Both current year and birth year must be integers")
        return max(0, current_year - self._birth_year)
    @property
    def first_name(self) -> str:
        """Getter for first name"""
        return self._first_name
    
    @property
    def last_name(self) -> str:
        """Getter for last name"""
        return self._last_name
    
    @property
    def birth_year(self) -> int:
        """Getter for birth year"""
        return self._birth_year
    
    @birth_year.setter 
    def birth_year(self, year: int) -> None:
        """Setter for birth year with type validation"""
        try:
            year_int = int(year)
        except (ValueError, TypeError):
            raise TypeError("Birth year must be convertible to an integer")
        self._birth_year = year_int

    def set_birth_year(self, year: int) -> None:
        """Sets the birth year using the setter for birth_year"""
        self.birth_year = year  # This will use the setter method
    
    @property
    def full_name(self) -> str:
        """Combines first and last name"""
        return f"{self._first_name} {self._last_name}".strip()
    
    @full_name.setter 
    def full_name(self, name: str) -> None:
        """Splits full name into first and last name"""
        parts = name.split()
        self._first_name = parts[0] if parts else ''
        self._last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
    
    @property
    def salary(self) -> float:
        """Calculates salary based on base salary and bonus"""
        return round(self._base_salary * (1 + self._bonus / 100), 2)
    
    @property
    def base_salary(self) -> float:
        """Getter for base salary"""
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, value: float) -> None:
        """Setter for base salary"""
        self._base_salary = value
    
    @property
    def bonus(self) -> float:
        """Getter for bonus percentage"""
        return self._bonus
    
    @bonus.setter
    def bonus(self, percentage: float) -> None:
        """Setter for bonus percentage with validation"""
        if not 0 <= percentage <= 100:
            raise ValueError("Bonus percentage must be between 0 and 100")
        self._bonus = percentage

    def __str__(self) -> str:
        """String representation of the Person"""
        return f"{self.full_name}, Age: {self.age}, Salary: {self.salary:.2f}"