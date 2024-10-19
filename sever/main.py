import socket
import time
import threading
def get_current_time():
    current_struct_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_struct_time)
    return formatted_time
def log_output(input,input2):
    current_time = get_current_time()
    print("[{0}]".format(current_time),"[{0}]".format(input),input2)
users=[]
main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=("127.0.0.1",1234)
main_server.bind(ip)
main_server.listen(50)
log_output("normal","服务器已启动")
def server_listen(client_socket, client_address):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            broadcast_message(client_socket,data)
    except:
        log_output("exit","{0}的连接断开".format(client_address))
def broadcast_message(self,message,target_client=None):
    for client_socket, client_address in users:
        if target_client is None or client_address == target_client:
            if client_socket==self:
                client_socket.sendall("air".encode('utf-8'))
                break
            client_socket.sendall(message)
while True:
     client_socket, client_address = main_server.accept()
     log_output("join",f"{client_address}已经连接")
     users.append((client_socket, client_address))
     client_thread = threading.Thread(target=server_listen, args=(client_socket, client_address))
     client_thread.start()
