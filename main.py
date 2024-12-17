from flask import Flask, render_template, request, jsonify
import logging
from utils.conversions import perform_conversion

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'dev_key_123'  # For development purposes

CONVERSION_TYPES = {
    'length': ['Meters', 'Feet', 'Inches', 'Kilometers', 'Miles'],
    'weight': ['Kilograms', 'Pounds', 'Ounces', 'Grams'],
    'temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
    'volume': ['Liters', 'Gallons', 'Cubic Meters', 'Milliliters'],
    'area': ['Square Meters', 'Square Feet', 'Square Kilometers', 'Acres'],
    'time': ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years'],
    'digital': ['Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes'],
    'speed': ['Meters per Second', 'Kilometers per Hour', 'Miles per Hour', 'Knots'],
    'energy': ['Joules', 'Calories', 'Kilocalories', 'Watt Hours', 'Kilowatt Hours']
}

@app.route('/')
def index():
    return render_template('index.html', conversion_types=CONVERSION_TYPES)

@app.route('/convert', methods=['POST'])
def convert():
    try:
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        
        result = perform_conversion(value, from_unit, to_unit)
        return jsonify({'success': True, 'result': result})
    except ValueError as e:
        return jsonify({'success': False, 'error': 'Invalid number input'})
    except Exception as e:
        logging.error(f"Conversion error: {str(e)}")
        return jsonify({'success': False, 'error': 'Conversion error occurred'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
