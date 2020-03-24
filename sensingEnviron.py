from sense_hat import SenseHat
sense = SenseHat()

pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

print(pressure)
print(temperature)
print(humidity)