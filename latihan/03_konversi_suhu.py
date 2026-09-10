KELVIN_OFFSET = 273.15

celsius = float(input("Masukkan suhu Celsius: "))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print(f"Suhu Fahrenheit = {fahrenheit:.2f} °F")
print(f"Suhu Kelvin = {kelvin:.2f} K")