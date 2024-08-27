import subprocess
import re

def get_cpu_temperature():
    try:
        # Ch?y l?nh vcgencmd measure_temp
        result = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Ki?m tra n?u l?nh ch?y th�nh c�ng
        if result.returncode == 0:
            # L?y k?t qu? t? stdout
            temp_output = result.stdout.strip()
            temp = re.findall(r'\d+\.\d+', temp_output)[0]
            print(temp_output)
            return temp
        else:
            # N?u c� l?i, in ra stderr
            print(f"Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

# S? d?ng h�m get_cpu_temperature d? l?y nhi?t d? CPU
cpu_temp = get_cpu_temperature()
if cpu_temp:
    print(f"CPU Temperature: {cpu_temp}")
else:
    print("Failed to get CPU temperature")
