import json
import random
from datetime import date, timedelta

def get_last_digit_sum(num_str):
    total = sum(int(digit) for digit in num_str)
    return total % 10

def generate_pairs():
    first = str(random.randint(100, 999))
    third = str(random.randint(100, 999))
    first_sum = get_last_digit_sum(first)
    third_sum = get_last_digit_sum(third)
    middle = f"{first_sum}{third_sum}"
    return {"first": first, "middle": middle, "third": third}

start_date = date(2026, 1, 1)
end_date = date(2027, 12, 31)

data = {}

current = start_date
while current <= end_date:
    date_str = current.strftime("%Y-%m-%d")
    data[date_str] = generate_pairs()
    current += timedelta(days=1)

with open("d:\\dpbs\\data.js", "w") as f:
    f.write("const staticData = " + json.dumps(data, indent=2) + ";\n")

print("Data successfully generated and saved to data.js")
