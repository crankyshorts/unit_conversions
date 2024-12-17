class UnitConverter:
    def __init__(self):
        self.conversions = {
            'length': {
                'meters': 1.0,
                'feet': 3.28084,
                'inches': 39.3701,
                'centimeters': 100,
                'kilometers': 0.001,
                'miles': 0.000621371
            },
            'weight': {
                'kilograms': 1.0,
                'pounds': 2.20462,
                'grams': 1000,
                'ounces': 35.274
            },
            'temperature': {
                'celsius': 'base',
                'fahrenheit': 'special',
                'kelvin': 'special'
            }
        }

    def convert_temperature(self, from_unit, to_unit, value):
        # Convert to Celsius first
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        else:
            celsius = value

        # Convert from Celsius to target unit
        if to_unit == 'fahrenheit':
            return (celsius * 9/5) + 32
        elif to_unit == 'kelvin':
            return celsius + 273.15
        return celsius

    def convert(self, category, from_unit, to_unit, value):
        if category == 'temperature':
            return self.convert_temperature(from_unit, to_unit, value)
        
        if category not in self.conversions:
            raise ValueError(f"Invalid category: {category}")
        
        conversions = self.conversions[category]
        if from_unit not in conversions or to_unit not in conversions:
            raise ValueError("Invalid unit type")
        
        # Convert to base unit first
        base_value = value / conversions[from_unit]
        # Convert from base unit to target unit
        return base_value * conversions[to_unit]

converter = UnitConverter()

def get_conversion_types():
    return {
        'length': ['meters', 'feet', 'inches', 'centimeters', 'kilometers', 'miles'],
        'weight': ['kilograms', 'pounds', 'grams', 'ounces'],
        'temperature': ['celsius', 'fahrenheit', 'kelvin']
    }

def convert_units(category, from_unit, to_unit, value):
    return round(converter.convert(category, from_unit, to_unit, value), 6)
