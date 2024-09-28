# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

# User interaction
def main():
    # Step 1: Get temperature input from user
    temperature = input("Enter the temperature to convert: ")

    # Step 2: Validate that the input is a number
    try:
        temperature = float(temperature)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Step 3: Get the temperature unit (Celsius or Fahrenheit)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Step 4: Convert the temperature based on the unit
    if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    elif unit == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the program
if __name__ == "__main__":
    main()
 
