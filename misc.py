import subprocess
import time
subprocess.run(['python', 'main.py'])
time.sleep(300)
subprocess.run(['python', 'hf.py'])