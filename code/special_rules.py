import materials
import fluids


def apply_seawater_rules(material, material_data, temperature):
    avoid = []

    if material_data["corrosion_resistance"] != "high":
        avoid.append("Insufficient corrosion resistance for seawater")
    
    return avoid if avoid else None


def apply_freshwater_rules(material, material_data, temperature):
    # Fresh water does not impose special restrictions
    return None
    

def apply_steam_rules(material, material_data, temperature):
    avoid = []

    if material_data["max_temp"] < 400:
        avoid.append("Insufficient temperature resistance for steam")

    if material_data["type"] != "metal":
        avoid.append("Steam systems require metallic materials")

    return avoid if avoid else None


def apply_fuel_oil_rules(material, material_data, temperature):
    avoid = []

    if material_data["type"] != "metal":
        avoid.append("Fuel systems require metallic materials")
    
    if material in ["Plastic (PE/PVC)", "GRP"]:
        avoid.append("Material not suitable for hydrocarbons")

    return avoid if avoid else None


def apply_lubricating_rules(material, material_data, temperature):
    avoid = []

    if material_data["type"] != "metal":
        avoid.append("Lubricating oil requires metallic materials")
    
    return avoid if avoid else None


def apply_hydraulic_rules(material, material_data, temperature):
    avoid = []

    if material in ["Plastic (PE/PVC)", "GRP"]:
        avoid.append("Material not suitable for hydraulic oil")

    return avoid if avoid else None


def apply_ballast_rules(material, material_data, temperature):
    avoid = []

    if material_data["corrosion_resistance"] == "low":
        avoid.append("Insufficient corrosion resistance for ballast water")

    return avoid if avoid else None


def apply_compressed_air_rules(material, material_data, temperature):
    avoid = []

    if material_data["type"] != "metal":
        avoid.append("Compressed air systems require metallic materials")

    return avoid if avoid else None


def apply_CO2_rules(material, material_data, temperature):
    avoid = []

    if temperature < -20 and material not in ["Carbon steel", "Galvanised steel"]:
        avoid.append("Material becomes brittle below -20ºC except Carbon steel and Galvanised steel")
    
    if material_data["type"] != "metal":
        avoid.append("CO2 systems require metallic materials")

    return avoid if avoid else None


def apply_cryogenic_rules(material, material_data, temperature):
    avoid = []

    if material_data["fragile_low_temp"]:
        avoid.append("Material becomes brittle at cryogenic temperatures")
    
    if material_data["type"] != "metal":
        avoid.append("Cryogenic fluid systems require metallic materials")
    
    if material in ["Plastic (PE/PVC)", "GRP", "Copper"]:
        avoid.append("Material not suitable for cryogenic fluids")
    
    return avoid if avoid else None


def apply_special_rules(fluid, material, material_data, temperature):
    if fluid == "Sea water":
        return apply_seawater_rules(material, material_data, temperature)
    if fluid == "Fresh water":
        return apply_freshwater_rules(material, material_data, temperature)
    if fluid == "Steam":
        return apply_steam_rules(material, material_data, temperature)
    if fluid == "Fuel oil":
        return apply_fuel_oil_rules(material, material_data, temperature)
    if fluid == "Lubricating oil":
        return apply_lubricating_rules(material, material_data, temperature)
    if fluid == "Hydraulic oil":
        return apply_hydraulic_rules(material, material_data, temperature)
    if fluid == "Ballast water":
        return apply_ballast_rules(material, material_data, temperature)
    if fluid == "Compressed air":
        return apply_compressed_air_rules(material, material_data, temperature)
    if fluid == "CO2":
        return apply_CO2_rules(material, material_data, temperature)
    if fluid == "Cryogenic fluid":
        return apply_cryogenic_rules(material, material_data, temperature)
    
    return None
