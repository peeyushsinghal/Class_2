class ValidatedAttribute:
    """A descriptor that ensures values are positive integers"""
    
    def __init__(self):
        self._value = 0
    
    @property
    def value(self) -> int:
        """Get the validated value"""
        return self._value
    
    @value.setter
    def value(self, val: int) -> None:
        """Set value with validation"""
        if not isinstance(val, (int, float)):
            raise TypeError("Value must be a number")
        if val <= 0:
            raise ValueError("Value must be positive")
        self._value = int(val)


class DynamicClass:
    # Class-level variable
    static_value = 100
    
    def __init__(self, **kwargs):
        """Initialize with optional keyword arguments"""
        self._attributes = {}
        # Initialize with any provided kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
            self._attributes[key] = value  # Add this line to store attributes

    
    def dynamic_attr(self, name: str, value: any) -> None:
        """Dynamically add an attribute at runtime"""
        if not isinstance(name, str):
            raise TypeError("Attribute name must be a string")
        
        setattr(self, name, value)
        self._attributes[name] = value
    
    def get_attributes(self) -> dict:
        """Return dictionary of dynamic attributes"""
        return self._attributes.copy()
    
    @classmethod
    def get_static_value(cls) -> int:
        """Get the class-level static value"""
        return cls.static_value
    
    @classmethod
    def set_static_value(cls, value: int) -> None:
        """Set the class-level static value"""
        cls.static_value = value

