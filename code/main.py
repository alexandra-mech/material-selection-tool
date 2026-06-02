import materials
import fluids
from rules import apply_general_rules
from special_rules import apply_special_rules


def evaluate_materials(fluid_name, temperature, pressure):
    results = {
        "valid": [],
        "rejected": {}
    }

    # Obtain fluid data
    fluid_data = fluids.fluids.get(fluid_name)
    if not fluid_data:
        print(f"Fluid '{fluid_name}' not found.")
        return results
    
    # Temperature out of the fluid range
    if temperature < fluid_data["min_temp"] or temperature > fluid_data["max_temp"]:
        print(f"ERROR: Temperature {temperature}ºC is outside the allowed range for {fluid_name} "
              f"({fluid_data['min_temp']}ºC to {fluid_data['max_temp']}ºC).")
        return results

    # Negative pressure or excessively high
    if pressure <= 0:
        print("ERROR: Pressure must be greater than 0 bar.")
        return results

    if pressure > 200:  # Safety system
        print("ERROR: Pressure exceeds safe system limits (>200 bar).")
        return results

    # Evaluate each material
    for material, material_data in materials.materials.items():

        avoid = []

        # 1. General rules
        general_avoid = apply_general_rules(
            material,
            material_data,
            fluid_name,
            fluid_data,
            temperature,
            pressure
        )
        if general_avoid:
            avoid.extend(general_avoid)

        # 2. Specific rules
        special_avoid = apply_special_rules(
            fluid_name,
            material,
            material_data,
            temperature
        )
        if special_avoid:
            avoid.extend(special_avoid)

        # 3. Classification
        if avoid:
            results["rejected"][material] = avoid
        else:
            results["valid"].append(material)

    return results


def main():
    print("=== PIPE MATERIAL SELECTOR ===")

    fluid_name = input("Enter fluid name: ")
    temperature = float(input("Enter operating temperature (ºC): ").strip().replace("\\", ""))
    unit = input("Pressure unit [bar/kPa]: ").lower()
    pressure = float(input("Enter operating pressure: "))

    # Convert pressure to bar
    if unit == "kpa":
        pressure = pressure / 100

    results = evaluate_materials(fluid_name, temperature, pressure)

    print("\n=== VALID MATERIALS ===")
    for m in results["valid"]:
        print(f" - {m}")

    print("\n=== REJECTED MATERIALS ===")
    for m, avoid in results["rejected"].items():
        print(f"\n{m}:")
        for r in avoid:
            print(f"   - {r}")


if __name__ == "__main__":
    main()
