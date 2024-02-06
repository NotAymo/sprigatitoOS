import time

print("[os-host] Launching os...")
time.sleep(1)
print("[os-services] Loading services...")
print("[os-ui] Launching UI...")
time.sleep(1)
exec(open('src/home.py').read())
