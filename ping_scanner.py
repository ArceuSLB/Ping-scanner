import os
import platform
import subprocess


subnet = "192.168.1."


if platform.system().lower() == "windows":
    param = "-n"  
else:
    param = "-c"  


print(f"\n🔍 Escaneando la red {subnet}1 - {subnet}10...\n")


for i in range(1, 11):
    ip = f"{subnet}{i}"

    
    result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

   
    if result.returncode == 0:
        print(f"{ip} Responde ✅")
    else:
        print(f"{ip} no responde ❌")


print("\n✅ Escaneo finalizado.")

