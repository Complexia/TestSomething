import subprocess
from sense_hat import SenseHat 
sense = SenseHat()
cpuTemp = subprocess.check_output("vcgencmd measure_temp", shell=True)
print(cpuTemp)
array1 = str(cpuTemp).split("=")

array2 = array1[1].split("'")
cpuTempFloat = float(array2[0])

temp = sense.get_temperature()

actualTemp = temp - ((cpuTempFloat - temp)/7.5)
print(actualTemp)

