import os
import platform
import subprocess

# 1️⃣ Definir la red a escanear
subnet = "192.168.1."

# 2️⃣ Detectar el sistema operativo
if platform.system().lower() == "windows":
    param = "-n"  # Windows usa "-n"
else:
    param = "-c"  # Linux/macOS usa "-c"

# 3️⃣ Mostrar mensaje antes de empezar
print(f"\n🔍 Escaneando la red {subnet}1 - {subnet}10...\n")

# 4️⃣ Escanear direcciones IP del 1 al 10
for i in range(1, 11):
    ip = f"{subnet}{i}"

    # Ejecutar ping con subprocess.run()
    result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 5️⃣ Mostrar si está activo o no
    if result.returncode == 0:
        print(f"{ip} está activo ✅")
    else:
        print(f"{ip} no responde ❌")

# 6️⃣ Mensaje final
print("\n✅ Escaneo finalizado.")

