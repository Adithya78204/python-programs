#9.Implement a function to convert a temperature from Celsius to Fahrenheit.

def celsius_to_fahr(celsius):

    return(celsius * 9/5) + 32
temp_celsius = int(input("enter the temp:"))
print(celsius_to_fahr(temp_celsius))