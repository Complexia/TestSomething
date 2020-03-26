import subprocess
cpuTemp = subprocess.check_output("vcgencmd measure_temp", shell=True)
print(cpuTemp)