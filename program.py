print("Weather Report")
city = input("Enter city name: ")
temperature = int(input("Enter temperature (in °C): "))

if temperature < 0:
    weather_condition = "Freezing"
elif temperature < 15:
    weather_condition = "Cold"
elif temperature < 25:
    weather_condition = "Mild"
elif temperature < 35:
    weather_condition = "Warm"
else:
    weather_condition = "Hot"

print(f"\nWeather Report for {city}:")
print(f"Temperature: {temperature}°C")
print(f"Weather Condition: {weather_condition}")

if weather_condition == "Freezing" or weather_condition == "Cold":
    print("Advice: Wear warm clothing!")
elif weather_condition == "Mild":
    print("Advice: Enjoy the day!")
elif weather_condition == "Warm" or weather_condition == "Hot":
    print("Advice: Stay hydrated!")
