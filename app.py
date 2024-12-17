import logging
from flask import Flask, render_template, jsonify
from conversions import get_conversion_types, convert_units

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = "unit-converter-secret-key"

@app.route('/')
def index():
    conversion_types = get_conversion_types()
    return render_template('index.html', conversion_types=conversion_types)

@app.route('/convert/<category>/<from_unit>/<to_unit>/<value>')
def convert(category, from_unit, to_unit, value):
    try:
        result = convert_units(category, from_unit, to_unit, float(value))
        return jsonify({'success': True, 'result': result})
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)})
