from sense_hat import SenseHat
sense = SenseHat()

pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

print(pressure)
print(temperature)
print(humidity)

pressure = round(pressure,1)
temperature = round(temperature,1)
humidity = round(humidity,1)

message = (" Pressure: " + str(pressure) + " Temprerature: " + str(temperature) + " Humidity: " + str(humidity))
sense.show_message(message, scroll_speed=0.05)