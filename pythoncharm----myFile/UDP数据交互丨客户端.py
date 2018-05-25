#思路：设置主机与端口，输入数据，发送数据到指定地址
import socket
serverHost="localhost"
serverPort=51880
serverAddress=(serverHost,serverPort)
client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#使用INET地址集，udp传输协议
file = open("123456.txt", "r")
password = file.read()
print("您的密码："+password)
client_socket.sendto((password.encode()), serverAddress)
server_data, server=client_socket.recvfrom(1024)
print("验证结果："+server_data.decode())



