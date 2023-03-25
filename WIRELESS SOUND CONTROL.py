import pip

pip install pyaudio
import socket
import pyaudio

# initialize PyAudio
audio = pyaudio.PyAudio()

# set up socket
HOST = ''    # the server's hostname or IP address
PORT = 12345  # the port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f"Server listening on port {PORT}")

# accept connection from client
conn, addr = s.accept()
print(f"Connected by {addr}")

# set up stream for playback
stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

# receive sound data from client and play it back
while True:
    data = conn.recv(1024)
    if not data:
        break
    stream.write(data)

# clean up
stream.stop_stream()
stream.close()
audio.terminate()
conn.close()
import socket
import pyaudio

# initialize PyAudio
audio = pyaudio.PyAudio()

# set up socket
HOST = 'localhost'    # the server's hostname or IP address
PORT = 12345         # the port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# set up stream for recording
stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# record sound and send it to server
while True:
    data = stream.read(1024)
    s.sendall(data)

# clean up
stream.stop_stream()
stream.close()
audio.terminate()
s.close()
