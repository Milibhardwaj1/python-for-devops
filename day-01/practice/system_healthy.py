# You will create a Python script that:
# - Takes threshold values (CPU, disk, memory) from **user input**
# - Also fetches system metrics using a Python library (example: `psutil`)
# - Compares metrics against thresholds
# - Prints the result to the **terminal**
import psutil
def system_health():
    cpu_threshold = int(input("Enter a CPU Threshold Value: "))
    memory_threshold = int(input("Enter a Memory Threshold Value: "))
    disk_threshold = int(input("Enter a Disk Threshold Value: "))
    current_cpu = psutil.cpu_percent(interval=1)
    print("The current CPU is: ", current_cpu)
    current_memory = psutil.virtual_memory()
    print("The current memory is: ", current_memory)
    current_disk_size = psutil.disk_usage('/')
    print("The current disk_size is: ", current_disk_size)
    if current_cpu>cpu_threshold:
        print("Cpu usage exceeded, send email...")
    else: 
        print("CPU Usage not exceeded.")
    if current_memory.percent>memory_threshold:
        print("Memory usage exceeded, send email...")
    else:
        print("Memory usage not exceeded.")
    if current_disk_size.percent>memory_threshold:
        print("Disk usage exceeded, send email...")
    else:
        print("Disk usage not exceeded.")
system_health()