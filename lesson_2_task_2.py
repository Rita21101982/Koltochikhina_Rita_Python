# Високосный год

def is_year_leap(year_num):
    return True if year_num % 4 == 0 else False

year_num = int(input("Введите номер года: "))
result = is_year_leap(year_num)

print(f"год {year_num}: {result}")
