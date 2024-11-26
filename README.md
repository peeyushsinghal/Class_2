# Python Classes and Properties Demo

This project demonstrates various Python OOP concepts including properties, descriptors, class methods, static methods, and dynamic attributes.

## Project Structure

```
├── circle 
├── person.py # Person class with dynamic age property
├── vehicle.py # Vehicle classes with class/static methods
├── dynamic.py # DynamicClass and ValidatedAttribute
├── test_circle.py # Circle tests
├── test_person.py # Person tests
├── test_vehicle.py # Vehicle tests
├── test_dynamic.py # Dynamic class tests
└── classes_tests.py # Combined pytest test suite
```

## Classes Overview

### Circle
- Properties for radius, diameter, and area
- Area caching implementation
- Validation for negative radius

### Person
- Dynamic age calculation based on birth year
- Full name handling with first/last name
- Salary calculation with base salary and bonus
- Property decorators for attribute access

### Vehicle
- Class-level vehicle counting
- Static method for vehicle classification
- ElectricVehicle subclass with method override

### DynamicClass
- Dynamic attribute creation at runtime
- Class-level static value
- ValidatedAttribute descriptor for value validation

## Running Tests

You can run individual test files:
```bash
python -m pytest test_circle.py
python -m pytest test_person.py
python -m pytest test_vehicle.py
python -m pytest test_dynamic.py
```
Or run all tests together:
```bash
python -m pytest -v classes_tests.py
```
## Features Demonstrated
- Property decorators
- Computed properties
- Property validation
- Class methods
- Static methods
- Inheritance
- Descriptors
- Dynamic attributes
- Method overriding
- Type hints
- Unit testing
- Test fixtures
- GitHub Actions workflow