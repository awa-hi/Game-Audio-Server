import pyaudio
import socket
import threading
# 定义录音参数
CHUNK = 1024  # 每个缓冲区的帧数
FORMAT = pyaudio.paInt16  # 采样位数
CHANNELS = 1  # 声道数
RATE = 44100  # 采样率

# 初始化 PyAudio 对象
p = pyaudio.PyAudio()

# 打开输入流（录音）
stream_in = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   frames_per_buffer=CHUNK)

# 打开输出流（播放）
stream_out = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

print("开始录制和播放...")

SERVER_IP = '127.0.0.1'  # 服务器IP地址
SERVER_PORT = 1234  # 服务器端口


# 创建客户端套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
def input():
    while True:
        # 从输入流读取数据
        data = stream_in.read(CHUNK)
        client_socket.sendall(data)
def out ():
        while True:
            data = client_socket.recv(CHUNK)
            if not data: continue
            stream_out.write(data)

try:
    li_thread = threading.Thread(target=input)
    out_thread = threading.Thread(target=out)
    out_thread.start()
    li_thread.start()
except:
    stream_in.stop_stream()
    stream_in.close()
    stream_out.stop_stream()
    stream_out.close()

    # 终止 PyAudio 对象
    p.terminate()


    