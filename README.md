

Main Structure:

  main.py is the entry point, setting up a Flask server with routes for the homepage ('/') and conversion endpoint ('/convert')
  
  The app uses templates (in templates/) for the UI
  
  Static files (JS/CSS) are in the static/ directory
  
  Key Components:

Frontend: 

  Bootstrap-based UI with a form for selecting conversion types and units
  
  Backend: Uses a UnitConverter class in conversions.py to handle calculations
  
  JavaScript: converter.js manages form submissions and updates the UI dynamically
  
Flow:

  User selects a conversion type (length, weight, etc.)
  
  Enters a value and selects from/to units
  
  Frontend sends a POST request to /convert
  
  Backend performs conversion using perform_conversion()
  
  Result is returned as JSON and displayed on the page

Architecture:

  UnitConverter class maintains conversion ratios
  
  Special handling for temperature conversions
  
  Error handling for invalid inputs
  
  Responsive design with Bootstrap
