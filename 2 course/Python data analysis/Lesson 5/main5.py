import re
def normalize_ua_phone(raw_phone: str) -> str | None:
    digits = re.sub(r'\D', '', raw_phone)
    if len(digits) == 10:
        return "+38" + digits
    elif len(digits) == 12 and digits.startswith("380"):
        return "+" + digits
    else:
        return None
if __name__ == "__main__":
    test_cases = [
        "+38(050)123-45-67",
        "050 123 45 67",
        "380501234567",
        "050-123-45-67",
        "тел: 0501234567",
        "невідомо"
    ]
    
    for phone in test_cases:
        print(f"{phone} -> {normalize_ua_phone(phone)}")