"""
Temperature Converter

Description: A simple Python program to convert temperatures between Celsius, Fahrenheit, and Kelvin.
Includes input validation and supports bidirectional conversion between all three scales.

Time Complexity: O(1) - Constant time operations
Space Complexity: O(1) - Uses constant space
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def get_valid_temperature(prompt):
    """Get a valid temperature input from user"""
    while True:
        try:
            temp = float(input(prompt))
            return temp
        except ValueError:
            print("Please enter a valid number!")

def display_conversion_table():
    """Display common temperature conversions for reference"""
    print("\n" + "="*50)
    print("COMMON TEMPERATURE CONVERSIONS")
    print("="*50)
    print("°C     °F     K     Description")
    print("-"*50)
    
    common_temps = [
        (-40, -40, 233.15, "Extreme Cold"),
        (0, 32, 273.15, "Freezing Point"),
        (20, 68, 293.15, "Room Temperature"),
        (37, 98.6, 310.15, "Human Body"),
        (100, 212, 373.15, "Boiling Point")
    ]
    
    for c, f, k, desc in common_temps:
        print(f"{c:4.1f}  {f:5.1f}  {k:6.2f}  {desc}")

def main():
    """Main function to run the temperature converter"""
    print("="*50)
    print("        TEMPERATURE CONVERTER")
    print("="*50)
    
    while True:
        print("\nConversion Options:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Display Conversion Table")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            celsius = get_valid_temperature("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
            
        elif choice == '2':
            fahrenheit = get_valid_temperature("Enter temperature in Fahrenheit: ")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
            
        elif choice == '3':
            celsius = get_valid_temperature("Enter temperature in Celsius: ")
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius:.2f}°C = {kelvin:.2f}K")
            
        elif choice == '4':
            kelvin = get_valid_temperature("Enter temperature in Kelvin: ")
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin:.2f}K = {celsius:.2f}°C")
            
        elif choice == '5':
            fahrenheit = get_valid_temperature("Enter temperature in Fahrenheit: ")
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit:.2f}°F = {kelvin:.2f}K")
            
        elif choice == '6':
            kelvin = get_valid_temperature("Enter temperature in Kelvin: ")
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin:.2f}K = {fahrenheit:.2f}°F")
            
        elif choice == '7':
            display_conversion_table()
            
        elif choice == '8':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter 1-8.")

# Test functions
def run_tests():
    """Run tests to verify conversion accuracy"""
    print("Running tests...")
    
    test_cases = [
        (0, 32, 273.15),      # Freezing point
        (100, 212, 373.15),   # Boiling point
        (-40, -40, 233.15),   # Equal point
        (37, 98.6, 310.15),   # Body temperature
    ]
    
    passed = 0
    for celsius, fahrenheit, kelvin in test_cases:
        # Test Celsius to Fahrenheit
        calc_f = celsius_to_fahrenheit(celsius)
        f_match = abs(calc_f - fahrenheit) < 0.1
        
        # Test Celsius to Kelvin
        calc_k = celsius_to_kelvin(celsius)
        k_match = abs(calc_k - kelvin) < 0.1
        
        # Test Fahrenheit to Celsius
        calc_c = fahrenheit_to_celsius(fahrenheit)
        c_match = abs(calc_c - celsius) < 0.1
        
        if f_match and k_match and c_match:
            print(f"✓ PASS: {celsius}°C = {fahrenheit}°F = {kelvin}K")
            passed += 1
        else:
            print(f"✗ FAIL: {celsius}°C")
            print(f"  Expected: {fahrenheit}°F, {kelvin}K")
            print(f"  Got: {calc_f:.2f}°F, {calc_k:.2f}K")
    
    print(f"\nTest Results: {passed}/{len(test_cases)} passed")
    return passed == len(test_cases)

if __name__ == "__main__":
    # Run tests first
    if run_tests():
        print("\nAll tests passed! Starting interactive mode...\n")
        main()
    else:
        print("\nSome tests failed! Please check the implementation.")
