# 31 ตรวจสอบปีอธิกสุรทิน (Leap Year)

#1

import calendar

y = int(input())
if calendar.isleap(y):
    print("Leap Year")
else : 
    print("Not Leap Year")

#2

y = int(input())

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 :
    print("Leap Year")
else :
    print("Not Leap Year")