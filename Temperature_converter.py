print("Your temperature converter")
print("1. Convert fahrenheit to degree celcius")
print("2. Convert degree celcius to fahrenheit")
choice = (int(input("Choose 1 or 2: ")))
if choice == 1:
    fahrenheit = float(input("Input temperature in fahrenheit: "))
    degree_celcius = float(fahrenheit - 32)
    print("Your temperature is", degree_celcius, "degree celcius")
elif choice == 2:
    degree_celcius = float(input("Input temperature in degree celcius: "))
    fahrenheit = float(degree_celcius + 32)
    print("Your temperature is", fahrenheit, "fahrenheit")
else:
    print("Invalid choice")