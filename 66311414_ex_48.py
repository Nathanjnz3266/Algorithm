number = int(input())

year = number // 365
number = number % 365 #ลบจำนวนปี
month = number // 30
number = number % 30 #ลบจำนวนวัน
day = number
print(f"{year} years, {month} months, {day} days")