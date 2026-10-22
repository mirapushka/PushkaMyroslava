def convert_to_meters(value: float, unit: str = "cm") -> float | None:
    """Конвертує значення в метри."""
    if value < 0:
        return None
    
    if unit == "cm":
        return value / 100
    elif unit == "mm":
        return value / 1000
    elif unit == "inch":
        return value * 0.0254
    else:
        return None

def calculate_bmi(weight_kg: float, height_m: float) -> tuple[float, str] | None:
    """Розраховує індекс маси тіла (BMI)."""
    if weight_kg <= 0 or height_m <= 0:
        return None
    
    bmi = round(weight_kg / (height_m ** 2), 1)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal"
    elif 25.0 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
        
    return (bmi, category)

h = convert_to_meters(175, "cm")
print(h)

bmi_result = calculate_bmi(70, h)
print(bmi_result)