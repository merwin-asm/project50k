import subprocess
import time

subprocess.Popen(["python", "fastapi_ver.py"])
subprocess.Popen(["python", "dashboard.py"])
subprocess.Popen(["python", "simulation_api.py"])
while True:
    time.sleep(0.3)
