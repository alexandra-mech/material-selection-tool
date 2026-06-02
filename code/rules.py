# GENERAL RULES

def apply_general_rules(material, material_data, fluid_name, fluid_data, temperature, pressure):
    avoid = []

    # Maximum temperature rule
    if temperature > material_data["max_temp"]:
        avoid.append(f"Temperature exceeds material limit ({material_data['max_temp']}ºC)")

    # Pressure
    # print(material, pressure, material_data["max_pressure"])
    if pressure > material_data["max_pressure"]:
        avoid.append(f"Pressure exceeds material limit ({material_data['max_pressure']} bar)")

    # Corrosion rule
    if fluid_data["corrosivity"] == "high" and material_data["corrosion_resistance"] != "high":
        avoid.append("Material not resistant to high corrosivity")

    # Chemical compatibility
    if "all" not in material_data["compatible_with"] and fluid_name not in material_data["compatible_with"]:
        avoid.append("Chemical incompatibility")

    return avoid
