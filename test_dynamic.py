import pytest
from dynamic import DynamicClass, ValidatedAttribute

class TestDynamicClass:
    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments"""
        obj = DynamicClass(name="John", age=30)
        assert obj.name == "John"
        assert obj.age == 30
        assert obj.get_attributes() == {"name": "John", "age": 30}
    
    def test_dynamic_attr_addition(self):
        """Test adding attributes dynamically"""
        obj = DynamicClass()
        obj.dynamic_attr("name", "Dynamic Object")
        assert obj.name == "Dynamic Object"
        assert "name" in obj.get_attributes()
    
    def test_invalid_attr_name(self):
        """Test adding attribute with invalid name"""
        obj = DynamicClass()
        with pytest.raises(TypeError):
            obj.dynamic_attr(123, "value")
    
    def test_static_value(self):
        """Test class-level static value"""
        assert DynamicClass.get_static_value() == 100
        DynamicClass.set_static_value(200)
        assert DynamicClass.get_static_value() == 200
        # Reset static value for other tests
        DynamicClass.set_static_value(100)


class TestValidatedAttribute:
    def test_initial_value(self):
        """Test initial value is zero"""
        attr = ValidatedAttribute()
        assert attr.value == 0
    
    def test_valid_value(self):
        """Test setting valid values"""
        attr = ValidatedAttribute()
        attr.value = 100
        assert attr.value == 100
        attr.value = 42.5  # Should convert to int
        assert attr.value == 42
    
    def test_negative_value(self):
        """Test setting negative value raises error"""
        attr = ValidatedAttribute()
        with pytest.raises(ValueError):
            attr.value = -10
    
    def test_zero_value(self):
        """Test setting zero raises error"""
        attr = ValidatedAttribute()
        with pytest.raises(ValueError):
            attr.value = 0
    
    def test_invalid_type(self):
        """Test setting non-numeric value raises error"""
        attr = ValidatedAttribute()
        with pytest.raises(TypeError):
            attr.value = "42"
        with pytest.raises(TypeError):
            attr.value = None


if __name__ == '__main__':
    pytest.main([__file__]) 