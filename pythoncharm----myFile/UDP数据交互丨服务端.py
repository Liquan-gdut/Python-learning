#思路：设置主机、端口号、创建socket对象、绑定地址、接收数据和客户端名、打印
import socket
serverHost="localhost"
serverPort=51880
Address=(serverHost,serverPort)
server_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#使用INET地址集，udp传输协议
server_socket.bind(Address)
print("等待中...")
client_data, clientAddress = server_socket.recvfrom(1024)
print("接收到来自%s 传来的：%s " % (clientAddress, client_data.decode()))
if client_data.decode() == "123456":
    server_data = "correct"
else:
    server_data = "error"
server_socket.sendto(server_data.encode(),clientAddress)

# bug:一直出现“python an integer is required (got type str)”；解决：一开始将“clientAddress”设成一个固定值
