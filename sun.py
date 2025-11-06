months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
month: None
month = input("Enter your birth month: ").lower()
while month not in months:
    month = input("Enter your birth month: ").lower()
day = int(input("Enter your birth day: "))
if day < 0 or day > 31:
  print("Please enter valid date")
elif month == "march" and day >= 21 or month == "april" and day <= 19:
  print("Your sun sign is Aries")
elif month == "april" and day >= 20 or month == "may" and day <= 20:
  print("Your sun sign is Taurus")
elif month == "may" and day >= 21 or month == "june" and day <= 21:
  print("Your sun sign is Gemini")
elif month == "june" and day >= 21 or month == "july" and day <= 22:
  print("Your sun sign is Cancer")
elif month == "july" and day >= 21 or month == "august" and day <= 22:
  print("Your sun sign is Leo")
elif month == "august" and day <= 23 or month == "september" and day <= 22:
  print("Your sun sign is Virgo")
elif month == "september" and day >= 23 or month == "october" and day <= 23:
  print("Your sun sign is Libra")
elif month == "october" and day <= 24 or month == "november" and day <= 21:
  print("Your sun sign is Scorpio")
elif month == "november" and day >= 22 or month == "december" and day <= 21:
  print("Your sun sign is Sagittarius")
elif month == "december" and day >= 22 or month == "january" and day <= 19:
  print("Your sun sign is Aquarius")
else:
  print("Your sun sign is Pisces")


