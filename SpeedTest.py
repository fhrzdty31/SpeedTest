import speedtest

st = speedtest.Speedtest()

print(f"\n # Memuat daftar server...")
st.get_servers()

print(f" # Memilih server terbaik...")
best = st.get_best_server()

print(f" #\n # ({best['host']})")
print(f" #\n # {best['country']}")
print(f" #\n # Latitude {best['lat']}\n # Longitude {best['lon']}")

print(f" # \n # Melakukan tes pengunduhan...")
down = st.download() / 1024 / 1024
print(f" # \n # Kecepatan unduh\n # => {down:.2f} Mbps")

print(f" # \n # Melakukan tes pengunggahan...")
up = st.upload() / 1024 / 1024
print(f" # \n # Kecepatan mengunggah\n # => {up:.2f} Mbps")

ping = st.results.ping
print(f" # \n # Ping : {ping:.2f} ms")