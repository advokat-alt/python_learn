weather = input("What is the weather? ").strip().lower()

if weather == "sunny":
    print("go outside")
elif weather == "raining":
    print("stay at home")
else:
    print("weather not recognized")
