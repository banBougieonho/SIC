import subprocess
result = subprocess.run(['vcgencmd', 'measure_temp'],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
a = subprocess.run('pwd')