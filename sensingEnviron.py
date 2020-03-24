from sense_hat import SenseHat
sense = SenseHat()

pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

print(pressure)
print(temperature)
print(humidity)

pressure = pressure.round(pressure,1)
temperature = temperature.round(temperature,1)
humidity = humidity.round(humidity,1)

message = (" Pressure: " + str(pressure) + " Temprerature: " + str(temperature) + " Humidity: " + str(humidity))
sense.show_message(message, scroll_speed=0.05)