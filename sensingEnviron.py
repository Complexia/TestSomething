from sense_hat import SenseHat
sense = SenseHat()

pressure = sense.get_pressure()
temperature = sense.get_temperature()

print(pressure)
print(temperature)