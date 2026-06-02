# FLUID PROPERTIES
# Temperature in ºC
# Pressure in bar


fluids = {
    "Sea water": {
        "name": "Sea water",
        "min_temp": 0,
        "max_temp": 35,
        "chemical_nature": "water",
        "corrosivity": "high",
        "systems": ["Cooling", "Ballast"]
    },
    "Fresh water": {
        "name": "Fresh water",
        "min_temp": 0,
        "max_temp": 90,
        "chemical_nature": "water",
        "corrosivity": "low",
        "systems": ["Cooling"]
    },
    "Steam": {
        "name": "Steam",
        "min_temp": 170,
        "max_temp": 450,
        "chemical_nature": "gas",
        "corrosivity": "low",
        "systems": ["Steam"]
    },
    "Fuel oil": {
        "name": "Fuel oil",
        "min_temp": 40,
        "max_temp": 150,
        "chemical_nature": "hydrocarbon",
        "corrosivity": "low",
        "systems": ["Fuel"]
    },
    "Lubricating oil": {
        "name": "Lubricating oil",
        "min_temp": 40,
        "max_temp": 120,
        "chemical_nature": "lubricant",
        "corrosivity": "low",
        "systems": ["lubrication"]
    },
    "Hydraulic oil": {
        "name": "Hydraulic oil",
        "min_temp": 20,
        "max_temp": 80,
        "chemical_nature": "hydrocarbon",
        "corrosivity": "low",
        "systems": ["Hydraulic"]
    },
    "Ballast water": {
        "name":"Ballast water",
        "min_temp": 0,
        "max_temp": 35,
        "chemical_nature": "water",
        "corrosivity": "high",
        "systems": ["Ballast"]
    },
    "Compressed air": {
        "name": "Compressed air",
        "min_temp": 0,
        "max_temp": 60,
        "chamical_nature": "gas",
        "corrosivity": "low",
        "systems": ["Air"]
    },
    "CO2": {
        "name": "CO2",
        "min_temp": -50,
        "max_temp": 30,
        "chemical_nature": "gas",
        "corrosivity": "low",
        "systems": ["Inert gas", "Firefighting"]
    },
    "Cryogenic fluid": {
        "name": "Cryogenic fluid",
        "min_temp": -196,
        "max_temp": -100,
        "chemical_nature": "cryogenic",
        "corrosivity": "low",
        "systems": "cryogenic"
    }
}