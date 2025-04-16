import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

duration = 2  # seconds
fs = 44100

# These are the new USB PnP Audio Device mic inputs that showed up
usb_mic_indices = [4, 15, 30, 44, 46, 47]

for device_index in usb_mic_indices:
    try:
        print(f"\nTesting device index {device_index}...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, device=device_index)
        sd.wait()
        max_amp = np.max(np.abs(audio))
        print(f"Max amplitude: {max_amp}")
        plt.plot(audio)
        plt.title(f"Signal from device index {device_index}")
        plt.xlabel("Sample")
        plt.ylabel("Amplitude")
        plt.show()
    except Exception as e:
        print(f"Error on device {device_index}: {e}")
