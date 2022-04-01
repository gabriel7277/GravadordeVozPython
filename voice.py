import sounddevice
from scipy.io.wavfile import write


# Tempo de Gravação

fs = 55100
second = int(input(" Defina o tempo de Gravação "))

print("\nGravando...\n")

# Captura Gravação

record_voice = sounddevice.rec(int(second*fs), samplerate=fs, channels=2)
sounddevice.wait()

# salvar arquivo

write("gravação.wav", fs, record_voice)
print("Gravação Finalizada!")
