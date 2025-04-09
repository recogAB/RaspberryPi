import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

duration = 5  # sekunder
samplerate = 44100
device_index = 1  # USB PnP Audio Device

# Välj rätt inputenhet
sd.default.device = (2, None)   #direkt i 3.5 port

print("Spelar in...")
data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float64')
sd.wait()
print("Inspelning klar.")

# Skapa tidsaxel
time = np.linspace(0, duration, len(data))

# Plotta signalen
plt.plot(time, data)
plt.xlabel("Tid (s)")
plt.ylabel("Amplitud (normaliserad)")
plt.title("Signal från USB PnP Audio Device")
plt.grid(True)
plt.show()
