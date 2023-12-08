import socket

# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口号
UDP_PORT = 12123  # 将端口号设为12123
sock.bind(("192.168.136.128", UDP_PORT))  # 将 IP 地址设为虚拟机的 IP 地址

# 接收数据并写入文件
try:
    data, addr = sock.recvfrom(1024)  # 接收第一个数据包，即文件名
    FILE_NAME = data.decode("utf-8").strip()  # 解码并去除空白字符

    with open(FILE_NAME, "wb") as f:  # 使用二进制模式写入文件
        while True:
            data, addr = sock.recvfrom(1024)  # 每次接收1024字节数据
            if not data:
                break
            f.write(data)

except KeyboardInterrupt:
    print("接收被中断")

finally:
    # 关闭套接字
    sock.close()
"""
运行环境:
Python 3.x
Windows、Linux 或 macOS 

配置选项：
sock.bind(("192.168.136.128", UDP_PORT)) 这行代码用于绑定UDP套接字到指定的IP地址和端口号。
   
在接收文件时，首先接收文件名，然后逐块写入数据到文件中。
程序在接收完成或通过键盘中断（Ctrl+C）时结束执行
"""