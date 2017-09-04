city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

# rewrote these lines to use the format method rather than string concatenation
alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions " \
        "will be {}.".format(city, low_temperature, high_temperature, temperature_unit, weather_conditions)

# print the alert
print(alert)